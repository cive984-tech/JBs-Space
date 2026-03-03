# Dockerfile

# Stage 1: Build the application
FROM node:14 AS builder
WORKDIR /app
COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Run the application
FROM node:14
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY package.json .
COPY package-lock.json .
RUN npm install --only=production
CMD ["node", "dist/server.js"]
