# Gebruik een officiële Node image
FROM node:20 AS build

# Stel werkdirectory in
WORKDIR /app

# Kopieer dependency-bestanden
COPY package*.json ./

# Installeer dependencies
RUN npm install

# Kopieer alle frontendbestanden
COPY . .

# Build de Vite productieversie
RUN npm run build

# Gebruik een lichtgewicht webserver (Nginx) om de app te hosten
FROM nginx:alpine

# Kopieer de build-output van stap 1 naar de webroot van Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Expose poort 80
EXPOSE 80

# Start de server
CMD ["nginx", "-g", "daemon off;"]