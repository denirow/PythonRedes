const express = require('express');
const multer = require('multer');
const path = require('path');
const basicAuth = require('express-basic-auth');
const https = require('https');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

// Usuário e senha para autenticação básica
const users = {
  'devops': 'stAqJ5ER5C7kxglJw5'
};

// Middleware para autenticação básica
app.use(basicAuth({
  users: users,
  unauthorizedResponse: getUnauthorizedResponse
}));

function getUnauthorizedResponse(req) {
  return req.auth ? ('Credenciais ' + req.auth.user + ':' + req.auth.password + ' rejeitadas') : 'Credenciais não fornecidas';
}

// Configuração do Multer para o armazenamento de arquivos
const storage = multer.diskStorage({
  destination: function(req, file, cb) {
    cb(null, 'uploads/');
  },
  filename: function(req, file, cb) {
    cb(null, file.originalname); // Mantém o nome original do arquivo
  }
});

// Middleware do Multer
const upload = multer({ storage: storage });

// Rota para upload de arquivos
app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('Nenhum arquivo foi enviado.');
  }

  res.send('Arquivo enviado com sucesso: ' + req.file.originalname);
});

// Configuração do servidor HTTPS com certificado autoassinado
const httpsOptions = {
  key: fs.readFileSync('/usr/src/app/chave-privada.pem'),
  cert: fs.readFileSync('/usr/src/app/chave-publica.pem')
};

// Iniciando o servidor HTTPS
https.createServer(httpsOptions, app).listen(PORT, () => {
  console.log(`Servidor rodando em https://localhost:${PORT}`);
});
