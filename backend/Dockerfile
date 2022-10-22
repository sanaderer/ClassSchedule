FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY docker-requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code/
RUN chmod +x docker-entrypoint.sh
CMD ./docker-entrypoint.sh

