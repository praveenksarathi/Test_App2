#The repository from which Flask is pulled in
FROM tiangolo/uwsgi-nginx-flask:flask

COPY ./app /app

# tell the port number the container should expose
EXPOSE 5000

# Command to run the program
CMD ["python", "./app_get.py","-p 5000"]

#CMD ["curl -i http://localhost:5000/todo/api/v1.0/tasks"]
