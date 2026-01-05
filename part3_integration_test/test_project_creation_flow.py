import uuid
import requests
from playwright.sync_api import sync_playwright

# ASSUMPTIONS:
# - Staging environment allows test API calls
# - Auth token is obtainable (here mocked for simplicity)
# - Tenant subdomains: company1.workflowpro.com, company2.workflowpro.com
# - 2FA is disabled for test users

def test_project_creation_flow():
    # 1. API: Create a unique project via API
    project_name = f"Test Project - {uuid.uuid4().hex[:8]}"
    api_url = "https://api.workflowpro.com/v1/projects"
    headers = {
        "Authorization": "Bearer fake_test_token_for_staging",
        "X-Tenant-ID": "company1"
    }
    payload = {
        "name": project_name,
        "description": "Created via automation test",
        "team_members": ["user1@company1.com"]
    }

    # Create project
    response = requests.post(api_url, json=payload, headers=headers)
    assert response.status_code == 201, f"API failed: {response.text}"
    project_id = response.json()["id"]

    try:
        # 2. Web UI: Verify project appears in company1 dashboard
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Login as company1 user
            page.goto("https://company1.workflowpro.com/login")
            page.fill("#email", "admin@company1.com")
            page.fill("#password", "password123")
            page.click("#login-btn")
            page.wait_for_url("https://company1.workflowpro.com/dashboard")

            # Go to projects and verify
            page.goto("https://company1.workflowpro.com/projects")
            page.wait_for_selector(f"text={project_name}", timeout=10000)
            assert page.is_visible(f"text={project_name}")

            # 3. Mobile: Simulate mobile view (BrowserStack concept)
            page.set_viewport_size({"width": 390, "height": 844})  # iPhone 14
            assert page.is_visible(f"text={project_name}")

            browser.close()

        # 4. Security: Verify tenant isolation (NOT visible in company2)
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Login as company2 user
            page.goto("https://company2.workflowpro.com/login")
            page.fill("#email", "user@company2.com")
            page.fill("#password", "password123")
            page.click("#login-btn")
            page.wait_for_url("https://company2.workflowpro.com/dashboard")

            page.goto("https://company2.workflowpro.com/projects")
            page.wait_for_selector(".project-card", timeout=10000)

            # Ensure project is NOT visible
            page_content = page.content()
            assert project_name not in page_content, \
                "Security violation: Project visible in wrong tenant!"

            browser.close()

    finally:
        # OPTIONAL: Cleanup (would use DELETE /api/v1/projects/{id} in real setup)
        # requests.delete(f"{api_url}/{project_id}", headers=headers)
        pass