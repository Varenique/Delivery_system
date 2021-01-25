FROM python:3

ARG PATH_FOR_INITIAL_DATA="restaurants.json"
ENV PATH_FOR_INITIAL_DATA="${PATH_FOR_INITIAL_DATA}"
# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./app.py"]
