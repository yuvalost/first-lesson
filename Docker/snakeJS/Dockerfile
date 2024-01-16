FROM node

WORKDIR /user/src/app

COPY . .

EXPOSE 8000

RUN npm install -g http-server

CMD ["http-server", ".", "-p", "8000"]