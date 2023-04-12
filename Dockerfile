# ./docker/Dockerfile
FROM python:3.10
# specifying the working directory inside the container
WORKDIR $HOME

# installing the Python dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copying the contents of our app' inside the container
COPY app $HOME/app

# defining env vars
ENV FLASK_APP=app.app
# watch app' files
ENV DEBUG=1
ENV FLASK_DEBUG=0
EXPOSE 80

COPY migrations $HOME/migrations

# running Flask as a module, we sleep a little here to make sure that the DB is fully instanciated before running our app'
CMD flask db upgrade && flask run --host=0.0.0.0 --port=80
