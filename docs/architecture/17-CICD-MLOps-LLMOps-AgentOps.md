# 17 — CI/CD / MLOps / LLMOps / AgentOps

**Project:** Semiconductor Enterprise AI Platform
**Architecture Pattern:** Pattern 2 — Hybrid AI Platform
**Artifact:** 17 of 22
**Status:** DRAFT FOR REVIEW

## Purpose

Artifact 17 defines the operating model and lifecycle architecture for continuously building, validating, releasing, deploying, operating and improving the Semiconductor Enterprise AI Platform.

> **How do we safely move platform code, models, knowledge pipelines, prompts, agents, MCP tools and infrastructure from development into production across cloud, private and air-gapped environments?**

## 1. Core Principle

MLOps, LLMOps and AgentOps are complementary operating disciplines around one Enterprise AI Platform.

```text
Software / Infrastructure
          ↓
         CI/CD
          ↓
 ┌────────┼─────────┐
 ↓        ↓         ↓
MLOps   LLMOps   AgentOps
 ↓        ↓         ↓
Models   LLM/RAG  Agents/Tools
          ↓
     Production
          ↓
 Observability / Feedback
          ↓
 Continuous Improvement
```

## 2. Lifecycle Principle

```text
Define → Build → Validate → Evaluate → Approve → Release → Deploy → Observe → Improve
```

The same principle applies to platform software, infrastructure, models, knowledge pipelines, prompts, agents and MCP tools.

## 3. Operating Model

**Platform Engineering:** shared platform, infrastructure, runtime, security integration, developer experience, reliability.

**AI/ML Engineering:** models, model evaluation, ML pipelines, model deployment.

**GenAI/LLM Engineering:** RAG, prompt/context engineering, LLM evaluation, inference configuration.

**Agent Engineering:** agent workflows, tool orchestration, agent evaluation, agent policies.

**Domain Engineering:** semiconductor workflow requirements, engineering validation, domain acceptance, business outcomes.

**Security/Governance:** policy, risk, compliance, approval controls, audit requirements.

The model is collaborative rather than fully centralized.

## 4. 17-A — AI Engineering Lifecycle

```text
Business / Engineering Need
          ↓
Architecture / Requirements
          ↓
Design → Build → Test → Evaluate
          ↓
Security / Governance
          ↓
Release → Deploy → Operate
          ↓
Measure → Improve
```

The lifecycle connects engineering work to business outcomes.

## 5. Source of Truth

Production changes should be traceable to version-controlled artifacts:

- Application code
- Infrastructure definitions
- Model metadata
- Evaluation datasets/configuration
- Prompts
- Agent definitions
- Tool definitions
- Policies
- Deployment configurations

A production deployment should be reproducible from approved versioned artifacts.

## 6. 17-B — CI/CD Platform Pipeline

```text
Developer
    ↓
Source Control
    ↓
Build
    ↓
Unit / Integration Tests
    ↓
Security / Quality Gates
    ↓
Artifact
    ↓
Environment Promotion
    ↓
Deployment
    ↓
Smoke / Health Tests
    ↓
Production
```

CI/CD is the foundation on which MLOps, LLMOps and AgentOps operate.

## 7. Continuous Integration

CI validates:

- Code quality
- Unit/integration tests
- Dependency checks
- Security scanning
- Container/image validation
- Configuration validation
- Infrastructure validation

AI-specific validation is added later in the pipeline.

## 8. Continuous Delivery / Deployment

```text
Development → Test → Staging → Production
```

Production promotion requires appropriate evidence and approvals.

Deployment strategy can later be rolling, blue/green, canary or shadow without locking the architecture to one approach.

## 9. 17-C — MLOps Lifecycle

```text
Data
 ↓
Preparation
 ↓
Training / Adaptation
 ↓
Evaluation
 ↓
Model Registration
 ↓
Approval
 ↓
Deployment
 ↓
Monitoring
 ↓
Drift / Performance
 ↓
Retraining / Replacement
```

MLOps governs conventional ML and model-adaptation workloads.

## 10. MLOps Evaluation

Evaluate:

- Accuracy
- Precision / recall
- Domain-specific task performance
- Robustness
- Bias/fairness where applicable
- Resource efficiency
- Model latency
- Cost

Semiconductor evaluation should use actual engineering tasks, not only generic benchmarks.

## 11. 17-D — LLMOps Lifecycle

```text
Foundation Model
       ↓
Model Selection
       ↓
Prompt / Context Design
       ↓
RAG Integration
       ↓
Evaluation
       ↓
Safety / Security
       ↓
Inference Configuration
       ↓
Release
       ↓
Production
       ↓
Observability
       ↓
Continuous Evaluation
```

## 12. LLM Evaluation

### Model quality
- Task accuracy
- Task success
- Relevance

### RAG quality
- Retrieval recall
- Context relevance
- Groundedness
- Citation/attribution quality

### Runtime
- TTFT
- Latency
- Tokens/sec
- Throughput
- Error rate

### Economics
- Tokens/request
- Cost/request
- Cost/workflow

## 13. 17-E — RAG / KnowledgeOps Lifecycle

```text
Source
 ↓
Ingest
 ↓
Parse
 ↓
Classify
 ↓
Chunk / Transform
 ↓
Index
 ↓
Evaluate Retrieval
 ↓
Publish
 ↓
Monitor
 ↓
Refresh / Re-index
```

Knowledge is continuously operated, not a one-time data load.

## 14. Knowledge Evaluation Gates

```text
Source Validation
      ↓
Parsing Validation
      ↓
Metadata Validation
      ↓
Access-Control Validation
      ↓
Retrieval Evaluation
      ↓
Grounding Evaluation
      ↓
Publish
```

A knowledge update can be rejected without changing the model.

## 15. 17-F — AgentOps Lifecycle

```text
Workflow Design
      ↓
Agent Build
      ↓
Tool Definition
      ↓
Unit / Scenario Tests
      ↓
Agent Evaluation
      ↓
Safety / Policy Validation
      ↓
Approval
      ↓
Deployment
      ↓
Runtime Monitoring
      ↓
Feedback
      ↓
Improvement
```

AgentOps extends operational control from the model to the complete agentic workflow.

## 16. Agent Evaluation

Evaluate the complete workflow:

- Task success
- Tool selection accuracy
- Tool execution success
- Planning quality
- Handoff success
- Groundedness
- Policy violations
- Human intervention rate
- Number of steps
- Execution latency
- Cost/workflow

## 17. Agent Safety Gates

```text
Agent Definition
      ↓
Tool Allow-List
      ↓
Permission Validation
      ↓
Prompt / Policy Tests
      ↓
Scenario Tests
      ↓
Adversarial Tests
      ↓
Human Review
      ↓
Production Approval
```

High-impact engineering actions require stronger gates.

## 18. 17-G — MCP / Tool Lifecycle

```text
Tool Design
    ↓
Implementation
    ↓
Schema Validation
    ↓
Security Review
    ↓
Functional Testing
    ↓
Authorization Testing
    ↓
Agent Integration Testing
    ↓
Approval
    ↓
Production
    ↓
Monitoring
    ↓
Version / Retire
```

MCP tools are governed platform assets.

## 19. Tool Risk Classification

```text
READ → ANALYZE → RECOMMEND → CREATE / UPDATE → EXECUTE → HIGH-IMPACT ACTION
```

As impact increases, authorization, evaluation, human approval and audit requirements may increase.

## 20. 17-H — Model Promotion Pipeline

```text
Candidate Model
      ↓
Security / Provenance
      ↓
Benchmark
      ↓
Domain Evaluation
      ↓
Performance Evaluation
      ↓
Cost Evaluation
      ↓
Approval
      ↓
Staging
      ↓
Production
      ↓
Monitor
```

Model promotion is evidence-driven.

## 21. Model Rollback

```text
Production Model
      ↓
New Model
      ↓
Validation
      ↓
Release
      ↓
Problem Detected
      ↓
Rollback
      ↓
Previous Approved Model
```

Rollback restores the known-good model configuration, not merely model weights.

## 22. 17-I — Agent Promotion Pipeline

```text
Agent Candidate
      ↓
Scenario Tests
      ↓
Tool Tests
      ↓
Security / Policy
      ↓
Evaluation
      ↓
Human Review
      ↓
Staging
      ↓
Production
      ↓
Observe
```

Promote the complete agent configuration: agent definition, prompts, model configuration, tool bindings, policies, workflow configuration and evaluation version.

## 23. Hybrid Deployment Pipeline

```text
                         Release
                            ↓
                    Policy / Classification
                            ↓
              ┌─────────────┴─────────────┐
              ↓                           ↓
          Cloud Path                 Private Path
              ↓                           ↓
       Cloud Deployment             Private Deployment
                                          ↓
                                    Air-Gapped Path
                                          ↓
                                   Controlled Transfer
                                          ↓
                                    Local Validation
                                          ↓
                                      Deployment
```

## 24. 17-J — Hybrid / Air-Gapped CI/CD

```text
Source / Build
      ↓
Artifact Package
      ↓
Security / Signing
      ↓
Classification
      ↓
   ┌──┴──────────┐
   ↓             ↓
Cloud          Transfer
   ↓             ↓
Deploy      Air-Gapped Validation
                 ↓
               Deploy
```

Air-gapped deployment adds a controlled promotion boundary.

## 25. Air-Gapped Reproducibility

The isolated environment should retain sufficient local artifacts to reproduce approved deployments:

- Source artifacts
- Container images
- Model artifacts
- Configuration
- Infrastructure definitions
- Dependencies
- Evaluation packages
- Security metadata

## 26. 17-K — Evaluation Gates

```text
Build
 ↓
Technical Tests
 ↓
AI Evaluation
 ↓
Security
 ↓
Domain Validation
 ↓
Operational Validation
 ↓
Approval
 ↓
Production
```

## 27. Evaluation Matrix

| Artifact | Technical | AI Quality | Security | Domain | Operational |
|---|---:|---:|---:|---:|---:|
| Platform Code | ✓ | — | ✓ | ✓ | ✓ |
| Model | ✓ | ✓ | ✓ | ✓ | ✓ |
| RAG | ✓ | ✓ | ✓ | ✓ | ✓ |
| Agent | ✓ | ✓ | ✓ | ✓ | ✓ |
| MCP Tool | ✓ | ✓ | ✓ | ✓ | ✓ |
| Infrastructure | ✓ | — | ✓ | ✓ | ✓ |

## 28. Release Approval

A release package may contain:

- Version
- Test results
- Evaluation results
- Security results
- Domain validation
- Performance results
- Cost estimate
- Risk classification
- Rollback version
- Approval record

## 29. 17-L — Production Release / Rollback

```text
Approved Release
      ↓
Staging Validation
      ↓
Production Deployment
      ↓
Health Check
      ↓
Observe
      ↓
Healthy?
  ┌───┴───┐
 Yes      No
  ↓        ↓
Continue  Rollback
           ↓
       Known-Good
```

## 30. Progressive Delivery

```text
New Version
    ↓
Shadow
    ↓
Small Traffic
    ↓
Evaluate
    ↓
Increase Traffic
    ↓
Full Production
```

Useful for new models, prompts, RAG configurations, agents and inference runtimes.

## 31. 17-M — Continuous Feedback Loop

```text
Production
    ↓
Observability
    ↓
User Feedback
    ↓
Engineering Outcomes
    ↓
Evaluation
    ↓
Improvement
    ↓
New Version
    ↓
Release
    ↓
Production
```

## 32. Production Feedback Sources

- User ratings
- Engineer corrections
- Failed tasks
- Tool failures
- Retrieval failures
- Hallucination reports
- Policy violations
- Performance degradation
- Cost increases
- Regression results
- Business KPI changes

## 33. Incident → Improvement

```text
Regression Agent
      ↓
Incorrect Diagnosis
      ↓
Incident
      ↓
Root Cause
      ↓
Evaluation Case Added
      ↓
Agent / RAG Improvement
      ↓
Regression Test
      ↓
New Release
```

Production incidents become reusable evaluation assets.

## 34. Platform vs AI Lifecycle

### Platform lifecycle
```text
Infrastructure → Platform Services → Runtime → Deployment → Operations
```

### AI capability lifecycle
```text
Model / Knowledge / Agent / Tool → Evaluation → Release → Runtime → Feedback
```

They remain integrated but independently evolvable.

## 35. Versioning

Version independently where appropriate:

- Application
- Infrastructure
- Model
- Prompt
- RAG configuration
- Knowledge dataset/index
- Agent
- Tool/MCP server
- Policy
- Evaluation dataset
- Evaluation configuration

A production result should be traceable to the versions that produced it.

## 36. Reproducibility

```text
Application Version
+
Model Version
+
Prompt Version
+
Knowledge Version
+
Agent Version
+
Tool Version
+
Policy Version
+
Infrastructure Version
```

This is essential for debugging and audit.

## 37. Environment Promotion

```text
DEV → TEST → STAGING → PRODUCTION
```

Promotion should preserve artifact identity.

## 38. Separation of Duties

A possible model:

```text
Builder
   ↓
Evaluator
   ↓
Security / Governance
   ↓
Domain Owner
   ↓
Release Approval
```

Exact organizational implementation depends on company policy.

## 39. Governance Integration

Governance is embedded throughout:

```text
Design → Build → Evaluate → Security → Approve → Deploy → Monitor → Re-evaluate
```

Risk level determines control depth.

## 40. Risk-Based Lifecycle

```text
Low Risk
   ↓
Standard Gates

Medium Risk
   ↓
Additional Evaluation / Approval

High Risk
   ↓
Strong Security + Domain Review
+ Human Approval + Controlled Deployment
```

EDA write/execute workflows generally require stronger controls than read-only knowledge workflows.

## 41. Metrics

### Delivery
- Lead time for change
- Deployment frequency
- Change failure rate
- Mean time to recovery

### AI
- Evaluation pass rate
- Task success
- Groundedness
- Human intervention

### Runtime
- Latency
- TTFT
- TPS
- Availability
- Error rate

### Agent
- Tool success
- Workflow success
- Policy violations
- Cost/workflow

### Business
- Engineer-hours saved
- Cycle-time reduction
- Regression triage time
- Time-to-answer
- Time-to-silicon

## 42. Architectural Decisions

- **AD-17-01:** Unified lifecycle — MLOps, LLMOps and AgentOps are complementary disciplines.
- **AD-17-02:** CI/CD is the delivery foundation.
- **AD-17-03:** Models, RAG, agents and tools receive artifact-specific evaluation.
- **AD-17-04:** Production promotion is evidence-based.
- **AD-17-05:** Version-controlled artifacts are the source of truth.
- **AD-17-06:** Production workflows must be reproducible.
- **AD-17-07:** Higher-impact capabilities receive stronger gates.
- **AD-17-08:** Progressive delivery is supported where practical.
- **AD-17-09:** Production AI changes require rollback paths.
- **AD-17-10:** Air-gapped deployment uses controlled transfer and local validation.
- **AD-17-11:** Production feedback becomes evaluation input.
- **AD-17-12:** Production approval has appropriate separation of duties.

## 43. Trade-offs

### Centralized vs Federated Operations
Central standards improve consistency while domain teams own workflow-specific innovation.

### Speed vs Control
Risk-based controls avoid applying maximum friction to every change.

### Continuous Deployment vs Controlled Release
Lower-risk changes can move faster; sensitive models, agents and EDA actions may require controlled promotion.

### Cloud vs Air-Gapped Delivery
Cloud enables automation and elasticity; air-gapped delivery requires additional packaging, transfer and local validation.

## 44. What Artifact 17 Does Not Decide

Still deferred:

- Exact CI/CD product
- Exact source-control platform
- Exact artifact registry
- Exact model registry
- Exact evaluation framework
- Exact experiment tracking tool
- Exact orchestration platform
- Exact deployment strategy
- Exact GitOps implementation
- Exact air-gap transfer technology
- Exact observability technology

## 45. Traceability

```text
15 AI Infrastructure
        ↓
16 Air-Gapped Architecture
        ↓
17 CI/CD / MLOps / LLMOps / AgentOps
        ↓
18 Governance & Security
        ↓
19 Observability
        ↓
20 Execution Roadmap
        ↓
21 Business KPIs
        ↓
22 Executive Narrative
```

Artifact 17 connects architecture to operational execution.

## 46. Acceptance Criteria

- [ ] Unified AI engineering lifecycle defined.
- [ ] CI/CD foundation defined.
- [ ] MLOps lifecycle defined.
- [ ] LLMOps lifecycle defined.
- [ ] RAG/KnowledgeOps lifecycle defined.
- [ ] AgentOps lifecycle defined.
- [ ] MCP/tool lifecycle defined.
- [ ] Model promotion defined.
- [ ] Agent promotion defined.
- [ ] Hybrid deployment lifecycle defined.
- [ ] Air-gapped promotion defined.
- [ ] Evaluation gates defined.
- [ ] Release/rollback defined.
- [ ] Progressive delivery defined.
- [ ] Continuous feedback defined.
- [ ] Versioning defined.
- [ ] Reproducibility defined.
- [ ] Environment promotion defined.
- [ ] Separation of duties defined.
- [ ] Governance integration defined.
- [ ] Risk-based lifecycle defined.
- [ ] Operating metrics defined.
- [ ] Architectural decisions recorded.
- [ ] Trade-offs documented.
- [ ] Technology selection deferred until justified.

# Status

**17 — CI/CD / MLOps / LLMOps / AgentOps — DRAFT FOR REVIEW**

Next:

> **18 — Governance & Security**
