## Loop control with continue and breake in python

### it can be applied to DevOps monitoring

below we have some service and im gonna check each of server's status using python
```bash
deployments = [
    {"name": "nginx-ingress-controller", "status": "success"},      # Load balancer untuk Kubernetes
    {"name": "prometheus-monitoring", "status": "success"},         # Monitoring service
    {"name": "postgres-database", "status": "pending"},             # Database service
    {"name": "grafana-dashboard", "status": "failed"},              # Visualisasi monitoring
    {"name": "frontend-react-app", "status": "success"},            # Web aplikasi
    {"name": "backend-api-service", "status": "pending"},           # API backend
    {"name": "redis-cache", "status": "success"},                   # Cache service
    {"name": "elastic-search", "status": "success"},                # Search engine
]
```

### Python loop
```bash
for deployment in deployments:
    if deployment ["status"] == "success":
        continue
    if deployment["status"] == "failed":
        print(f"Deployment {deployment['name']} failed. process stopped.")
        break
    print(f"Deployment {deployment['name']} status: {deployment['status']}")
```

in this simple example we Automate basic check and implement conditional logic like stopping from failure using pthon 