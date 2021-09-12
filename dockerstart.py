from docker import from_env
from sys import argv
from os import listdir

codePATH = str(argv[1])

fileName = listdir(codePATH)

client = from_env()

# volume configuration
volume = {
    '/tmp/test': {
        'bind': '/tmp',
        'mode': 'rw',
    },
}

env = {"Name_Variable": "Name_Path", "Name_Variable2": "Name_Path2"}

if "main.py" in fileName:
    # docker build command
    # client.images.build(path="/home/arya/Desktop/testdocker", tag="aicup")
    # docker run command

    # , stdin_open=True, tty=True => such -it in docker run :))
    # client.containers.run(image='ubuntu', name='finaltest1',
    #                      volumes=volume, detach=True, environment=env)
    pass
elif "main.cpp" in fileName:
    # docker build command
    # client.images.build(path="/home/arya/Desktop/testdocker", tag="aicup")

    # , stdin_open=True, tty=True => such -it in docker run :))
    # client.containers.run(image='ubuntu', name='finaltest1',
    #                      volumes=volume, detach=True, environment=env)
    pass
elif "main.java" in fileName:
    # docker build command
    # client.images.build(path="/home/arya/Desktop/testdocker", tag="aicup")

    # , stdin_open=True, tty=True => such -it in docker run :))
    # client.containers.run(image='ubuntu', name='finaltest1',
    #                      volumes=volume, detach=True, environment=env)
    pass
else:
    pass


print("YES")
