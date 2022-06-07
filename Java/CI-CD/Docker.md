`docker run`

a **Docker image** allows you to quickly deploy instances of an application wherever a container runtime is installed. 

Docker provides standardization of packaging and deployment of application irrespective of language or framework used to build the app, or the platform where you want to deploy to. It is cloud neutral and language neutral.

[[Kubernetes]] will allow you to manage many instances of an application deployed with Docker.

**Docker Hub** (hub.docker.com) is where you can find repositories of docker images.

## Docker images
Docker images contain everything you need to run an app on your local machine, without worrying about having specific software or versions installed.
`docker images` shows all images on local machine.
`docker image history YOUR_IMAGE_ID` gives a breakdown of commands involved in running this application. e.g. java -jar in order to start a Java app

## Docker containers
Applications run in Docker containers.
`docker container ls -a`
without `-a`, gives only running containers.
`docker container rm` and `docker image remove` in that order, otherwise it will say the image is being used in a container.
*There are many commands like this that help you manage Docker images and active/inactive containers, including `docker logs container-name` . The container ID (e.g. e971d1583720ddfa9a5db45f354f6b1dad907a0524822af785de60886d53098a) will be useful as well.**

## Dockerfile
A Dockerfile contains commands that allow us to automate the creation of Docker images.
Example:
```
FROM openjdk:8-jdk-alpine
VOLUME /tmp
EXPOSE 5000
ADD target/*.jar app.jar
ENTRYPOINT [ "sh", "-c", "java -jar /app.jar" ]
```

Dockerfile Maven plugin allows for the creation of a docker image during the typical Maven lifecycle. 
**E.g. in Eclipse**: Select Maven project directory -> run as Maven build -> goals: "package" -> Run.

## Docker Hub
`docker login` authorizes you
`docker push` with your repository name pushes your image up to Docker Hub.