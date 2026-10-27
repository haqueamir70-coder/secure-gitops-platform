# Incident Runbook

## 1. Initial triage

1. Confirm alert timestamps, affected environment, and scope.
2. Check deployment health:

   ```bash
   kubectl -n secure-gitops-demo get deploy,pods,svc,hpa,pdb
   kubectl -n secure-gitops-demo rollout status deployment/secure-gitops-api
   kubectl -n secure-gitops-demo describe deployment secure-gitops-api
   kubectl -n secure-gitops-demo logs deployment/secure-gitops-api --all-containers=true --tail=200
   ```

3. Inspect recent deployment and image changes; verify image reference and image pull errors.
4. Review `/health`, `/ready`, request rate, 5xx rate, and latency metrics.

## 2. Common symptoms

### Pods are not Ready

- Check `kubectl describe pod` events and container logs.
- Confirm `/ready` is served on port 8000.
- Confirm the image starts as UID 10001 and works with a read-only root filesystem.

### Service has no endpoints

- Check Service selector and pod labels.
- Check readiness status and `kubectl -n secure-gitops-demo get endpointslices`.

### Network traffic is blocked

- Verify that the CNI enforces NetworkPolicy.
- Inspect ingress/monitoring namespace and pod labels; adapt allowed peers deliberately.
- Preserve least privilege; do not disable the policy as a permanent fix.

### HPA does not scale

- Confirm metrics-server is available and `kubectl top pods` works.
- Compare CPU utilization with requests and HPA target.

## 3. Mitigation and rollback

For a bad rollout, only roll back if the previous ReplicaSet/image is known to be safe and compatible:

```bash
kubectl -n secure-gitops-demo rollout history deployment/secure-gitops-api
kubectl -n secure-gitops-demo rollout undo deployment/secure-gitops-api
kubectl -n secure-gitops-demo rollout status deployment/secure-gitops-api
```

Verify health and error rate after mitigation. Do not run rollback blindly where database or schema changes may be irreversible.

## 4. Closure

Record impact, start/end time, detection source, contributing factors, mitigation, and actionable follow-ups. Run a blameless review for material incidents.
