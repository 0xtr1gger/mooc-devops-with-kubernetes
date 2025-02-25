# Exercise 1.01: Getting started

Link to the exercise: [click](https://devopswithkubernetes.com/part-1/1-first-deploy)

1. Build the image:

```bash
BUILDX_BUILDER=1 docker build -t "random_string" . 
```

2. Tag it:

```bash
docker tag random_string 0xtr1gger/random_string:1.01  
```

3. Push to DockerHub:

```bash
docker push random_string 0xtr1gger/random_string:1.01  
```

4. Create a Deployment:

```bash
kubectl create deployment random-string --image=0xtr1gger/random_string:1.01
```

6. Ensure the Pod is running:

```bash
kubectl get pods
```

```
NAME                         READY   STATUS    RESTARTS   AGE
random-string-7479f9949f-nvrzc   1/1     Running   0          51s
```

7. Look at the logs:

```bash
kubectl logs <pod_ID>
```

```bash
kubectl logs -f random-string-7479f9949f-nvrzc
```




