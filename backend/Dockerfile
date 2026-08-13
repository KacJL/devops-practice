FROM python:3.12-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /app/wheels -r requirements.txt

# === ФИНАЛЬНЫЙ СТЭЙДЖ ===
FROM python:3.12-slim
WORKDIR /app

# 1. Создаем системную группу и пользователя (например, с UID/GID 10001)
RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g appgroup -m -s /bin/bash frontend-app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.txt && rm -rf /wheels

COPY . .

# 2. Менять владельца файлов приложения нужно ОБЯЗАТЕЛЬНО, 
# иначе non-root пользователь не сможет их прочитать/запустить
RUN chown -R frontend-app:appgroup /app

ENV PYTHONUNBUFFERED=1
EXPOSE 5000

# 3. Переключаемся на созданного пользователя. 
# Все последующие команды (включая CMD) будут выполняться от его имени.
USER frontend-app

CMD ["python", "app.py"]
