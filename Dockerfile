FROM python:3

COPY manage.py /opt/demo/
COPY requirements.txt /opt/
COPY ./tutorial /opt/demo/tutorial/
COPY ./snippets /opt/demo/snippets/
RUN pip install -r /opt/requirements.txt


WORKDIR /opt/demo/
EXPOSE 80
CMD [ "/usr/local/bin/gunicorn", "--bind", "0.0.0.0:80", "tutorial.wsgi:application" ]