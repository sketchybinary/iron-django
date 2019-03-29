FROM python:3

COPY manage.py /opt/brewwolf/
COPY requirements.txt /opt/
COPY brewwolf/ /opt/brewwolf/
RUN pip install -r /opt/requirements.txt


WORKDIR /opt/brewwolf/
EXPOSE 80
CMD [ "/usr/local/bin/gunicorn", "--bind", "0.0.0.0:80", "brewwolf.wsgi:application" ]