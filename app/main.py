from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest
from time import perf_counter

app = FastAPI(title="Secure GitOps Platform API", version="1.0.0")
REQUESTS = Counter("secure_gitops_http_requests_total", "HTTP requests", ["method", "path", "status"])
LATENCY = Histogram("secure_gitops_http_request_duration_seconds", "Request latency", ["path"])

@app.middleware("http")
async def metrics_middleware(request, call_next):
    started = perf_counter()
    response = await call_next(request)
    REQUESTS.labels(request.method, request.url.path, str(response.status_code)).inc()
    LATENCY.labels(request.url.path).observe(perf_counter() - started)
    return response

@app.get("/")
def root():
    return {"service": "secure-gitops-platform", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/metrics", include_in_schema=False)
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
