# Part 3: API + UI Integration Test – Summary

## Test Flow
1. **API**: Create a unique project via `POST /api/v1/projects`  
2. **Web UI**: Log in as company1 user and verify project appears in dashboard  
3. **Mobile**: Simulate mobile viewport to check responsiveness (BrowserStack concept)  
4. **Security**: Log in as company2 user and confirm project is **not visible** (tenant isolation)

## Key Strategies
- **Unique test data**: Project name includes UUID suffix to avoid collisions  
- **Explicit waits**: `wait_for_selector()` ensures elements load before validation  
- **Mobile simulation**: Uses Playwright’s `set_viewport_size()` (in CI, would run on BrowserStack with real iOS/Android devices)  
- **Tenant isolation**: Explicit cross-tenant validation to catch security leaks  
- **Error resilience**: Assertions include clear failure messages; timeouts set to 10s  

## Assumptions
- Staging environment allows test API calls with static token  
- 2FA is **disabled** for test users  
- Tenant subdomains: `company1.workflowpro.com`, `company2.workflowpro.com`  
- Real BrowserStack execution would use remote WebKit/Android drivers in CI (simulated locally via viewport)