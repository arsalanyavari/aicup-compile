FROM gcc:11.2.0

WORKDIR "/home"

COPY main.cpp ./main.cpp

RUN g++ main.cpp -o main

CMD ["cp", "/home/main", "/tmp"]
