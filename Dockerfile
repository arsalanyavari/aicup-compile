FROM openjdk:latest

RUN mkdir -p /home
WORKDIR "/home"

RUN mkdir -p src/package
RUN mkdir -p build/classes

WORKDIR "/home/src"

COPY *.java ./src/package/
RUN javac -sourcepath src -d build/classes package/*.java
RUN cp ./package/*.java ./

##########################################
RUN name=`ls *.java | cut -d "." -f1`
RUN echo Main-Class: main>myManifest
##########################################

RUN jar cfm build/main.jar myManifest -C build/classes/ .

CMD ["cp", "/home/src/build/main.jar", "/tmp"]




# Finaly jar executable code is main.jar => running syntax: java -jar main.jar