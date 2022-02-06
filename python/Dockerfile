FROM aicuppy:latest

WORKDIR "/home"

COPY ./main.py ./main.py
## binary code is in /dist/code/ directory but it depends on its libraries and its name is code
RUN python -m PyInstaller --onefile main.py 

CMD ["cp", "/home/dist/main", "/tmp"]




# Finaly python executable code is ./main
