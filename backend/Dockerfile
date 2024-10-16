# 1. Указываем базовый образ Python
FROM python:3.10-slim

# 2. Устанавливаем рабочую директорию
WORKDIR /app

# 3. Копируем файл с зависимостями в контейнер
COPY requirements.txt .

# 4. Устанавливаем зависимости через pip
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем остальные файлы проекта в контейнер
COPY . .

# 6. Открываем порт 8000 для FastAPI
EXPOSE 8000

# 7. Запускаем приложение с использованием uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
