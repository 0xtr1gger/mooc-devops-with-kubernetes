# Exercise 1.05: Project v0.4

>Use a NodePort Service to enable access to the project.

Link to the Exercise: https://devopswithkubernetes.com/part-1/3-introduction-to-networking

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

2. Create a NodePort service:

```
manifests/nodeport_service.yaml
```

```YAML
apiVersion: v1
kind: Service
metadata:
  name: todo-server-svc
spec:
  type: NodePort
  selector:
    app: todo-server
  ports:
    - name: http
      nodePort: 30080
      protocol: TCP
      port: 1234
      targetPort: 5000
```

3. Apply the deployment and service:

```bash
kubectl apply -f manifests/
```

4. List services:


```bash
kubectl get svc
```

```bash
NAME              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes        ClusterIP   10.43.0.1       <none>        443/TCP          33s
todo-server-svc   NodePort    10.43.145.137   <none>        1234:30080/TCP   6s
```

5. Access the server from outside of the cluster:

```bash
curl http://localhost:8081
```

5. Delete the deployment and service:

```bash
kubectl delete -f manifests/
```