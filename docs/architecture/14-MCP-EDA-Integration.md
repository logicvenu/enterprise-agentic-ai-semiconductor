# 14 — MCP / EDA Integration

**Project:** Semiconductor Enterprise AI Platform
**Pattern:** Pattern 2 — Hybrid AI Platform
**Artifact:** 14 of 22
**Status:** DRAFT FOR REVIEW

## Frozen predecessors
01 Business Problem — FROZEN v1.0
02 Architecture Drivers — FROZEN v1.0
03 Functional Requirements — FROZEN v1.0
04 NFRs — FROZEN v1.0
05 C4 Context — FROZEN v1.0
06 Layered Architecture — FROZEN v1.0
07 C4 Container — FROZEN v1.0
08 C4 Component — FROZEN v1.0
09 Runtime / Sequence — FROZEN v1.0
10 Data Flow — FROZEN v1.0
11 AI Model Strategy — FROZEN v1.0
12 RAG / Knowledge Architecture — FROZEN v1.0
13 Agent Architecture — FROZEN v1.0

---

# 1. Purpose

Artifact 14 defines how agents securely interact with semiconductor engineering tools and systems.

The central question is:

> **How can AI agents use EDA and engineering tools without directly coupling the agent runtime to proprietary tools, repositories and execution environments?**

The architecture treats MCP as an **integration protocol/capability**, not as the AI platform, agent runtime or EDA tool itself.

---

# 2. Core Principle

```text
Agent
  ↓
Tool Capability
  ↓
Tool / EDA Gateway
  ↓
MCP / Integration Layer
  ↓
Policy / Authorization
  ↓
EDA / Engineering System
```

The agent asks for a capability. The platform controls whether, where and how that capability can be executed.

---

# 3. MCP Is Not the Platform

Keep these boundaries explicit:

```text
MCP
  ≠ Agent Framework
  ≠ Agent Runtime
  ≠ EDA Tool
  ≠ Tool Gateway
  ≠ Security Boundary
```

MCP can provide a standardized mechanism for exposing tools and contextual resources, but enterprise authorization, network isolation, auditing, approval and policy remain platform responsibilities.

---

# 4. EDA Ecosystem

Representative engineering systems include:

- RTL/source repositories
- Verification repositories
- Simulation engines
- Regression systems
- EDA analysis tools
- Physical-design tools
- DFT tools
- License services
- Engineering databases
- Ticketing systems
- Artifact/report stores
- CI/CD and build systems

The exact vendor/tool portfolio remains environment-specific.

---

# 5. 14-A — EDA Ecosystem Landscape

```text
                    Engineering Workflows
                            |
                         AI Agents
                            |
                    Tool / EDA Gateway
                            |
                 MCP / Integration Layer
                            |
        +---------+---------+---------+---------+
        |         |         |         |         |
       RTL      Verify    Sim       PD/DFT    Repos
       Tools    Tools     Tools      Tools
        |         |         |         |
        +---------+---------+---------+---------+
                            |
                     Engineering Data
```

The gateway prevents every agent from creating its own point-to-point EDA integration.

---

# 6. Tool Capability Model

Expose capabilities rather than raw infrastructure.

Examples:

```text
Repository
  read_file
  search_code
  compare_change

Regression
  get_status
  get_failure
  get_logs
  rerun

Simulation
  inspect_result
  retrieve_waveform
  run_simulation

EDA Analysis
  run_analysis
  retrieve_report
  inspect_violation

Engineering
  create_ticket
  update_status
  retrieve_artifact
```

The final tool catalog is determined by approved workflows.

---

# 7. 14-B — MCP Architecture

```text
Agent Runtime
      ↓
Tool / EDA Gateway
      ↓
MCP Client / Integration Adapter
      ↓
+-------------------------------+
| MCP Tool / Resource Servers   |
+-------------------------------+
      ↓
Enterprise Tool Adapters
      ↓
EDA / Engineering Systems
```

The MCP layer standardizes interaction where appropriate.

The Tool / EDA Gateway remains the enterprise control boundary.

---

# 8. MCP Server Responsibilities

An MCP server/integration endpoint can expose:

### Tools
Actions the agent can invoke.

### Resources
Contextual engineering information.

### Prompts
Reusable interaction patterns where appropriate.

The platform should still apply enterprise policy around these capabilities.

---

# 9. Tool / EDA Gateway Responsibilities

The gateway provides:

- Authentication
- Authorization
- Agent identity
- User delegation context
- Tool discovery
- Policy enforcement
- Risk classification
- Parameter validation
- Rate limiting
- Approval routing
- Audit
- Observability
- Network routing
- Execution controls

This is why:

> **MCP is an integration mechanism; the Tool / EDA Gateway is the enterprise control plane.**

---

# 10. 14-C — Agent → MCP → EDA Runtime

```text
Engineer
   ↓
Agent
   ↓
Plan
   ↓
Tool Capability Request
   ↓
Tool / EDA Gateway
   ↓
Policy Check
   ↓
MCP Integration
   ↓
EDA Tool
   ↓
Execution
   ↓
Result
   ↓
Validation
   ↓
Agent
   ↓
Engineer
```

For consequential operations, approval is inserted before execution.

---

# 11. Tool Discovery

Logical discovery:

```text
Agent
  ↓
Tool Gateway
  ↓
Approved Capability Catalog
  ↓
Available Tool
  ↓
Tool Schema
  ↓
Agent Planning
```

Agents should discover only tools permitted for their identity, workflow and environment.

---

# 12. Tool Contracts

Every exposed tool should have an explicit contract:

```text
Tool ID
Purpose
Inputs
Input Schema
Outputs
Output Schema
Required Permissions
Risk Level
Allowed Environments
Timeout
Rate Limit
Audit Requirements
Approval Requirement
Version
Owner
```

This makes tool invocation predictable and governable.

---

# 13. Tool Risk Classification

A logical classification:

```text
READ
 ↓
ANALYZE
 ↓
CREATE / UPDATE
 ↓
EXECUTE
 ↓
DESTRUCTIVE / HIGH IMPACT
```

Examples:

| Risk | Example | Control |
|---|---|---|
| Low | Read report | Policy |
| Low/Medium | Search repository | Policy |
| Medium | Create ticket | Policy / approval |
| High | Start expensive regression | Approval / budget |
| High | Modify engineering artifact | Strong approval |
| Critical | Destructive operation | Explicit human control |

Exact classification is environment-specific.

---

# 14. 14-D — MCP Server / Tool Architecture

```text
                    Tool / EDA Gateway
                           |
              +------------+------------+
              |            |            |
              v            v            v
        Repository      Regression     EDA
        MCP Server      MCP Server    MCP Server
              |            |            |
              v            v            v
           Git/Repo      Regression   EDA Tools
                         Platform
```

Multiple MCP servers can specialize by engineering domain.

The architecture does not require one universal MCP server.

---

# 15. EDA Integration Patterns

### Pattern A — Direct adapter

```text
MCP Server → EDA API
```

Use when an approved API exists.

### Pattern B — Command wrapper

```text
MCP Server → Controlled Command Runner → EDA Tool
```

Use when the tool is primarily command-line driven.

### Pattern C — Job service

```text
MCP Server → Job Service → Queue / Scheduler → EDA Environment
```

Useful for long-running simulations and regressions.

### Pattern D — Source-local integration

```text
MCP Server
     ↓
Private EDA Environment
```

Useful for sensitive or isolated environments.

---

# 16. 14-E — EDA Tool Integration

```text
Agent
  ↓
Tool Gateway
  ↓
MCP
  ↓
Integration Adapter
  ↓
+--------------------+
| EDA Execution      |
| Environment        |
+--------------------+
  ↓
Tool / Job
  ↓
Report / Result
  ↓
Artifact Store
  ↓
Agent
```

Long-running EDA operations should be treated as jobs rather than synchronous model/tool calls.

---

# 17. Synchronous vs Asynchronous Tools

### Synchronous

Suitable for:

- Read metadata
- Search repository
- Retrieve report
- Simple analysis

```text
Request → Tool → Result
```

### Asynchronous

Suitable for:

- Simulation
- Regression
- Synthesis
- Physical analysis
- Large EDA jobs

```text
Request
  ↓
Job Accepted
  ↓
Queue / Scheduler
  ↓
EDA Execution
  ↓
Result
  ↓
Notification / Poll
```

---

# 18. Long-Running Job Control

An agent should not continuously hold a model execution open while an EDA job runs.

Instead:

```text
Agent
 ↓
Submit Job
 ↓
Job ID
 ↓
Persist State
 ↓
EDA Execution
 ↓
Completion Event / Poll
 ↓
Retrieve Result
 ↓
Resume Workflow
```

This reduces coupling and improves resilience.

---

# 19. 14-F — Secure Tool Execution

```text
Agent Request
      ↓
Agent Identity
      ↓
User / Project Context
      ↓
Policy Evaluation
      ↓
Tool Authorization
      ↓
Input Validation
      ↓
Risk Classification
      ↓
Human Approval?
      ↓
MCP Integration
      ↓
EDA Execution
      ↓
Audit / Telemetry
```

No direct agent-to-EDA connection is permitted.

---

# 20. Identity and Delegation

The platform should preserve:

```text
Human
  ↓
Agent Invocation
  ↓
Agent Identity
  ↓
Delegated Authorization
  ↓
Tool Execution
```

The system must be able to determine:

- Who initiated the action?
- Which agent requested it?
- Which tool was called?
- Under which project/context?
- Which policy permitted it?
- What was executed?

---

# 21. Secrets and Credentials

Agents should never receive raw EDA credentials.

```text
Agent
  ↓
Tool Gateway
  ↓
Credential / Secret Boundary
  ↓
EDA Service Identity
  ↓
Tool
```

Credentials remain outside model context and agent state.

---

# 22. Network Security

Hybrid deployment may require:

```text
AWS
  |
Secure Connectivity
  |
Private / On-Prem
  |
EDA Environment
```

The integration layer should support:

- Private connectivity
- Network segmentation
- Egress control
- Service identity
- Allow-listed endpoints
- Protocol restrictions

Exact network architecture is deferred to Artifact 15/16.

---

# 23. 14-G — Read vs Write / Action Boundaries

```text
                 Tool Capability
                       |
             +---------+---------+
             |                   |
            READ               ACTION
             |                   |
       Lower Risk          Higher Risk
             |                   |
          Policy          Policy + Approval
                               |
                       Controlled Execute
```

The platform separates observation from consequential action.

---

# 24. Read-Only First Strategy

For initial deployment:

```text
Phase 1
Read
  ↓
Analyze
  ↓
Recommend
  ↓
Human Review

Phase 2
Approved Actions

Phase 3
Controlled Automation
```

This provides a safer path to production adoption.

---

# 25. EDA Artifact Handling

EDA operations may generate:

- Logs
- Reports
- Waveforms
- Coverage data
- Netlists
- Simulation artifacts
- Error files
- Analysis results

Agents should receive only the relevant result/context rather than unrestricted filesystem access.

---

# 26. Tool Output Normalization

```text
EDA Tool
   ↓
Raw Output
   ↓
Adapter
   ↓
Normalized Result
   ↓
Tool Gateway
   ↓
Agent
```

Normalized results improve portability across different tools and vendors.

---

# 27. Tool Versioning

Tool contracts and integrations should be versioned.

```text
Tool Capability v1
       ↓
Adapter v1
       ↓
EDA Tool Version X
```

Upgrading an EDA tool should not automatically break agent workflows.

The gateway provides a compatibility boundary.

---

# 28. MCP Governance

Govern:

- Server registration
- Tool registration
- Tool schemas
- Versioning
- Ownership
- Security review
- Permissions
- Risk classification
- Environment placement
- Logging
- Retirement

No unregistered MCP server should become an enterprise production dependency.

---

# 29. 14-H — MCP Governance & Lifecycle

```text
Develop
   ↓
Register
   ↓
Security Review
   ↓
Tool Evaluation
   ↓
Approve
   ↓
Deploy
   ↓
Monitor
   ↓
Version
   ↓
Re-certify
   ↓
Retire
```

---

# 30. MCP Observability

Capture:

```text
Request ID
Agent ID
User ID
Tool ID
MCP Server
Tool Version
Input Metadata
Execution Time
Status
Result Metadata
Error
Approval
Cost
EDA Job ID
```

Sensitive tool inputs and outputs should follow data-classification policies.

---

# 31. Example — Regression Diagnosis

```text
Regression Failure
       ↓
Agent
       ↓
get_failure()
       ↓
MCP / Regression Server
       ↓
Regression Platform
       ↓
Failure Log
       ↓
Knowledge Gateway
       ↓
Related RTL / Specs
       ↓
Agent Analysis
       ↓
Root Cause Candidate
       ↓
Engineer Review
```

The agent uses **read-oriented tools** initially.

---

# 32. Example — Controlled Regression Rerun

```text
Agent
 ↓
Determine rerun required
 ↓
Tool Request
 ↓
Policy
 ↓
Risk Check
 ↓
Human Approval
 ↓
MCP / Regression Server
 ↓
Job Submission
 ↓
Job ID
 ↓
Regression Execution
 ↓
Result
 ↓
Agent Analysis
```

This demonstrates bounded agentic automation.

---

# 33. MCP and Knowledge Architecture

MCP can expose contextual resources, but enterprise knowledge remains governed by Artifact 12.

```text
Agent
 ├── Knowledge Capability
 │       ↓
 │   Knowledge Gateway
 │
 └── Tool Capability
         ↓
     Tool / EDA Gateway
         ↓
        MCP
```

The two paths are related but remain architecturally distinct.

---

# 34. MCP and Agent Architecture

Artifact 13 defines:

> **What the agent is allowed to do.**

Artifact 14 defines:

> **How the agent reaches engineering tools under those controls.**

Therefore:

```text
Agent Policy
     ↓
Tool Capability
     ↓
Tool Gateway
     ↓
MCP
     ↓
EDA
```

---

# 35. Architectural Decisions

### AD-14-01 — MCP as Integration Capability
MCP is used where it improves standardized tool/context integration; it is not the platform control plane.

### AD-14-02 — Tool / EDA Gateway as Enterprise Boundary
All agent-to-tool access passes through the governed gateway.

### AD-14-03 — Capability-Based Tool Exposure
Expose approved engineering capabilities rather than arbitrary commands.

### AD-14-04 — Least Privilege
Tool permissions are scoped by agent, user, project, environment and workflow.

### AD-14-05 — Read Before Write
Initial AI adoption emphasizes read/analyze/recommend workflows before controlled actions.

### AD-14-06 — Human Approval for High-Risk Actions
Consequential operations require explicit approval where policy requires it.

### AD-14-07 — Async EDA Jobs
Long-running EDA operations use asynchronous job semantics.

### AD-14-08 — Credential Isolation
Agents and models never receive raw EDA credentials.

### AD-14-09 — Tool Contract Versioning
Tool capabilities are versioned independently from underlying EDA implementations.

### AD-14-10 — MCP Lifecycle Governance
MCP servers and tools are registered, reviewed, monitored, versioned and retired.

---

# 36. Trade-offs

## Direct EDA Integration vs MCP

Direct integration can be simpler for one application but creates point-to-point coupling.

MCP can standardize tool interaction but does not remove the need for enterprise security, governance and adapters.

## One MCP Server vs Domain-Specific Servers

One server is simpler initially.

Domain-specific servers provide stronger isolation and ownership boundaries.

## Synchronous vs Asynchronous

Synchronous calls are simple for short operations.

Asynchronous jobs are better for long-running EDA workloads.

## Read vs Write

Read-only operations have lower operational risk.

Write/execute operations provide greater automation value but require stronger governance.

---

# 37. What Artifact 14 Does Not Decide

Still deferred:

- Specific MCP server products
- Exact MCP SDK/runtime
- EDA vendor integration method
- AWS networking services
- Kubernetes deployment
- Specific API gateway
- Secrets-management product
- Queue/scheduler product
- Exact EDA tool catalog
- Exact authorization implementation

Those decisions follow infrastructure and security architecture.

---

# 38. Traceability

```text
13 Agent Architecture
        ↓
Tool / EDA Gateway
        ↓
14 MCP / EDA Integration
        ↓
MCP / Integration Adapters
        ↓
EDA Systems
        ↓
15 AI Infrastructure
        ↓
16 Air-Gapped Architecture
        ↓
17 CI/CD / MLOps / LLMOps / AgentOps
```

Artifact 14 is the bridge between **agent orchestration** and the **engineering tool ecosystem**.

---

# 39. Acceptance Criteria

- [ ] EDA ecosystem defined.
- [ ] MCP role clearly defined.
- [ ] MCP separated from agent runtime.
- [ ] Tool / EDA Gateway defined.
- [ ] Tool capability model defined.
- [ ] Tool contracts defined.
- [ ] Tool discovery defined.
- [ ] Risk classification defined.
- [ ] MCP server architecture defined.
- [ ] EDA integration patterns defined.
- [ ] Sync/async execution defined.
- [ ] Long-running job control defined.
- [ ] Secure tool execution defined.
- [ ] Identity/delegation defined.
- [ ] Credential isolation defined.
- [ ] Network security boundaries defined.
- [ ] Read/write boundaries defined.
- [ ] Read-only-first adoption strategy defined.
- [ ] EDA artifact handling defined.
- [ ] Tool output normalization defined.
- [ ] Tool versioning defined.
- [ ] MCP governance/lifecycle defined.
- [ ] MCP observability defined.
- [ ] Regression diagnosis example defined.
- [ ] Controlled regression rerun example defined.
- [ ] Knowledge/MCP boundary defined.
- [ ] Agent/MCP boundary defined.
- [ ] Architectural decisions recorded.
- [ ] Trade-offs documented.
- [ ] No premature technology selection introduced.

# Status

**14 — MCP / EDA Integration — DRAFT FOR REVIEW**

Next:

> **15 — AI Infrastructure**
