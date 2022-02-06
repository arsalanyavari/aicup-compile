FROM openjdk:11.0.6

RUN mkdir -p /home
WORKDIR "/home"

RUN mkdir -p src/package
RUN mkdir -p build/classes

COPY main.java /home/src/package/main.java

WORKDIR "/home/src"

RUN javac -sourcepath src -d build/classes package/main.java

RUN cp ./package/main.java ../

##########################################
RUN name=`ls *.java | cut -d "." -f1`
RUN echo Main-Class: main>myManifest
##########################################

RUN jar cfm build/main.jar myManifest -C build/classes/ .

CMD ["cp", "/home/src/build/main.jar", "/tmp"]




# Finaly jar executable code is main.jar => running syntax: java -jar main.jar
