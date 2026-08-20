from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

# Используем переменные окружения для гибкости (DevOps style)
REDIS_HOST = os.getenv("REDIS_HOST", "db")
redis = Redis(host=REDIS_HOST, port=6379, decode_responses=True)


@app.route('/api')
def hello():
    try:
        count = redis.incr('hits')
        return f'Привет! Этот сайт открывали {count} раз.'
    except Exception as e:
        return f"Ошибка БД: {str(e)}", 500


if __name__ == "__main__":
    # debug=True полезен при разработке
    app.run(host="0.0.0.0", port=5000, debug=False)
