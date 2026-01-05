# QA Case Study Test Plan

## Objectives
1. Fix flaky login tests (Part 1)
2. Design scalable framework (Part 2)
3. Validate end-to-end project flow with security (Part 3)

## Assumptions
- Test environment is **staging**, not production
- **2FA is disabled** for all test users
- API accepts requests with static test token
- Tenant isolation enforced via subdomain + `X-Tenant-ID`
- Mobile testing simulated locally; BrowserStack used in CI

## Test Data Strategy
- Use **unique project names** (UUID suffix) to avoid collisions
- No real cleanup in code (would use teardown hooks in real framework)
- Credentials hardcoded for demo (in real: loaded from secure config)

## Risks & Limitations
- No real BrowserStack integration (no credentials)
- No 2FA handling (assumed off)
- API mock assumed stable

## Success Criteria
- All tests pass **consistently** in CI
- Tenant isolation verified
- Mobile responsiveness checked