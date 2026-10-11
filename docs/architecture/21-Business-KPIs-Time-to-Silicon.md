# 21 — Business KPIs / Time-to-Silicon

**Project:** Semiconductor Enterprise AI Platform
**Pattern:** Pattern 2 — Hybrid AI Platform
**Artifact:** 21 of 22
**Status:** DRAFT FOR REVIEW

## Purpose
Establish how the Enterprise AI Platform measures business value.

> **AI metrics tell us whether AI is working. Engineering metrics tell us whether the workflow is improving. Business metrics tell us whether the company is benefiting.**

Strategic KPI: **Time-to-Silicon**.

No arbitrary improvement percentages are assumed. Establish **baseline → target → measurement → attribution → business impact**.

## 1. Business Value Chain
```text
AI Platform → AI Capability → Engineering Workflow → Engineer Productivity
→ Cycle-Time Reduction → Faster Design / Verification → Reduced Time-to-Silicon
→ Earlier Customer Delivery → Business Growth
```

## 2. 21-A — Business KPI Framework
```text
Enterprise AI Platform
        │
 ┌──────┼────────┐
 ↓      ↓        ↓
AI KPIs  Engineering  Business
         KPIs         KPIs
 ↓      ↓        ↓
Quality Productivity Time-to-Silicon
Cost    Cycle Time   Delivery
Latency Debug/Triage Business Value
 └──────┼────────┘
        ↓
Executive Scorecard
```

## 3. KPI Hierarchy
**Level 1 — Platform:** availability, latency, throughput, GPU/capacity.
**Level 2 — AI:** task success, TTFT, TPS, retrieval quality, groundedness, tool/agent success.
**Level 3 — Engineering:** cycle time, time-to-answer, triage/debug/documentation time, engineer-hours.
**Level 4 — Business:** design-cycle acceleration, delivery predictability, time-to-silicon, customer delivery.

## 4. 21-B — Engineering Productivity KPIs
Measure engineer-hours/task, manual steps, tasks/engineer, search/triage/debug/documentation effort and rework.

```text
Current Workflow → Engineer Effort → AI-Assisted Workflow
→ Measured Effort → Validated Improvement
```

AI usage is not itself productivity improvement.

## 5. 21-C — Workflow / Cycle-Time KPIs
Regression: failure-to-triage, root-cause and resolution time.
Design: specification-to-design and review cycle time.
Verification: failure analysis, debug and regression closure time.
Documentation: drafting, review and update turnaround.

Measure the complete workflow, not only model latency.

## 6. 21-D — AI Quality KPIs
Task success, accuracy, groundedness, retrieval relevance, citation/provenance quality, tool success, agent success, human intervention, rework and defect escape.

> A faster system producing incorrect engineering recommendations is not productivity improvement.

## 7. 21-E — Adoption KPIs
Active engineers, workflow adoption, repeat usage, tasks assisted/completed, feature adoption, abandonment, human override and acceptance.

```text
Eligible → Exposed → Activated → First Success → Repeat Usage
→ Workflow Adoption → Sustained Usage
```

## 8. 21-F — Platform / Infrastructure KPIs
Availability, latency, TTFT, TPS, throughput, queue time, GPU utilization/memory, capacity, idle time, errors, timeouts, recovery and deployment reliability.

## 9. GPU Economics
```text
GPU Capacity → Allocated Capacity → Actual Utilization
→ Useful AI Work → Cost / Useful Work
```
High GPU utilization alone does not prove economic efficiency.

## 10. 21-G — AI Economics
Track cost/request, token, workflow, engineer task, GPU and infrastructure; analyze by model, team, application, workflow, environment and business unit.

```text
Infrastructure → Inference → AI Capability → Workflow
→ Engineering Task → Business Value
```

## 11. 21-H — Engineering Quality
Track defect rate, rework, regression quality, escaped defects, review findings, verification coverage where applicable, false recommendations, incorrect tool actions and human override.

```text
Productivity + Quality = Sustainable Gain
```

## 12. 21-I — Time-to-Silicon
Time-to-silicon is a strategic outcome, not a single AI metric.

```text
Architecture → RTL → Verification → Physical Design → DFT
→ Signoff → Tapeout → Fabrication → Silicon Validation
```

AI contribution should be measured through the upstream workflows it actually improves.

## 13. Time-to-Silicon Decomposition
```text
Total Time-to-Silicon
       │
 ┌─────┼────────────────┐
 ↓     ↓                ↓
Design Verification Physical / Signoff
 ↓     ↓                ↓
Cycle  Debug/Regression Iteration/Closure
Time
```

## 14. 21-J — KPI Attribution
```text
Business KPI
      ↑
Engineering Outcome
      ↑
Workflow
      ↑
AI Capability
      ↑
Model / Agent / RAG
      ↑
Platform
```
Capture workflow, baseline period, team, capability/version, model/agent/RAG/tool versions, environment, outcome and confounding factors.

## 15. 21-K — Baseline → Target → Measurement
```text
Baseline → Target → AI Intervention → Measurement
→ Comparison → Validation → Business Impact
```
Targets are agreed with engineering/business stakeholders after baselines exist.

## 16. Regression Triage Example
Baseline: average triage time, engineer-hours, failure frequency, rework, root-cause accuracy.

AI-assisted workflow → measured triage time, engineer-hours, rework, accuracy and human intervention.

No arbitrary percentage is assumed.

## 17. Experimental Discipline
Where practical compare historical baseline, control workflow and AI-assisted workflow. Control for workload, engineer experience, failure complexity, release phase and environment/tool changes.

## 18. 21-L — Executive KPI Scorecard
```text
┌─────────────────────────────────────────────┐
│         ENTERPRISE AI KPI SCORECARD         │
├─────────────────────────────────────────────┤
│ Platform Health        Availability / Cost  │
│ AI Quality             Task / RAG Quality   │
│ Engineering            Cycle Time / Effort  │
│ Adoption                Active / Repeat Use  │
│ Quality                 Defects / Rework    │
│ Economics               Cost / Workflow     │
│ Strategic               Time-to-Silicon     │
└─────────────────────────────────────────────┘
```

## 19. Executive KPI Layers
**CEO/Business:** time-to-silicon, delivery predictability, productivity, business impact.
**CTO/Engineering:** cycle time, quality, adoption, AI capability performance.
**Platform:** availability, latency, GPU efficiency, cost, reliability.
**Engineering teams:** task success, time saved, workflow quality, intervention.

## 20. 21-M — Executive Business Value Chain
```text
Platform → Capability → Workflow → Productivity → Cycle Time
→ Design / Verification Speed → Time-to-Silicon
→ Customer Delivery → Business Growth
```

## 21. KPI Ownership
| KPI | Primary Owner |
|---|---|
| Platform Health | AI Platform Engineering |
| AI Quality | AI / ML / GenAI Engineering |
| RAG Quality | GenAI / Knowledge Engineering |
| Agent Success | Agent Engineering |
| Tool / EDA Success | Domain + Platform |
| Engineering Productivity | Engineering Leadership |
| Engineering Quality | Domain Engineering |
| Adoption | Product / Engineering |
| AI Economics | Platform + Finance |
| Time-to-Silicon | Engineering Leadership / Business |

## 22. 21-N — KPI Governance
```text
Define → Instrument → Collect → Validate → Review → Act → Re-baseline
```

Validate metric definitions, timestamps, workflow boundaries, identity, attribution, completeness, sampling and aggregation.

## 23. KPI Review Cadence
**Daily:** operational/platform health.
**Weekly:** AI quality, workflow performance, incidents.
**Monthly:** adoption, productivity, cost.
**Quarterly:** engineering outcomes and strategic impact.
**Milestone/release:** time-to-silicon contribution and workflow impact.

## 24. 21-O — Business Value Feedback Loop
```text
Business Outcome → KPI → Analysis → Finding
→ Platform / Workflow Improvement → New Measurement → Business Outcome
```

## 25. KPI Failure Modes
Avoid vanity metrics, counting interactions as value, measuring only tokens/GPU/latency, unsupported causation, ignoring quality/rework, adoption, cost or human validation.

## 26. KPI Maturity
```text
Infrastructure → AI System → AI Quality → Workflow
→ Engineering Productivity → Business Outcomes
```
Target: **Level 5–6**.

## 27. Strategic KPI Principle
> **Time-to-silicon should not be presented as an AI metric. It is the business outcome to which multiple engineering improvements may contribute.**

## 28. Architectural Decisions
- **AD-21-01:** Business value uses a KPI hierarchy.
- **AD-21-02:** Time-to-silicon is the strategic outcome.
- **AD-21-03:** Baselines precede targets and improvement claims.
- **AD-21-04:** AI and engineering quality are measured with productivity.
- **AD-21-05:** Adoption is not business value by itself.
- **AD-21-06:** AI economics are measured at workflow/task level where practical.
- **AD-21-07:** Attribution includes model, agent, RAG and platform versions.
- **AD-21-08:** Confounding factors are considered before causal claims.
- **AD-21-09:** KPI ownership is explicit.
- **AD-21-10:** KPI definitions/instrumentation are governed.
- **AD-21-11:** Metrics feed continuous improvement.

## 29. Trade-offs
Measurement depth vs instrumentation cost; business attribution vs causality; speed vs quality; adoption vs value; enterprise-standard KPIs vs domain-specific metrics.

## 30. What Artifact 21 Does Not Decide
Exact KPI targets, baseline values, time-to-silicon contribution, financial valuation, finance-approved cost allocation, dashboard implementation, telemetry product and experimental methodology remain dependent on actual TYLsemi data and stakeholder agreement.

## 31. Traceability
```text
01 Business Problem → 17 Lifecycle → 18 Governance → 19 Observability
→ 20 30/60/90 Roadmap → 21 Business KPIs / Time-to-Silicon
→ 22 Executive Architecture Narrative
```

## 32. Acceptance Criteria
- [ ] Business KPI framework
- [ ] Productivity KPIs
- [ ] Workflow/cycle-time KPIs
- [ ] AI quality KPIs
- [ ] Adoption KPIs
- [ ] Platform KPIs
- [ ] AI economics
- [ ] Engineering quality
- [ ] Time-to-silicon framework
- [ ] Attribution model
- [ ] Baseline/target/measurement
- [ ] Executive scorecard
- [ ] KPI ownership/governance
- [ ] Review cadence
- [ ] Feedback loop
- [ ] Maturity model
- [ ] Decisions/trade-offs

# Status
**21 — Business KPIs / Time-to-Silicon — DRAFT FOR REVIEW**

Next: **22 — Executive Architecture Narrative**
