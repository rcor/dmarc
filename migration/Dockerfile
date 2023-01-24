FROM python:3

WORKDIR /usr/src/app

ADD src ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "__init__.py" ]