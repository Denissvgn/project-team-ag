---
description: Initialize a new project with vision and scope
---

# Project Initialization Workflow

## Trigger
Use when starting a new project or feature set.

## Prerequisites
- User request describing the project/feature
- Access to PM and PO skills

## Steps

### Step 1: Receive User Request
PM receives initial project description from User.

```
Input: User's natural language description of what they want to build
Output: Parsed project requirements
```

### Step 2: Invoke Product Owner
PM activates the `product-owner` skill to create Vision draft.

```
Action: Use @skill product-owner
Input: User request + any existing context
Output: Draft Vision document
```

**Vision Document includes:**
- Business Goal
- Target Users
- Success Metrics
- In-Scope / Out-of-Scope items
- Constraints

### Step 3: User Validation
PM presents Vision to User for approval.

**Decision Point:**
- ❌ **Rejected**: Return to Step 2 with feedback. PM provides specific feedback to PO.
- ✅ **Approved**: Proceed to Step 4.

### Step 4: Create Iteration Structure
PM creates the 3-iteration cycle scaffold.

```
Iteration 1: PLANNING
├── Research (RE)
├── Analysis (AN)
├── Architecture (AR)
├── Design (DS)
└── Quality Gate (CR, SA)

Iteration 2: DEVELOPMENT
├── Frontend (FD)
├── Backend (BD)
├── DevOps (DO)
├── Security Review (SA)
├── Documentation (TW)
└── Merge (MA)

Iteration 3: VERIFICATION
├── Testing (QA)
├── Coverage Review (CR)
├── Vision Check (PO)
└── Decision Loop (PM)
```

### Step 5: Initialize Project Timeline
PM creates initial Gantt chart using MCP tools.

```
Action: @mcp gantt-tools create_project
Input: Iteration structure, estimated durations
Output: Project timeline
```

### Step 6: Begin Planning Iteration
PM transitions to `/workflow planning-iteration`.

## Outputs
- ✅ Approved Vision document
- ✅ 3-iteration structure defined
- ✅ Initial Gantt chart created
- ✅ Ready for Planning phase

## Next Step
→ `/workflow planning-iteration`
