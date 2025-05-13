# 🛡️ Projeto Sniffer + Página de Login

Este projeto tem dois componentes principais:

1. **Sniffer de pacotes** em Python: captura pacotes HTTP/TCP ou UDP, exibindo timestamp, IPs, portas e payload.  
2. **Página de login simples** em HTML + JS: envia usuário e senha para um servidor local via POST.

---

## 📌 Visão Geral do Projeto

- O **sniffer** monitora a rede local em busca de pacotes com dados relevantes.
- A **página de login** simula um formulário simples que envia dados para um servidor Python.
- Ideal para estudos de captura de pacotes, segurança e análise de rede local.

---

## ⚙️ Pré-requisitos e Instalação

### 🔹 Linguagem e Bibliotecas

- Python 3.8 ou superior
- Bibliotecas necessárias:
  - `scapy` (para o sniffer)
  - `http.server` (servidor embutido em Python)

### 🔹 Instalar dependências

```bash
pip install scapy
```

---

## 🐍 Como Executar o Sniffer

⚠️ É necessário rodar como **root** para acessar raw sockets.

### 🔸 Linux/macOS:

```bash
sudo python3 sniffer/sniffer.py
```

### 🔸 Windows (executar terminal como administrador):

```bash
python sniffer/sniffer.py
```

Você verá saídas como:

```
[2025-05-13 14:50:21] TCP 127.0.0.1:51500 -> 127.0.0.1:5000  
Payload: POST /login HTTP/1.1
```

---

## 🌐 Como Iniciar a Página de Login

1. Acesse a pasta `web/`  
2. Execute o servidor:

```bash
python3 -m http.server 8080
```

3. Acesse no navegador:

```
http://localhost:8080/index.html
```

4. Insira um login (ex: `admin` / `123`) e envie.

---

## 📩 Como Iniciar o Servidor que Recebe o Login

Rode o servidor Python que escuta os dados da página:

```bash
python3 sniffer/servidor.py
```

Ele estará escutando em:  
```
http://localhost:5000/login
```

Apenas aceita login com:

- **Usuário:** `admin`  
- **Senha:** `123`

---

## 🧪 Filtros Wireshark Recomendados

Se quiser visualizar o tráfego com Wireshark:

### 🔹 Capturar requisições POST:

```
tcp.port == 5000 && tcp contains "POST"
```

### 🔹 Apenas pacotes enviados para o servidor:

```
ip.dst == 127.0.0.1 && tcp.port == 5000
```

---

## 🧾 Exemplo de Saída Esperada

### 🔸 Sniffer

```
[2025-05-13 14:50:21] TCP 127.0.0.1:51500 -> 127.0.0.1:5000  
Payload:  
POST /login HTTP/1.1  
Host: localhost:5000  
Content-Type: application/x-www-form-urlencoded  
Content-Length: 29  

user=admin&password=123
```

### 🔸 Terminal do Servidor

```
Servidor rodando em http://localhost:5000  
Login recebido: usuário='admin', senha='123'
```

---