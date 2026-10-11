# Implementation Boundaries

## Platform versus workflow

Platform capabilities are reusable services: model access, knowledge retrieval, tool execution, policy enforcement, audit, evaluation, and telemetry. The regression-diagnosis workflow will compose these capabilities without embedding provider-specific logic.

## Initial deployable units

The repository is modular-monolith-first. Directories are not automatically separate network services. Split into deployable units only when operational, scaling, security, or ownership needs justify it.

## Security boundary

A model response is untrusted input. Model output cannot authorize a tool call. Tool execution must pass through deterministic identity and policy checks. Request-ID middleware provides correlation only; it does not authenticate users.

## MVP scope

The initial build uses synthetic engineering records and a mock EDA/regression adapter. No proprietary RTL, real regression logs, or customer IP should be committed.
