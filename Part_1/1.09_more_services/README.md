1. Create pingpong.py that accepts GET requests to /pingpong.
2. Create a Dockerfile for the app.
3. Build an image and push it to the DockerHub:
```bash
docker build -t mooc-ping-pong:1.09_more_services .
docker tag mooc-ping-pong:1.09_more_services doreen01/mooc-ping-pong:1.09_more_services
docker push doreen01/mooc-ping-pong:1.09_more_services
```
4. Create a deployment for it named pong_deployment.yaml; the previous deployment form 0.07 will have name log_deployment.yaml.
5. Create two services for applications, ping_service.yaml and log_service.yaml.
6. Create an ingress.yaml. It will direct traffic to different applications based on URL.
7. Apply everything:
```bash
kubectl apply -f manifests/
```