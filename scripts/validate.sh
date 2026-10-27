#!/usr/bin/env sh
set -eu

python -m compileall -q app tests
pytest -q

if command -v docker >/dev/null 2>&1; then
  docker build -t secure-gitops-platform:local .
else
  echo "Docker not found; skipped container build." >&2
fi

if command -v kubectl >/dev/null 2>&1; then
  kubectl kustomize k8s >/dev/null
  echo "Kustomize rendering succeeded. Cluster validation is still required."
else
  echo "kubectl not found; skipped Kubernetes manifest rendering." >&2
fi
