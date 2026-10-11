# ADR 0001: Modular monolith first

- **Status:** Accepted for MVP
- **Decision:** Keep clean internal module boundaries, but initially run a small number of deployable services rather than making every component a microservice.
- **Context:** The portfolio MVP must be runnable, testable, and inexpensive to operate while demonstrating platform boundaries.
- **Consequences:** Lower local operational complexity and faster integration. Service extraction remains possible behind stable interfaces when justified by scaling, security, ownership, or availability requirements.
