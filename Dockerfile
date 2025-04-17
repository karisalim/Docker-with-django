FROM python:3.12-alpine3.20


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app
COPY requirements.txt .


RUN pip install --upgrade pip

RUN pip install -r requirements.txt
COPY . .
# جمع الملفات الثابتة
RUN python manage.py collectstatic --noinput

# EXPOSE 1234
  EXPOSE 8000

# CMD ["python", "manage.py" , "runserver", "0.0.0.0:1234"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "elevate.wsgi:application"]

