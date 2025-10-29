# ---------- Build fase ----------
FROM node:20 AS build

# Ga naar de juiste submap
WORKDIR /app/poke-trade-frontend

# Kopieer package bestanden
COPY poke-trade-frontend/package*.json ./

# Installeer dependencies
RUN npm install

# Kopieer alle bestanden van de frontend
COPY poke-trade-frontend .

# Build met Vite
RUN npm run build

# ---------- Nginx fase ----------
FROM nginx:alpine

# Kopieer de Vite build-output naar Nginx
COPY --from=build /app/poke-trade-frontend/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
