FROM python:3.11.3
WORKDIR /Trainingmate/
COPY requirements.txt req.txt
RUN pip3 install -r req.txt
COPY . .
EXPOSE 8080
CMD ["python3", "Trainingmate.py"]
