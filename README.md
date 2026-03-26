# Agendamento de Manutenção

## Descrição

Este é um aplicativo web desenvolvido em **Django 6.0.3** para gerenciamento de agendamentos de manutenção e informações de clientes. O projeto permite o cadastro de clientes com seus dados pessoais e endereços, servindo como base para um sistema de agendamento de serviços de manutenção.

O aplicativo está configurado para o idioma português brasileiro (pt-br) e fuso horário de São Paulo, desenvolvido por Felipe Hoffmann Viana sob a licença MIT.

## Funcionalidades

- **Cadastro de Clientes**: Formulário para registrar novos clientes com informações pessoais (nome, telefone, e-mail) e endereço completo (CEP, rua, número, bairro, cidade).
- **Interface Responsiva**: Utiliza Bootstrap 5.3.2 para uma experiência de usuário moderna e adaptável a dispositivos móveis.
- **Validação de Formulários**: Validação robusta no lado do servidor com Django Forms e Crispy Forms.
- **Administração**: Interface de administração do Django para gerenciamento de usuários e dados.
- **Estrutura Modular**: Organizado em apps Django (`client` e `core`) para facilitar a expansão futura.

## Tecnologias Utilizadas

| Camada | Tecnologia |
|--------|------------|
| **Backend** | Django 6.0.3, Python |
| **Banco de Dados** | SQLite |
| **Frontend** | HTML5, Bootstrap 5.3.2, Crispy Forms |
| **Autenticação** | Django Auth com modelo de usuário customizado |
| **Implantação** | WSGI/ASGI configurado |
| **Desenvolvimento** | manage.py, Git |

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd agendamento_manuntencao
   ```

2. **Crie um ambiente virtual** (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados**:
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário** (opcional, para acessar o admin):
   ```bash
   python manage.py createsuperuser
   ```

6. **Execute o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

7. **Acesse o aplicativo**:
   - Página principal: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/` (se criou superusuário)

## Uso

### Cadastro de Cliente
1. Acesse a página inicial do aplicativo.
2. Preencha o formulário com os dados do cliente:
   - **Dados do Cliente**: Nome, telefone e e-mail.
   - **Endereço**: CEP, rua, número, bairro e cidade (Rio Negro/PR ou Mafra/SC).
3. Clique em "Salvar Cadastro".
4. Após o sucesso, será redirecionado para a página de boas-vindas.

### Administração
- Acesse `/admin/` para gerenciar usuários e dados através da interface administrativa do Django.

## Estrutura do Projeto

```
agendamento_manuntencao/
├── config/                 # Configuração do projeto Django
│   ├── settings.py         # Configurações e apps instalados
│   ├── urls.py            # Roteamento principal de URLs
│   ├── wsgi.py            # Aplicação WSGI
│   └── asgi.py            # Aplicação ASGI
├── apps/
│   ├── client/            # App de gerenciamento de clientes
│   │   ├── models.py      # Modelos: User, Client, EnderecoClient
│   │   ├── views.py       # Views: ClientCreateView, index_
│   │   ├── forms.py       # Formulários: ClientForm, EnderecoForm
│   │   ├── urls.py        # Padrões de URL do app
│   │   ├── admin.py       # Configuração do admin
│   │   ├── templates/client/
│   │   │   ├── home.html
│   │   │   └── cadastro_cliente.html
│   │   └── migrations/
│   └── core/              # App principal (para expansão futura)
│       ├── models.py
│       ├── views.py
│       ├── admin.py
│       └── migrations/
├── templates/
│   └── base/
│       └── base.html      # Template base com Bootstrap
├── static/
│   └── js/
│       └── js.js         # Arquivo JavaScript (atualmente vazio)
├── db.sqlite3            # Banco de dados SQLite
├── manage.py             # Utilitário de gerenciamento Django
├── README.md
└── LICENSE              # Licença MIT
```

## Modelos de Dados

### Cliente (Client)
- **Nome**: Campo de texto (100 caracteres)
- **E-mail**: Campo de e-mail único
- **Telefone**: Campo de texto único (14 caracteres)
- **Endereço**: Relacionamento um-para-um com EnderecoClient

### Endereço do Cliente (EnderecoClient)
- **CEP**: Campo de texto (9 caracteres)
- **Rua**: Campo de texto (200 caracteres)
- **Número**: Campo de texto único (10 caracteres)
- **Bairro**: Campo de texto opcional (200 caracteres)
- **Cidade**: Escolha entre Rio Negro (PR) ou Mafra (SC)

## Desenvolvimento

### Executando Testes
```bash
python manage.py test
```

### Fazendo Migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### Configurações Adicionais
- O projeto utiliza um modelo de usuário customizado (`AUTH_USER_MODEL = 'client.User'`).
- Templates utilizam Crispy Forms com o pacote Bootstrap5.
- Configurado para desenvolvimento (DEBUG=True).

## Contribuição

1. Fork o projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Autor

**Felipe Hoffmann Viana**

---

*Nota: Este projeto está em desenvolvimento inicial. O app `core` está preparado para futuras funcionalidades de agendamento de manutenção.*
