FROM node:24-alpine

ENV BACKEND_URL=http://0.0.0.0:5000

WORKDIR /app

ADD frontend /app

RUN npm install

# RUN npm run build

ENTRYPOINT ["npm"]

CMD ["start"]