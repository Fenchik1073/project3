from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def log_ip():
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Зберігаємо IP у файл
    with open('ip_log.txt', 'a') as f:
        f.write(f"{timestamp} | IP: {user_ip} | UA: {user_agent}\n")

    return f"""
    <h2>Спасибо за посещения сайта!</h2>
    <p>Вы взломаны.</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)