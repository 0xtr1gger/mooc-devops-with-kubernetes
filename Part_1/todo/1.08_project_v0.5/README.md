
1. Create a YAML manifest for a new deployment:

```bash
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

2. Create a new ClusterIP Service manifest:

```bash
manifests/service.yaml
```

```YAML
apiVersion: v1
kind: Service
metadata:
  name: todo-server-svc
spec:
  type: ClusterIP
  selector:
    app: todo-server
  ports:
    - port: 2345
      protocol: TCP
      targetPort: 5000
```

3. Create a new Ingress manifest:

```bash
manifests/ingress.yaml
```

```bash
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: todo-app-ingress
spec:
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: todo-server-svc
            port:
              number: 2345
```

4. Apply all manifests:

```bash
kubectl apply -f manifests/
```

5. Ensure all resources are up and running:

```bash
kubectl get svc,ing
```

```
NAME                      TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/kubernetes        ClusterIP   10.43.0.1       <none>        443/TCP    13h
service/todo-server-svc   ClusterIP   10.43.249.177   <none>        2345/TCP   21s

NAME                                         CLASS     HOSTS   ADDRESS                            PORTS   AGE
ingress.networking.k8s.io/todo-app-ingress   traefik   *       172.21.0.2,172.21.0.3,172.21.0.4   80      21s
```

6. Try to access the application from outside of the cluster:

```bash
curl http://localhost:8081
```