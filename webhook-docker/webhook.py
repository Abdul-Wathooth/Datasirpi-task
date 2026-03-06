from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    os.system("./deploy.sh")
    return "Deployment triggered"

app.run(host='0.0.0.0', port=9000)
