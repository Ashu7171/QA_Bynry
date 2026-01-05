import pytest
from playwright.sync_api import sync_playwright

def test_user_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # FIXED: Removed trailing spaces in URL
        page.goto("https://app.workflowpro.com/login")
        
        page.fill("#email", "admin@company1.com")
        page.fill("#password", "password123")
        page.click("#login-btn")
        
        # FIXED: Wait for navigation to complete
        page.wait_for_url("https://app.workflowpro.com/dashboard")
        
        # FIXED: Wait for element to be visible
        page.wait_for_selector(".welcome-message", state="visible")
        
        browser.close()

def test_multi_tenant_access():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # FIXED: Clean URL
        page.goto("https://app.workflowpro.com/login")
        page.fill("#email", "user@company2.com")
        page.fill("#password", "password123")
        page.click("#login-btn")
        
        # FIXED: Wait for projects to load
        page.wait_for_selector(".project-card")
        
        projects = page.locator(".project-card").all()
        for project in projects:
            assert "Company2" in project.text_content()
        
        browser.close()