# Falcon Projeto Template
#### Este é um modelo de projeto em Falcon (Python) para APIs que sugere como estruturar os diretórios de forma organizada e separando as responsabilidades no sistema.

1. Estrutura de diretórios
    - Os diretórios são organizados separando o código por suas responsabilidades no sistema:
      - **`app/`**: Diretório responsável pelas rotas e controladores da API. 
        - Em `app/routes.py` devem ser concentradas todas as rotas do sistema e cada rota do sistema tem seu controlador definido nesta mesma pasta. Ex.: Um *controller* de usuário deve ficar em `app/usuario/views.py`, o arquivo `views.py` é inspirado na estrutura do framework Django, sugiro que cada `views.py` defina um rota única com os métodos HTTP (`GET`, `POST`, `PUT`, `DELETE` etc) definidos.
        - Ao lado de `views.py` deve ficar o `queries.py`, que define todas as consultas de SQL usadas em `views.py`.
      - **`core/`**: Diretório responsável por guardar o código responsável pela configuração e funcionamento do sistema, além de *utils*. 
        - Em `core/database/` ficam os arquivos de conexão aos bancos de dados do sistema, é possível definir mais de uma conexão como preferir. 
        - Em `core/decorator/` ficam os *decorators* do sistema, há dois predefinidos que auxiliam no gerenciamento de permissão do sistema (`allow_permission.py`) e na validação de campos obrigatórios da API (`required_fields.py`).
        - Em `core/exception/` ficam as exceções previstas do sistema, útil para levantar as exceções corretas invés de usar apenas a classe `Exception`.
        - Em `core/middleware/` ficam os *middlewares* do sistema, que são funções que interceptam as requisições e fazem tratamentos nelas. Há um *middleware* padrão que permite definir a autenticação e as regras de `CORS` em `auth.py`.
        - Em `core/utils` ficam as *utils* do sistema, funções estáticas que não dependem de outra parte do sistema e fazem um determinada procedimento apenas.
        - O arquivo `.env.example` deve ser copiado para `.env` e é usado para definir variáveis do sistema.
        - O arquivo `settings.py` define as configurações do sistema a partir das variáveis do `.env`.
        - O arquivo `response.py` define métodos que padronizam as repostas de requisições do sistema.
        - O arquivo `error_codes.py` define códigos de erros personalizados para o sistema.
        - O arquivo `app.py` inicia a API Falcon.
      - **`scripts/`**: Diretório responsável por guardar os scripts SQL necessários para recriar os banco de dados do sistema. Sugiro que seja versionado.
      - **`static/`**: Diretório responsável por guardar arquivos estáticos do sistema, como imagens, documentos etc.
      - **`requirements.txt`**: Define as bibliotecas do sistema, `Falcon` é obrigatória para o funcionamento deste projeto, as demais podem ser substituídas ou descartadas. `Gunicorn` é necessário para executar o sistema, mas pode ser substituído.