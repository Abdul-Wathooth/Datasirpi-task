FROM python:3.11
WORKDIR /web
COPY . .
RUN pip install -r need.txt
COPY need.txt .
EXPOSE 5000
CMD ["python","app.py"]
