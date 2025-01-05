# frontend/Dockerfile

# ====== 1) BUILD STAGE ======
FROM node:18-alpine AS build
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json yarn.lock ./

# Install dependencies
RUN yarn install
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Build the React app for production
RUN yarn build
RUN npm run build

# ====== 2) SERVE STAGE ======
FROM nginx:alpine
# Remove default Nginx static files
RUN rm -rf /usr/share/nginx/html/*

# Copy the build output from the build stage
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 (default for Nginx)
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
