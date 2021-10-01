FROM node:14

WORKDIR /usr/src/app
COPY package*.json ./

RUN npm install

COPY . .

ENTRYPOINT [ "/usr/local/bin/npm", "run", "q2" ]