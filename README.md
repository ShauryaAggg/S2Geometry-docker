## Usage

##### Build

Build the docker container with the given `PLATFORM` the given the `IMAGE_NAME`

```sh
make build
```

##### Run

Build the image with the given `PLATFORM`, `IMAGE_NAME`, delete the previous container, and start a new one

```sh
make run
```

##### Start Container

Start the already built container

```sh
make start
```

##### Delete Container

Delete the previous existing container

```sh
make clean
```

##### Stop Container

Stop the existing container

```sh
make stop
```