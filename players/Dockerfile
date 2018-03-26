FROM python:3.6.3

COPY random/aifleet/requirement.txt /var/tmp/requirements.txt
RUN pip install -r /var/tmp/requirements.txt

WORKDIR /var/www/player

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

