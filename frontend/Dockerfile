# 1. Используем Node.js образ
FROM node:18-alpine

# 2. Устанавливаем рабочую директорию
WORKDIR /app

# 3. Копируем package.json и устанавливаем зависимости
COPY package*.json ./
RUN npm install

# 4. Копируем остальные файлы проекта
COPY . .

# 5. Открываем порт 3000 для React
EXPOSE 3000

# 6. Запускаем приложение
CMD ["npm", "start"]
