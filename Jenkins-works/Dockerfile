FROM python:3.11
WORKDIR /web
COPY need.txt .
RUN pip install -r need.txt
COPY . .
EXPOSE 5000
CMD ["python","app.py"]
