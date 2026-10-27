# SLO and Error Budget

## Purpose

This document defines an illustrative SRE exercise for the Secure GitOps Platform. These are proposed targets only; no production measurements are implied.

## Example service-level objective

- **SLI:** successful `/health` requests divided by all `/health` requests during the measurement window.
- **Target:** 99.9% success over a rolling 30-day window.
- **Measurement:** derive from Prometheus request counters, excluding explicitly documented synthetic probes if your measurement policy requires it.
- **Error budget:** 0.1% of eligible requests may fail during the same window.

## Operating policy

1. Review the SLI dashboard and alert quality during each operational review.
2. When budget burn is high, prioritize reliability work over risky feature releases.
3. Investigate changes in 5xx rate, latency, traffic, and dependency errors together.
4. Document the incident timeline, customer impact, mitigation, and follow-up actions.

## Query examples

Assuming Prometheus scrapes this application's `/metrics` endpoint:

```promql
sum(rate(secure_gitops_http_requests_total{status=~"5.."}[5m]))
/
sum(rate(secure_gitops_http_requests_total[5m]))
```

Example request rate:

```promql
sum(rate(secure_gitops_http_requests_total[5m]))
```

Example p95 latency by route:

```promql
histogram_quantile(0.95, sum by (le, path) (rate(secure_gitops_http_request_duration_seconds_bucket[5m])))
```

Confirm metric names and labels against the running `/metrics` output before operational use. Never present this example SLO as a contractual SLA.
