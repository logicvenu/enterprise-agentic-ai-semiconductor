# 16 — Air-Gapped Architecture

**Project:** Semiconductor Enterprise AI Platform
**Architecture Pattern:** Pattern 2 — Hybrid AI Platform
**Artifact:** 16 of 22
**Status:** DRAFT FOR REVIEW

## Purpose

Define how the Semiconductor Enterprise AI Platform operates when sensitive semiconductor IP, engineering data, models, tools, or AI workloads must remain inside a private or isolated environment.

> **How can enterprise AI operate close to sensitive EDA/IP workloads while preserving strong isolation, controlled software/model supply chains, and governed operational access?**

## 1. Core Principle

Air-gapping is a **deployment/security property**, not a separate AI architecture.

The logical platform remains:

```text
Experience
    ↓
AI Applications / Agents
    ↓
AI Platform Abstraction
    ↓
Models / Knowledge / Tools
    ↓
AI Infrastructure
```

The difference is the trust boundary and connectivity model.

## 2. Private vs Air-Gapped vs Hybrid

| Model | Connectivity | Typical Use |
|---|---|---|
| Cloud | Internet/private-cloud connectivity | General enterprise AI |
| Private | Organization-controlled network | Sensitive workloads |
| Hybrid | Cloud + private environments | Mixed workload placement |
| Air-gapped | No direct external network path | Highest-sensitivity workloads |

An air-gapped environment can communicate with approved internal systems; the protected environment has no unauthorized external network path.

## 3. Air-Gap Boundary

```text
External / Public Environment
              X
              │
       NO DIRECT PATH
              │
              ▼
┌─────────────────────────────────────┐
│        AIR-GAPPED AI ZONE           │
│ Models | RAG | Agents | MCP | EDA   │
│ Data   | GPU  | Storage | Security  │
└─────────────────────────────────────┘
```

Any transfer across the boundary occurs only through an explicitly controlled mechanism.

## 4. Trust Zones

```text
Zone 0 — External / Untrusted
Zone 1 — Controlled Transfer
Zone 2 — Enterprise Private
Zone 3 — Sensitive AI
Zone 4 — EDA / Crown-Jewel IP
```

Higher zones require stronger controls.

## 5. 16-A — Air-Gapped Architecture Landscape

```text
                    Enterprise AI Platform
                             |
               +-------------+-------------+
               |                           |
           Cloud Zone                 Private Zone
               |                           |
       General AI Workloads       Sensitive AI Workloads
                                           |
                                    +------+------+
                                    |             |
                               AI Platform       EDA
                                    |             |
                                    +------+------+
                                           |
                                    Crown-Jewel IP
```

The platform remains logically consistent while deployment location varies by data and workload sensitivity.

## 6. Private AI Platform

The private platform can host:

- AI Experience
- AI Applications
- Model Gateway
- Knowledge Gateway
- Agent Runtime
- Tool / EDA Gateway
- MCP integration
- Model serving
- Evaluation
- Governance
- Observability

The same abstraction interfaces should be retained across cloud and private deployments.

## 7. 16-B — Private AI Platform

```text
                  Private AI Environment
                           |
        +------------------+------------------+
        |                  |                  |
     Platform            AI Compute          Data
        |                  |                  |
 Model Gateway          GPU / CPU        Knowledge
 Agent Runtime          Inference        Artifacts
 MCP / Tools            Evaluation       Engineering Data
        |                  |                  |
        +------------------+------------------+
                           |
                         EDA
```

The private environment is another deployment topology of the same enterprise platform.

## 8. Air-Gapped AI Runtime

The isolated runtime should contain all dependencies necessary for approved operation:

```text
Application Runtime
Agent Runtime
Model Runtime
Knowledge Runtime
MCP Runtime
Policy / Identity
Observability
Artifact / Model Storage
```

The objective is operational independence from external runtime dependencies.

## 9. 16-C — Air-Gapped AI Runtime

```text
                 AIR-GAPPED AI ZONE
                        |
       +----------------+----------------+
       |                |                |
   Control Plane     AI Compute       Data Plane
       |                |                |
   Identity          GPU / CPU       Knowledge
   Policy            Inference       Models
   Config            Evaluation      Artifacts
       |                |                |
       +----------------+----------------+
                        |
                  Tool / EDA Gateway
                        |
                       MCP
                        |
                       EDA
```

## 10. Data Residency

Sensitive information may include RTL, verification environments, design specifications, netlists, simulation results, waveforms, coverage, regression logs, physical-design data, DFT data, customer/product information, and engineering documents.

The architecture supports data remaining entirely within the protected zone.

## 11. 16-D — Secure Data / Knowledge Flow

```text
Engineering Data
       ↓
Classification
       ↓
Private Ingestion
       ↓
Private Knowledge Store
       ↓
Access Control
       ↓
Private Retrieval
       ↓
Private Model
       ↓
Private Response
```

No external retrieval dependency is required for sensitive workflows.

## 12. Knowledge Isolation

```text
Sensitive Source
      ↓
Private Ingestion
      ↓
Private Index / Knowledge Store
      ↓
Access Control
      ↓
Retrieval
      ↓
Context
      ↓
Private Inference
```

Authorization must be enforced before sensitive context reaches the model.

## 13. Model Placement

Sensitive models may be self-hosted or privately deployed.

Applications continue using:

```text
Application
    ↓
Model Gateway
    ↓
Approved Model
```

rather than binding directly to a model runtime.

## 14. 16-E — Model Supply Chain

```text
Approved External Source
          ↓
Controlled Transfer Zone
          ↓
Security / Integrity Validation
          ↓
Artifact Scan
          ↓
Model Evaluation
          ↓
Approval
          ↓
Secure Transfer
          ↓
Air-Gapped Model Repository
          ↓
Deployment
```

The isolated environment does not require unrestricted access to public model repositories.

## 15. Model Integrity

Model artifacts should carry:

- Version
- Provenance
- Checksum / digest
- Source
- License metadata
- Security scan result
- Evaluation result
- Approval status
- Deployment status

Only approved artifacts enter the protected runtime.

## 16. Software Supply Chain

The same process applies to container images, OS packages, libraries, AI frameworks, MCP servers, EDA adapters, configuration, and infrastructure definitions.

```text
Build / Acquire
      ↓
Scan
      ↓
Test
      ↓
Sign
      ↓
Approve
      ↓
Transfer
      ↓
Verify
      ↓
Deploy
```

## 17. 16-F — Controlled Ingress / Egress

```text
                 External Environment
                         |
                   Controlled Gate
                         |
                +--------+--------+
                |                 |
             INGRESS            EGRESS
                |                 |
        Approved Artifacts    Approved Results
                |                 |
                +--------+--------+
                         |
                 Air-Gap Boundary
                         |
                  Protected Zone
```

Both ingress and egress are explicit and policy-controlled.

## 18. Ingress Controls

Potential controls:

- Approved transfer mechanism
- Artifact allow-list
- Malware scanning
- Integrity verification
- Digital signatures
- Provenance validation
- License review
- Security approval
- Change ticket
- Transfer audit

No arbitrary files should cross the boundary.

## 19. Egress Controls

Potential outputs:

- Approved reports
- Aggregated metrics
- Operational alerts
- Sanitized engineering results
- Approved artifacts

Sensitive IP should not leave merely because an agent generated a response.

## 20. Output Classification

```text
Result
  ↓
Classification
  ↓
Sensitive Content Detection
  ↓
Policy
  ↓
Approval if Required
  ↓
Sanitized / Approved Output
  ↓
Egress
```

This prevents the AI platform from becoming an accidental IP exfiltration path.

## 21. EDA Integration in Air-Gapped Zone

```text
Agent
 ↓
Agent Runtime
 ↓
Tool / EDA Gateway
 ↓
MCP
 ↓
EDA Adapter
 ↓
EDA Tool
 ↓
Engineering Data
```

No agent requires public-network access to invoke an EDA workflow.

## 22. 16-G — EDA + AI Integration

```text
                Air-Gapped AI Zone
                       |
                 Agent Runtime
                       |
                Tool / EDA Gateway
                       |
                      MCP
                       |
              Private EDA Adapter
                       |
        +--------------+--------------+
        |              |              |
       RTL          Simulation      Regression
        |              |              |
        +--------------+--------------+
                       |
                  EDA Data / IP
```

## 23. Air-Gapped Agent Architecture

```text
Engineer
   ↓
Private AI Experience
   ↓
Agent Runtime
   ↓
Private Model Gateway
   ↓
Private Knowledge Gateway
   ↓
Private Tool / EDA Gateway
   ↓
MCP
   ↓
EDA
```

## 24. 16-H — Air-Gapped Agent / MCP

```text
                 PRIVATE AI ZONE
                       |
                 Agent Runtime
                       |
                Model Gateway
                       |
              Knowledge Gateway
                       |
              Tool / EDA Gateway
                       |
                      MCP
                       |
                 Private EDA
```

## 25. Agent Restrictions

Air-gapped agents should have:

- Explicit tool allow-lists
- Restricted network access
- No unrestricted internet tools
- No arbitrary code execution
- Bounded execution
- Data classification awareness
- Controlled model access
- Audited tool invocation

## 26. Model Update Process

```text
Candidate Model
      ↓
External Evaluation
      ↓
Security / License Review
      ↓
Artifact Packaging
      ↓
Integrity Validation
      ↓
Controlled Transfer
      ↓
Private Evaluation
      ↓
Engineering Acceptance
      ↓
Production Approval
      ↓
Deployment
```

Private evaluation is important because model behavior must be assessed against actual engineering workflows.

## 27. 16-I — Software / Model Update Process

```text
Acquire
  ↓
Scan
  ↓
Evaluate
  ↓
Approve
  ↓
Package
  ↓
Controlled Transfer
  ↓
Verify
  ↓
Private Test
  ↓
Release
  ↓
Deploy
  ↓
Monitor
```

## 28. Operational Access

Administrative access should be:

- Authenticated
- Authorized
- Time-bound
- Audited
- Least-privilege
- Approved where required

## 29. 16-J — Break-Glass / Operational Access

```text
Operational Need
       ↓
Access Request
       ↓
Approval
       ↓
Time-Bound Privilege
       ↓
Controlled Access
       ↓
Activity Logging
       ↓
Privilege Revocation
       ↓
Review
```

Break-glass access is an exception mechanism, not a normal operating model.

## 30. Identity Architecture

```text
Human Identity
      ↓
Service Identity
      ↓
Agent Identity
      ↓
Tool / EDA Identity
```

Every action remains attributable.

## 31. Secrets

Secrets remain inside the protected environment:

- EDA credentials
- Service credentials
- Certificates
- API keys
- Signing keys
- Database credentials

Agents and model context must never become a secrets store.

## 32. Network Isolation

```text
Network Segmentation
        +
Egress Restrictions
        +
Ingress Controls
        +
Private Service Connectivity
        +
Service Identity
```

Exact network technology remains an implementation decision.

## 33. Availability

Air-gapped environments cannot assume an external service will be available when an internal dependency fails.

Critical services therefore require appropriate:

- Redundant compute
- Local model availability
- Local knowledge services
- Local identity dependencies
- Local observability
- Local artifact repositories
- Backup/recovery

## 34. 16-K — Hybrid ↔ Air-Gapped Boundary

```text
                         HYBRID PLATFORM
                                |
          +---------------------+---------------------+
          |                                           |
       CLOUD ZONE                               PRIVATE ZONE
          |                                           |
   General AI Workloads                       Sensitive AI
   Elastic Compute                            Private Models
   General Services                           Private RAG
                                               Agent Runtime
                                               MCP / EDA
                                                   |
                                                   ↓
                                              AIR-GAPPED
                                                ZONE
```

The same logical platform abstractions span environments while deployment and security boundaries remain explicit.

## 35. Workload Placement

Placement follows:

```text
Data Sensitivity
       +
EDA Dependency
       +
Security Policy
       +
Latency
       +
Compute
       +
Cost
       +
Availability
```

| Workload | Candidate Placement |
|---|---|
| Generic enterprise assistant | Cloud |
| Non-sensitive engineering knowledge | Cloud / Hybrid |
| Sensitive IP RAG | Private |
| Sensitive self-hosted inference | Private |
| EDA execution | Private / Air-Gapped |
| Highly sensitive customer design | Air-Gapped |
| Model evaluation | Cloud / Private |
| Production EDA agent | Private / Air-Gapped |

These are placement principles, not final deployment decisions.

## 36. Air-Gapped Observability

Observability must operate locally.

Collect:

- Infrastructure metrics
- GPU metrics
- Inference metrics
- Agent telemetry
- MCP/tool telemetry
- Audit events
- Security events
- EDA job status
- Cost/usage metrics

External observability dependency should not be required for core operations.

## 37. Air-Gapped Logging

```text
Application
    ↓
Structured Logging
    ↓
Classification
    ↓
Private Log Storage
    ↓
Access Control
    ↓
Retention
```

Log forwarding outside the zone requires explicit policy.

## 38. Disaster Recovery

The isolated environment needs independent recovery capabilities for:

- Infrastructure definitions
- Models
- Knowledge metadata
- Critical data
- Agent state
- Configuration
- Security policies
- Audit records

Recovery procedures must be tested without assuming external network access.

## 39. Air-Gapped Failure Scenario

```text
External Connectivity Unavailable
          ↓
Air-Gapped Platform
          ↓
Can it still:
  - Authenticate?
  - Retrieve knowledge?
  - Run models?
  - Execute EDA tools?
  - Monitor itself?
  - Audit actions?
  - Recover?
```

For critical isolated workloads, the answer should be **yes**.

## 40. Security Trust Model

```text
LOWER TRUST
     ↓
External
     ↓
Controlled Transfer
     ↓
Private Platform
     ↓
Sensitive AI
     ↓
EDA / Crown-Jewel IP
HIGHER TRUST
```

Security controls become stronger toward protected assets.

## 41. Crown-Jewel Principle

Highest-value semiconductor assets should have the strongest isolation.

Examples:

- Source RTL
- Proprietary design IP
- Customer-specific designs
- High-value verification assets
- Proprietary physical-design data
- Security-sensitive design information

The architecture should avoid creating a broad AI data path to these assets.

## 42. Architectural Decisions

- **AD-16-01:** Air-gap is treated as a deployment/security property, not a separate AI architecture.
- **AD-16-02:** Private deployments reuse the same logical platform architecture.
- **AD-16-03:** Critical isolated workflows have no uncontrolled external runtime dependency.
- **AD-16-04:** Models and software enter through a controlled supply chain.
- **AD-16-05:** Transferred artifacts require provenance and integrity validation.
- **AD-16-06:** Egress is classified and governed.
- **AD-16-07:** Critical model, knowledge, identity, observability and artifact services are locally available.
- **AD-16-08:** EDA and crown-jewel IP remain inside the protected boundary.
- **AD-16-09:** Operational access is least-privilege, time-bound and auditable.
- **AD-16-10:** Cloud and private deployments retain the same logical platform interfaces wherever practical.
- **AD-16-11:** Agents cannot bypass the Tool / EDA Gateway and MCP integration.

## 43. Trade-offs

### Air-Gapped vs Connected Private
Air-gapping provides stronger isolation but increases operational complexity.

### Local vs External Models
Local models improve IP protection and operational independence; external models may offer greater model choice but introduce transfer and dependency concerns.

### Centralized vs Local Knowledge
Centralized knowledge simplifies management; local knowledge is preferable for highly sensitive IP.

### Convenience vs Security
Automated updates and external services improve convenience; controlled transfer provides stronger security at additional operational cost.

## 44. What Artifact 16 Does Not Decide

Still deferred:

- Exact air-gap network implementation
- Exact AWS services
- Exact private-cloud technology
- GPU model
- Kubernetes distribution
- Artifact-transfer product
- Malware scanning product
- Identity provider
- Secrets-management product
- Model registry product
- Container registry
- Exact DLP implementation
- Exact EDA vendor integration
- RPO/RTO values

These choices will be selected only where justified by requirements and implementation constraints.

## 45. Traceability

```text
04 NFRs
    ↓
15 AI Infrastructure
    ↓
16 Air-Gapped Architecture
    ↓
17 CI/CD / MLOps / LLMOps / AgentOps
    ↓
18 Governance & Security
    ↓
19 Observability
```

Artifact 16 extends Artifact 15 from:

> **Where can infrastructure run?**

to:

> **How can sensitive AI and EDA workloads operate safely when external connectivity is restricted or completely unavailable?**

## 46. Acceptance Criteria

- [ ] Private, hybrid and air-gapped models distinguished.
- [ ] Air-gap boundary defined.
- [ ] Trust zones defined.
- [ ] Private AI platform defined.
- [ ] Air-gapped runtime defined.
- [ ] Data residency defined.
- [ ] Knowledge isolation defined.
- [ ] Model placement defined.
- [ ] Model supply chain defined.
- [ ] Model integrity requirements defined.
- [ ] Software supply chain defined.
- [ ] Controlled ingress defined.
- [ ] Controlled egress defined.
- [ ] Output classification defined.
- [ ] Private EDA integration defined.
- [ ] Air-gapped agent/MCP architecture defined.
- [ ] Agent restrictions defined.
- [ ] Model/software update process defined.
- [ ] Break-glass access defined.
- [ ] Identity architecture defined.
- [ ] Secrets isolation defined.
- [ ] Network isolation defined.
- [ ] Local availability requirements defined.
- [ ] Hybrid/air-gapped boundary defined.
- [ ] Workload placement criteria defined.
- [ ] Local observability defined.
- [ ] Local logging defined.
- [ ] Disaster recovery considerations defined.
- [ ] Failure scenario considered.
- [ ] Crown-jewel IP principle defined.
- [ ] Architectural decisions recorded.
- [ ] Trade-offs documented.
- [ ] No premature technology selection introduced.

# Status

**16 — Air-Gapped Architecture — DRAFT FOR REVIEW**

Next:

> **17 — CI/CD / MLOps / LLMOps / AgentOps**
