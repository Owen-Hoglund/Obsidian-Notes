**K8S**: k - 8 letters - s
in Greek, Kubernetes means "helmsman of a ship"

**Kubernetes** allows you to manage thousands of instances of applications or microservices. This is a way of scaling an application and balancing the workload, e.g. create more instances during time periods of the week the workload is higher.

commands:
`kubectl create deployment`
`kubectl scale deployment`
`kubectl autoscale deployment`
`kubectl get events` 
`get` can also give us... pods, replicaset, service, deployment
`kubectl expose deployment`
`kubectl edit deployment`
`kubectl set image`
`kubectl autoscale deployment`

Kubernetes is a resource manager, and a resource it's great at managing is servers (which may be in the cloud, or "virtual servers").
	Amazon: EC2 (elastic compute cloud)
	Azure: virtual machines
	Google: compute engines
	Kubernetes: nodes

Container orchestration:
- manage thousands of instances or microservices

Features
- autoscaling
- service discovery
- load balancing
- self healing
- zero downtime deployments for new versions

**Kubernetes cluster**: group of servers
- one option: Google Kubernetes Engine (GKE) on Google Cloud Platform (GCP)
	- infrastructure that Google uses to run YouTube, Google Maps, and searches.
**Kubernetes Architecture**: combination of nodes and the master node.
	- **Master Node** manages cluster: checks that the other nodes are available or doing some work.
	- **Worker node(s)** run your applications.
- note: your existing application will still run via the worker nodes if the master node goes down, however, you won't be able to make and changes to the deployment.

A **pod** is the smallest deployable unit, not a container. A container needs and lives inside a pod.
Pod properties (`kubectl describe pod your-pod-name-123`) include:
- Namespace
- Priority
- PriorityClassName
- Node

**replicaset** maintains the number of pods by monitoring the minimum number needed and replicating any missing pods. 
```
cquirk01@cloudshell:~$ kubectl scale deployment hello-world-rest-api --replicas=3
deployment.apps/hello-world-rest-api scaled
cquirk01@cloudshell:~$ kubectl get replicaset
NAME                              DESIRED   CURRENT   READY   AGE
hello-world-rest-api-687d9c7bc7   3         3         3       35m
```

A **service** provides a constant front-end interface irrespective of what's happening with pods that are running on the back end.

Node agent (kubelet) - monitors the status of a node.
Networking component (kube-proxy) - allows us to expose the service.

Cloud regions & zones
- generally, reasons for using multiple:
	- latency
	- availability
	- legal requirements