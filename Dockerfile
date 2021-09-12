FROM gcc:latest

WORKDIR "/home"

COPY *.cpp ./code.cpp

RUN g++ code.cpp -o code.o

CMD ["cp", "/home/code.o", "/tmp"]
