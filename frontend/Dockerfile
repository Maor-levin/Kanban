# ====== 1) BUILD STAGE ======
FROM node:18-alpine AS build
WORKDIR /app

ENV NODE_ENV=development

# Copy package files
COPY package*.json ./

# Force installation of devDependencies by setting NODE_ENV to development
ENV NODE_ENV=development

# Install dependencies (including devDependencies)
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Build the React app for production
RUN npm run build

# ====== 2) SERVE STAGE ======
FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
