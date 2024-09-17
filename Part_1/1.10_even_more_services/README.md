1. Create a timestamp writer script, log_print/log_print.py.
2. Create a reader script, timestamp_gen/timestamp_gen.py that reads a timestamp from a file, generates a hash from the timestamp file, and then displays it on a web page.
3. Create a Dockerfile for the writer script.
4. Create a Dockerfile for the reader script.
5. Build an image for the writer script and push the image to the DockerHub:
```bash
docker build -t mooc-log-output:1.10_writer .
docker tag mooc-log-output:1.10_writer doreen01/mooc-log-output:1.10_writer
docker push doreen01/mooc-log-output:1.10_writer
```
6. Build an image for the reader script and push the image to the DockerHub:
```bash
docker build -t mooc-log-output:1.10_reader .
docker tag mooc-log-output:1.10_reader doreen01/mooc-log-output:1.10_reader
docker push doreen01/mooc-log-output:1.10_reader
```
7. Create a Deployment for two applications, manifests/deployment.yaml. Here, specify a shared volume.
8. Create a service for the application, manifests/service.yaml.
9. Create an Ingress to expose the application, manifests/ingress.yaml.
10. Apply everything:
```bash
kubectl apply -f manifests/
```