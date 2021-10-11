# **Projeto Integrador 01 - UNIVESP**

Projeto Integrador da UNIVESP, do primeiro semestre do ano de 2021, equipe do polo de São Vicente.

Serão descritos todos os passos para a criação do projeto, 
incluindo detalhes de implementação backend e frontend.

Foi utilizado como base o tutorial presente no site do [Flask](https://flask.palletsprojects.com/en/2.0.x/tutorial/). 

## Preparação

Antes de tudo é necessário criar um ambiente virtual para isolar a aplicação.
Trata-se de uma medida de segurança para que configurações aplicadas neste projeto
não afetem outras aplicações presentes no seu computador.

#### [Virtualenv](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html)

Utilizaremos as seguintes dependências no projeto.

```
Flask==2.0.2
python-dotenv==0.19.1
```

Se você já souber criar e configurar seu ambiente virtual, pode pular este tópico.

Caso contrário, recomendo a utilização do [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/4.8.4/).
Para insalar digite `pip install virtualenvwrapper==4.8.4`.

Criando o ambiente (Caso tenha realizado o download do arquivo requirements.txt):

`mkvirtualenv -a <local-da-pasta-principal> -r <endereço-completo-do-requirements.txt> <nome-da-virtualenv>`

Sem o requirements.txt:

`mkvirtualenv -a <local-da-pasta-principal> <nome-da-virtualenv>`

Instalar as dependências indicadas anteriormente.


## Código da Aplicação

Após criarmos o ambiente virtual, iniciaremos passaremos a escrever os 
códigos necessários para funcionamento da aplicação.



## Teste da Aplicação Base

Para testar a aplicação é necessário indicar ao Flask a pasta da aplicação, antes de rodar o programa.

```
set FLASK_APP=concentra
set FLASK_ENV=development
flask run
```

