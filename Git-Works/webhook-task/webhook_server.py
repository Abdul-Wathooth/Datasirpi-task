from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    subprocess.call(['/home/user/webhook-project/webhook.sh'])
    return "Deployment Triggered", 200

if __name__ == '__main__':
    app.run(port=5000)
