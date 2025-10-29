# ---------- Bouwfase ----------
FROM node:20 AS build

# Stel de werkdirectory in
WORKDIR /app

# Kopieer package.json + package-lock.json vanuit de submap
COPY poke-trade-frontend/package*.json ./

# Installeer dependencies
RUN npm install

# Kopieer de rest van de frontendcode
COPY poke-trade-frontend ./

# Build de productieversie
RUN npm run build

# ---------- Productie ----------
FROM nginx:alpine

# Kopieer de build-output naar Nginx
COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
