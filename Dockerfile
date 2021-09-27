FROM python:3
ADD load-me-up.py /
RUN pip install flask
RUN pip install flask_restful
EXPOSE 3333
CMD [ "python", "./load-me-up.py"]
