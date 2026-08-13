FROM nginx:alpine

# Копируем кастомный конфиг (Nginx должен слушать порт 8080, а не 80!)
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/

# Настраиваем права доступа для встроенного пользователя nginx (UID 101)
# Ему нужен доступ на запись в папки кэша, логов и PID-файла
RUN chown -R nginx:nginx /usr/share/nginx/html && \
    chown -R nginx:nginx /var/cache/nginx && \
    chown -R nginx:nginx /var/log/nginx && \
    chown -R nginx:nginx /etc/nginx/conf.d && \
    touch /var/run/nginx.pid && \
    chown nginx:nginx /var/run/nginx.pid

EXPOSE 80

# Переключаемся на встроенного не-привилегированного пользователя
USER nginx

CMD ["nginx", "-g", "daemon off;"]