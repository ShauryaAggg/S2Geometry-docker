IMAGE_NAME ?= s2geo
CONTAINER ?= s2geo
PLATFORM ?= linux/amd64

.PHONY: build
build: # Build the docker container
	sudo docker buildx build --platform ${PLATFORM} -f Dockerfile -t ${IMAGE_NAME} .

.PHONY: clean
clean: # Remove existing container with the same name 
# Command shouldn't fail if the container doesnt exist
	docker rm ${CONTAINER} || true 

.PHONY: run
run: build # Build the container
	$(MAKE) clean # Delete the existing container and run a new one
	docker run --name ${CONTAINER} -p 8888:8888 -v $(PWD)/notebooks:/usr/src/notebooks -it ${IMAGE_NAME}

.PHONY: start
start: # Start the container
	docker start -i ${CONTAINER}

.PHONY: stop
stop: # Stop the container 
# Command shouldn't fail if the container doesnt exist
	docker stop ${CONTAINER} || true