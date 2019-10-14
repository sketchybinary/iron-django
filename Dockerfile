FROM python:3

COPY requirements.txt /opt/
RUN pip install --upgrade pip && \
    pip install -r /opt/requirements.txt

COPY brewwolf/ /opt/brewwolf/
RUN cd /opt/brewwolf && \
    python manage.py collectstatic --no-input
COPY entrypoint.sh /opt/brewwolf/entrypoint.sh
RUN chmod +x /opt/brewwolf/entrypoint.sh

WORKDIR /opt/brewwolf/
EXPOSE 80
ENTRYPOINT "/opt/brewwolf/entrypoint.sh"
CMD [ "gunicorn" ]