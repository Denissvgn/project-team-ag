---
description: Execute Verification iteration (Iteration 3) - Testing, Review, Vision Check, Decision
---

# Verification Iteration Workflow

## Trigger
Use after completing Development iteration.

## Goal
Verify that implementation meets requirements and Vision.

## Steps

### Step 1: Test Execution
PM activates test engineer skill.

```
Action: @skill test-engineer
Input: Main branch code, Requirements, Acceptance criteria
Output: Test suites, Test execution report
```

**QA deliverables:**
- Unit tests
- Integration tests
- E2E tests (if applicable)
- Test coverage report
- List of failing tests (if any)

### Step 2: Coverage Validation
PM activates critic for test coverage review.

```
Action: @skill critic
Input: Test report, Requirements
Output: Coverage validation report
```

**CR Checklist:**
- [ ] All acceptance criteria have tests
- [ ] Edge cases covered
- [ ] Error scenarios tested
- [ ] Coverage meets threshold (e.g., 80%)

**Decision Point:**
- ❌ **Insufficient Coverage**: Return to QA with feedback
- ✅ **Adequate Coverage**: Proceed to Step 3

### Step 3: Vision Check
PM activates Product Owner for final validation.

```
Action: @skill product-owner
Input: Implemented features, Original Vision
Output: Vision Validation Report
```

**PO Assessment:**
- Compare implementation against Vision
- Identify any deviations
- Classify issues by severity:
  - **CRITICAL**: Blocks release completely
  - **HIGH**: Major deviation from Vision
  - **MEDIUM**: Needs fix before release
  - **LOW**: Minor, acceptable deviation

### Step 4: Decision Loop
PM evaluates PO report and decides next action.

---

## Decision Logic

### Scenario A: Issues >= MEDIUM

If PO found issues at **MEDIUM** severity or higher:

1. **Create New Cycle**
   - PM generates new 3-iteration structure
   - Scope = ONLY the issues found by PO
   - Original Vision remains unchanged

2. **Restart Workflow**
   ```
   → /workflow planning-iteration
   ```
   But scoped to fixing identified issues.

### Scenario B: Issues <= LOW (or NONE)

If all issues are **LOW** severity or none found:

1. **Finalize Iteration**
   ```
   Action: @mcp gantt-tools complete_iteration
   Output: Iteration marked complete
   ```

2. **Update Vision**
   - PM triggers PO to update Vision
   - New features now marked as "existing"
   - Scope cleared for next feature set

3. **Await Next Request**
   - PM notifies User that cycle is complete
   - System awaits new User request
   - OR proceeds to next planned feature set

---

## Summary Decision Tree

```
Verification Complete
        │
        ▼
┌───────────────────┐
│  PO Vision Check  │
└─────────┬─────────┘
          │
    Issues Found?
          │
    ┌─────┴─────┐
    │           │
  >= MEDIUM   <= LOW
    │           │
    ▼           ▼
┌─────────┐ ┌─────────────┐
│New Cycle│ │Finalize     │
│Planning │ │Update Vision│
│Iteration│ │Await Next   │
└─────────┘ └─────────────┘
```

## Outputs

### If Continuing (Scenario A):
- New iteration cycle created
- Scope = PO issue list
- → Planning Iteration

### If Complete (Scenario B):
- ✅ All tests passing
- ✅ Coverage validated
- ✅ Vision confirmed
- ✅ Documentation complete
- ✅ Ready for release/deployment

## Next Step
- **Issues >= MEDIUM**: → `/workflow planning-iteration` (new cycle)
- **Issues <= LOW**: → Notify User, await next request
