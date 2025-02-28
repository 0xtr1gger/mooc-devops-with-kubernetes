1. Create a persistent volume manifest:

```bash
manifests/pvs/pv.yaml
```

```YAML
apiVersion: v1
kind: PersistentVolume
metadata:
  name: image-pv
spec:
  storageClassName: web-image-pv # the name of the volume used to claim this volume
  capacity:
    storage: 1Gi
  volumeMode: Filesystem # the volume will be mounted into pods as a directory
  accessModes:
  - ReadWriteOnce
  local:
    path: /tmp/kube # the volume uses path in a cluster node as a storage

  nodeAffinity: # only required for local, defines which nodes can access the volume
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - k3d-k3s-default-agent-0
```

2. Create a persistent volume claim manifest:

```bash
manifests/pvs/pvc.yaml
```

```YAML
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: image-claim # name of the volume claim, this will be used in the deployment
spec:
  storageClassName: web-image-pv # the name of the volume we are claiming
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

3. Create the `/tml/kube` directory inside your k3d agent:

```bash
docker exec -it k3d-k3s-default-agent-0 mkdir -p /tmp/kube
```


4. Apply volume manifests:

```bash
kubectl apply -f manifests/pvs/
```

Other manifests (deployment, service, and ingress) should be copied to the `manifests` folder.

5. Modify existing deployment manifest to include the volume claim:

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
      volumes:
        - name: shared-image
          persistentVolumeClaim:
            claimName: image-claim
      containers:
        - name: todo-server
          image: 0xtr1gger/todo_server:v6
          volumeMounts:
          - name: shared-image
            mountPath: /app/static
```


6. Apply the deployment, service, and ingress:

```
kubectl apply -f manifests/
```

7. Ensure all resources are up and running:

```bash
kubectl get svc,ing
```

```bash
NAME                      TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/kubernetes        ClusterIP   10.43.0.1      <none>        443/TCP    24m
service/todo-server-svc   ClusterIP   10.43.120.58   <none>        2345/TCP   7m

NAME                                         CLASS     HOSTS   ADDRESS                            PORTS   AGE
ingress.networking.k8s.io/todo-app-ingress   traefik   *       172.21.0.2,172.21.0.3,172.21.0.4   80      7m
```

```bash
kubectl get pv
```

```bash   
NAME       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                 STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
image-pv   1Gi        RWO            Retain           Bound    default/image-claim   web-image-pv   <unset>                          7m8s

```

8. Try to access the application from your browser or with `curl`:

```bash
curl http://localhost:8081
```