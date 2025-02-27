
1. Create a deployment:

```bash
manifests/deployment.yaml
```

```YAML

```

2. Apply the deployment:

```bash
kubectl apply -f manifests/
```

3. List currently running pods:

```bash
kubectl get pods
```

```
NAME                           READY   STATUS    RESTARTS   AGE
todo-server-6b549d5457-59cgd   1/1     Running   0          23m
```

4. Use the `port-forward` command:

```bash
kubectl port-forward 
```

```bash
Forwarding from 127.0.0.1:5003 -> 5000
Forwarding from [::1]:5003 -> 5000
Handling connection for 5003
Handling connection for 5003
```

5. Access the server on `locahost:5003`:

```bash
curl http://localhost:5003
```

6. Delete objects:

```bash
kubectl delete -f manifests/
```

