# Use a imagem oficial do Node.js como base
FROM node:14

# Crie e defina o diretório de trabalho dentro do contêiner
WORKDIR /usr/src/app

# Copie o package.json e package-lock.json para o diretório de trabalho
COPY package*.json ./

# Instale as dependências do projeto
RUN npm install express multer path express-basic-auth

# Copie todos os arquivos do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Exponha a porta 3000 do contêiner
EXPOSE 3000

# Comando para iniciar o servidor
CMD ["node", "app.js"]
