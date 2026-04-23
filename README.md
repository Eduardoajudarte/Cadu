# Cadu — Bot Discord 🤖

Bot Discord simples em Python que responde a comandos de apresentação pessoal.

## 📦 Pré-requisitos

- Python 3.8 ou superior
- Uma conta no [Discord Developer Portal](https://discord.com/developers/applications) com um bot criado e seu token em mãos

## 🚀 Instalação passo a passo

### 1. Clone o repositório (ou abra no CodeSpace)

```bash
git clone https://github.com/Eduardoajudarte/Cadu.git
cd Cadu
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure o arquivo `.env`

Copie o arquivo de exemplo e adicione o seu token:

```bash
cp .env.example .env
```

Abra o arquivo `.env` e substitua o placeholder pelo seu token real:

```
DISCORD_TOKEN=seu_token_aqui
```

> ⚠️ **Nunca** compartilhe seu token nem faça commit do arquivo `.env`!  
> O `.gitignore` já está configurado para protegê-lo.

### 4. Execute o bot

```bash
python bot.py
```

Se tudo estiver certo, você verá no terminal:

```
✅ Bot conectado com sucesso como Cadu#1234
```

## 🕹️ Comandos disponíveis

| Comando       | Descrição                                      |
|---------------|------------------------------------------------|
| `!apresenta`  | O bot se apresenta com um embed formatado      |
| `!ping`       | Mostra a latência atual do bot em milissegundos|
| `!ajuda`      | Lista todos os comandos disponíveis            |

## 💡 Exemplos de uso

```
Você: !apresenta
Cadu: [embed com nome, criador e prefixo de comandos]

Você: !ping
Cadu: 🏓 Pong! Latência: 42ms

Você: !ajuda
Cadu: [embed com a lista de todos os comandos]
```

## 📁 Estrutura do projeto

```
Cadu/
├── bot.py           # Arquivo principal do bot
├── requirements.txt # Dependências Python
├── .env.example     # Template do arquivo de variáveis de ambiente
├── .env             # Seu token (NÃO commitar — protegido pelo .gitignore)
├── .gitignore       # Arquivos ignorados pelo Git
└── README.md        # Esta documentação
```
