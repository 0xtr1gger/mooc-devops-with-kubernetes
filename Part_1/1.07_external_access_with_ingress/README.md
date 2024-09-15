0. For a k3d cluster, I create an Nginx webserver deployment in advance in order to expose Services, as outlined in [this](https://k3d.io/v5.3.0/usage/exposing_services/) Doc 

1. Modify previous version of the Log output script to add a Flask server and an endpoint.

2. Create a new Dockerfile to include Flask.

3. Build a new image from the Dockerfile and push it to the DockerHub:

```bash
docker build -t mooc-log-output:1.07_ingress .
docker tag mooc-log-output:1.07_ingress doreen01/mooc-log-output:1.07_ingress
docker push doreen01/mooc-log-output:1.07_ingress
```

4. Modify the deployment configuration file to use the new image version and to configure a port number.

```
manifests/service.yaml 
```

5. Create a Service configuration file.

```
manifests/service.yaml
```

6. Create an Ingress configuration file.

```
manifests/ingress.yaml
```

7. Apply all configuration files:

```bash
kubectl apply -f manifests/
```