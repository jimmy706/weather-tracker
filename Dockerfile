FROM python:3.11.5-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

# Define the command to run your Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]