FROM python:3.12.3
WORKDIR /
COPY .  .
RUN pip install -r requirements.txt
CMD ["python", "main_general.py"]
