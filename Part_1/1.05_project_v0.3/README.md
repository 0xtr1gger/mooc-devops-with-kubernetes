1. Create a simple static web application with Flask.
2. Create a Dockerfile for the app.
3. Push the image to the DockerHub:
```bash
docker build -t web_project:0.3_web_page .
docker tag web_project:0.3_web_page doreen01/web_project:0.3_web_page
docker push web_project:0.3_web_page
```
4. Create Deployment for the application, `manifests/depployment.yaml`.
5. Apply the deployment:
```bash
kubectl apply -f manifests/deployment.yaml
```
6. Use `kubectl port-forward` to expose the application:
```bash
kubectl get pods
```

```
NAME                           READY   STATUS    RESTARTS   AGE
web-project-5c5db7dd4f-f4tdg   1/1     Running   0          32s
```

```bash
kubectl port-forward web-project-5c5db7dd4f-f4tdg 5000:5000
```
```
Forwarding from 127.0.0.1:5000 -> 5000
Forwarding from [::1]:5000 -> 5000
Handling connection for 5000
```