# Secure GitOps — Advanced Interview Question Bank

> 40 additional questions and answers. Use with [ZERO-TO-HERO.md](./ZERO-TO-HERO.md). Verify all claims against source, CI and deployment evidence.

## Project context
- **Architecture:** Commit → CI/test/scan/SBOM → immutable image → Git desired state → pull controller → cluster policy
- **Tools:** GitHub Actions, Docker, Trivy, SBOM, Kubernetes, Argo CD/Flux where configured, NetworkPolicy, RBAC, Prometheus
- **Failure modes:** scan non-blocking, mutable tag, drift, controller outage, bad rollout
- **Mitigation:** Check scan exit-code policy, deploy digest, reconcile via Git, monitor sync/health and rollback by reverting desired state.

## Answer method
Context → decision → implementation → trade-off → failure handling → evidence.

## 40 questions with answers

### 1. What business problem does this project solve?

Explain user/operator pain, business impact and measurable outcome.

### 2. Who are the actors and trust boundaries?

Identify users, developers, operators, workload identities and external services; mark identity and network boundaries.

### 3. Explain the end-to-end flow.

Walk through every component and hand-off, protocol, identity, persistence boundary and response path.

### 4. Why split the architecture into components?

Each has bounded responsibility, independent scaling/failure domain and explicit interface.

### 5. Which non-functional requirements matter?

Availability, latency, throughput, security, recoverability, auditability, operability and cost.

### 6. Why use the primary tool?

It makes desired state repeatable, reviewable and automatable; compare alternatives and trade-offs.

### 7. What does CI validate—and not validate?

Static checks do not prove live deployment, permissions, network reachability, runtime behavior or DR.

### 8. How are environments handled?

Separate reusable logic from environment inputs, validate types, keep secrets out of source and promote explicitly.

### 9. How make deployment reproducible?

Pin tool/provider/action versions, lock dependencies, use immutable artifacts and version interfaces.

### 10. How are secrets managed?

Prefer managed identity/OIDC, least privilege and secret manager; rotate and audit, never print.

### 11. What failure would you test first?

Pick a high-impact dependency failure and define detection, impact, mitigation, recovery and evidence.

### 12. How troubleshoot an outage?

Scope impact, inspect changes, logs/events/metrics, identity, DNS/network, dependencies and saturation.

### 13. Authentication versus authorization?

Authentication proves identity; authorization decides allowed actions at resource/data scope.

### 14. How enforce least privilege?

Dedicated identities, narrow scope, minimum actions, privileged-operation review.

### 15. How prevent drift?

Reviewed desired state, scheduled detection, controlled break-glass changes and reconciliation.

### 16. What belongs in logs?

Timestamps, correlation IDs, outcomes, timings and security events; exclude tokens, keys and sensitive payloads.

### 17. How retry safely?

Bounded exponential backoff with jitter and idempotency/deduplication.

### 18. How design recovery?

Set RPO/RTO, protect backups, test restore and application consistency.

### 19. How scale?

Measure bottleneck, latency, throughput and saturation; scale constrained tier and validate cost.

### 20. Which metrics matter?

Availability, errors, latency percentiles, throughput, saturation, queue lag and dependency health.

### 21. How reduce alert noise?

Actionable sustained symptoms, appropriate windows, deduplication, ownership and runbooks.

### 22. What security gates belong in CI?

Secret/dependency/source/image/IaC scans, policy, severity thresholds and expiring exceptions.

### 23. What are cost drivers?

Compute, storage, egress, managed tiers, telemetry ingestion and idle capacity; measure cost per unit.

### 24. How roll back safely?

Known-good immutable artifact, explicit trigger, data compatibility, restore and monitor.

### 25. What evidence proves implementation?

Source, tests, workflow runs, resource IDs, live checks, security evidence, telemetry and runbooks.

### 26. What is implemented versus planned?

Inspect source/workflows and label implemented, CI-validated, deployed or planned.

### 27. How test end to end?

Happy path, invalid input, denied access, outage, retries, scale, rollback and recovery.

### 28. What are key trade-offs?

Simplicity/flexibility, cost/availability, centralization/autonomy, security/usability.

### 29. What improve next?

Missing tests, weak identity, unverified recovery, missing telemetry, unclear ownership.

### 30. Give a 2-minute explanation.

Business problem, architecture, decisions, security/reliability, failure scenario and evidence.

### 31. Explain Secure GitOps architecture.

Commit → CI/test/scan/SBOM → immutable image → Git desired state → pull controller → cluster policy. Explain trust boundaries, failure domains and data/control hand-offs.

### 32. Which tools are central and why?

Tool inventory: GitHub Actions, Docker, Trivy, SBOM, Kubernetes, Argo CD/Flux where configured, NetworkPolicy, RBAC, Prometheus. Explain responsibility, configuration, integration, limitations and alternatives; separate required from optional tools.

### 33. What are the key failure modes?

Main risks: scan non-blocking, mutable tag, drift, controller outage, bad rollout. Prioritize by impact and likelihood; define detection, containment and recovery.

### 34. How troubleshoot the likely incident?

Check scan exit-code policy, deploy digest, reconcile via Git, monitor sync/health and rollback by reverting desired state. Inspect scope/recent changes, telemetry and isolate layers; verify with a regression test.

### 35. How prove security controls work?

Create positive/negative tests for identity, authorization and network paths. Confirm permitted actions succeed and unauthorized actions fail.

### 36. How prove implementation?

Show source, tests, CI runs, resource IDs and live checks. Label implemented, CI-validated, cloud-deployed or planned.

### 37. What would you demo to a CTO?

Reproduce validation/build, trace architecture, show source/config, successful and failing test, telemetry and rollback.

### 38. What are operational limits?

Identify quotas, throughput/concurrency, state/partition constraints, dependencies and recovery objectives; test representative load.

### 39. How improve maintainability?

Cohesive modules, explicit interfaces, typed configuration, pinned dependencies, automated tests and actionable runbooks.

### 40. How measure success?

Choose indicators tied to business outcomes: reliability, latency, freshness, lead time, policy compliance or unit cost.

## Source-code deep-dive checklist
For every actual file, record its path and explain:
1. Terraform: versions/providers/backend, variables/validation, locals/data/resources, dependencies/lifecycle, outputs and state addresses.
2. GitHub Actions: triggers/permissions/runner, actions, environment/secrets/identity, working directory, every step, artifacts, conditions and failures.
3. Docker: base image, context/layers, ARG/ENV, COPY, ENTRYPOINT/CMD, user, ports, health check and filesystem.
4. Kubernetes: apiVersion/kind, metadata/selectors, replicas/strategy, image digest, probes, resources, securityContext, service account, volumes, Service/Ingress.
5. Application code: entry point, config, validation, business logic, errors, retries/timeouts, authN/authZ, logs, metrics and tests.
6. Policy/observability: rule, fixture, exit code, metric/label, query, alert window and runbook.

## Hands-on labs
Trace one real change end-to-end; break a safe dependency and diagnose it; demonstrate permitted/denied access; change an input and inspect plan; reproduce/fix CI failure; rollback; create an evidence matrix.

## Honesty rule
Optional tools are not automatically implemented dependencies. Conceptual/legacy projects remain design exercises until code and tests prove functionality. A diagram or static validation is not deployment evidence.
