1. Modify the application to change the image every hour. The image is stored to `/usr/src/app/static` directory as `cached_image.jpg`.
2. Create a Dockerfile for the app.
3. Build the image and push it to the DockerHub:
```bash
docker build -t web_project:1.12_v0.6 .
docker tag web_project:1.12_v0.6 doreen01/web_project:1.12_v0.6
docker push doreen01/web_project:1.12_v0.6
```
4. Create a directory for a persistent volume on the k3d-k3s-default-agent-0 node:
```bash
docker exec k3d-k3s-default-agent-0 mkdir -p /usr/src/app/static
```
5. Create a new persistent volume and a persistent volume claim, `storage/persistentvolume.yaml`, `storate/persistentvolumeclaim.yaml`.
6. Create a deployment for the app, and specify the newly created volume claim there, `manifests/deployment.yaml`.
7. Copy the Service and Ingress for the app from the previous version of the project, v0.5.
8. Apply everything:
```bash
kubectl apply -f storage/
```
```bash
kubectl apply -f manifests/
```