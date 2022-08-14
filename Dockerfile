FROM python:3.10.5-bullseye

WORKDIR /opt
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
WORKDIR /opt/mysite
	
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]