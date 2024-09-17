1. Use the web_server.py script from the exercise 1.02.
2. Create a Dockerfile for the script.
3. Build an image and push it to the DockerHub 
```bash
docker build -t mooc-project:v0.2 .
docker tag mooc-project:v0.2 doreen01/mooc-project:v0.2
docker push doreen01/mooc-project:v0.2
```
4. Create Deployment YAML file for the project, manifests/deployment.yaml
5. Apply it
```bash
kubectl apply -f manifests/deployment.yaml
```

```bash
kubectl get pods
```
```
NAME                            READY   STATUS    RESTARTS   AGE
project-depl-778fd58bb7-8d5dl   1/1     Running   0          43s
```