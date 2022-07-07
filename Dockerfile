FROM python:3.9-slim


RUN apt-get update

#copy requirements.txt into container
COPY requirements.txt .

#install dev-dependencies:
RUN  pip install -r requirements.txt


#Copy function into container:
COPY lambda_function.py ./

ENTRYPOINT ["python"]

#setting the CMD to the lambda-handler:
CMD  ["lambda_function.py"]
