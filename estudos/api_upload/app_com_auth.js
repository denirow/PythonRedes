const express = require('express');
const multer = require('multer');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware para autenticação básica
const basicAuth = require('express-basic-auth');

// Usuário e senha para autenticação básica
const users = {
  'denirow': 'abc@123'
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
    cb(null, file.fieldname + '-' + Date.now() + path.extname(file.originalname));
  }
});

// Middleware do Multer
const upload = multer({ storage: storage });

// Rota para upload de arquivos
app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('Nenhum arquivo foi enviado.');
  }

  res.send('Arquivo enviado com sucesso: ' + req.file.filename);
});

// Iniciando o servidor
app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});