# Part 1: Debugging Flaky Test – Summary

## Flakiness Issues Identified
1. **Trailing spaces in URLs** → invalid navigation  
2. **No waits after login click** → race condition with dynamic dashboard load  
3. **Fragile URL assertion** (`==`) instead of pattern/wait  
4. **Instant visibility check** (`is_visible()`) without waiting for element render  
5. **No handling of variable tenant load times**  
6. **Assumes no 2FA**, but some users require it (per context)  

## Root Causes in CI vs Local
- CI environments are **slower** (CPU, network) → timeouts on dynamic content  
- **No human-like delays** → race conditions exposed  
- **Inconsistent browser/screen sizes** → layout shifts or missed renders  

## Fixes Applied
- Removed trailing spaces in URLs  
- Replaced direct URL assertion with `page.wait_for_url()`  
- Replaced `is_visible()` with `page.wait_for_selector(..., state="visible")`  
- Added explicit wait before reading `.project-card` list  
- Kept original structure (no fixtures/helpers) — minimal necessary changes only  