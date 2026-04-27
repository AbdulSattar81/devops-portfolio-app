from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
   return f'Hello from {socket.gethostname()} — DevOps pipeline working!'

@app.route('/health')
def health():
   return {'status': 'ok'}, 200

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
