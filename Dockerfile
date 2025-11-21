# Używamy lekkiego serwera Nginx
FROM nginx:alpine

# Kopiujemy nasz plik html do folderu, z którego Nginx serwuje pliki
COPY index.html /usr/share/nginx/html/index.html
