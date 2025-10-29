# ---------- Build fase ----------
FROM node:20 AS build

# Zet de werkdirectory
WORKDIR /app

# Kopieer ALLES uit de frontend-map (inclusief submappen)
COPY ./poke-trade-frontend ./poke-trade-frontend

# Ga de submap in
WORKDIR /app/poke-trade-frontend

# Installeer dependencies
RUN npm install

# Build met Vite
RUN npm run build

# ---------- Nginx fase ----------
FROM nginx:alpine

# Kopieer de Vite build-output naar Nginx
COPY --from=build /app/poke-trade-frontend/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
