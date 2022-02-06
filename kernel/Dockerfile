# Tag name read from env KERNEL_IMAGE_TAG default is aicup-kernel:latest
# Please put map.json and main(kernel) next to Dockerfile before build
FROM ubuntu

RUN apt update
RUN apt install openjdk-16-jdk -y

RUN TZ=Asia/Tehran
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install libstdc++6 -y

WORKDIR /home/kernel
ENV MAP_PATH=/home/kernel/map.json
ENV PLAYER1_PATH=/home/players/1
ENV PLAYER2_PATH=/home/players/2

COPY ./main .
COPY map.json .

CMD ./main -p1 $PLAYER1_PATH -p2 $PLAYER2_PATH
