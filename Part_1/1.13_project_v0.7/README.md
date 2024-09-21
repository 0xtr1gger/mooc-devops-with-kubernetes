1. Alter the application to add a form and a sample to-do list.
2. Build a new image and push it to the DockerHub:
```bash
docker build -t web_project:1.13_v0.7 .
docker tag web_project:1.13_v0.7 doreen01/web_project:1.13_v0.7
docker push doreen01/web_project:1.13_v0.7
```
3. Update the deployment, `manifest/deployment.yaml`, to use the new image.
4. Apply everything:
```bash
kubectl apply -f storage/
kubectl apply -f manifests/
```