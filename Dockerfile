FROM python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /django

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

