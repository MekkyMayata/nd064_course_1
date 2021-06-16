# set base image
FROM golang:alpine

# set working directory
WORKDIR /go/src/app

# copy files
COPY ./ ./

# build app
RUN go mod init
RUN go build -o helloworld

EXPOSE 6111

CMD ["./helloworld"]