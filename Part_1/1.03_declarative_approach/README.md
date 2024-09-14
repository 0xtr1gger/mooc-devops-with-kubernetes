1. Use the image from the Exercise 1.01: Getting started to create a deployment with a YAML configuration file inside the `manifests` directory.

```bash
manifests/deployment.yaml
```

2. Apply the deployment:

```bash
kubectl apply -f manifests/deployment.yaml
```

3. View the logs:

```bash
kubectl get pods
```
```
NAME                               READY   STATUS        RESTARTS   AGE
log-output-depl-6658df47bf-lp5qk   1/1     Running       0          5s
```

```bash
kubectl log log-output-depl-6658df47bf-lp5qk
```