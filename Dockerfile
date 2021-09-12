FROM python:latest

WORKDIR "/home"

## mr roghani said
RUN pip install numpy

RUN pip install pyinstaller

COPY *.py ./code.py
## binary code is in /dist/code/ directory but it depends on its libraries and its name is code
RUN python -m PyInstaller code.py 

CMD ["cp", "-r", "/home/dist/code", "/tmp"]




# Finaly python executable code is ./code/code