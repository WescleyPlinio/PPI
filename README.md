# Repositório do projeto "Plataforma dos projetos integradores".
- A Plataforma dos Projetos Integradores se trata de um repositório. E seu principal objetivo é permitir o acesso público aos projetos desenvolvidos pelos alunos do IFRN campus São Paulo do Potengi.

## Alunos do terceiro ano do curso técnico integrado ao ensino médio em Informática Para Internet:
- Ellainy Nayara
- João Henrique
- Wescley Plínio

## Orientadoras:
- Pedrina Brasil
- Fernanda Lígia

## Para este sistema, serão usadas as seguintes Ferramentas:
- HTML, CSS e JavaScript
- Python e SQLite
- Bootstrap e Django

## Para rodar o sistema localmente, faça o seguinte:
- Faça as migrações do banco de dados e baixe projetos fictícios prontos:

python manage.py migrate

python manage.py loaddata ppi/fixtures/projetos.json

- Crie um super usuário para definir os grupos e permissões sempre que clonar o repositório. 

python manage.py createsuperuser

acesse o painel de administração pelo link:

127.0.0.1:8000/admin

por fim, na seção grupos/professores, dê todas as permissões do app ppi, clicando na seta entre as tabelas.

- Agora o sistema está pronto para ser acessado, aproveite!
