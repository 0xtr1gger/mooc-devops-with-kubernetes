# Exercise 1.04: Project v0.2

1. Create a YAML manifest for a new deployment:

```
manifests/deployment.yaml
```

```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
  name: todo-server
spec:
  replicas: 1
  selector:
    matchLabels:
      app: todo-server
  template:
    metadata:
      labels:
        app: todo-server
    spec:
      containers:
        - name: todo-server
          image: 0xtr1gger/todo_server:v
```

2. Apply the Deployment:

```bash
kubectl apply -f manifests/deployment.yaml
```

3. Ensure the Pod is running:

```bash
kubectl get pods
```

```bash
NAME                           READY   STATUS              RESTARTS   AGE
todo-server-6b549d5457-pgmtc   1/1     Running   0         11s

```

4. Check the logs:

```bash
kubectl logs todo-server-6b549d5457-pgmtc
```

5. Delete the Deployment:

```bash
kubectl delete -f manifests/deployment.yaml

```

---

## Troublehooting

- To get information about a Kubernetes resource:

```bash
kubectl describe pod todo-server-6b549d5457-pgmtc
```

- To get the logs of everything that happened in the cluster:

```bash
kubectl get events
```


