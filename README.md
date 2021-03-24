# Python Brasil: Validação de dados no padrão nacional

👋 Olá, Seja Bem-vindo(a) ao 'Python Brasil: Validação de dados no padrão nacional'.

# Projeto ['Python Brasil: Validação de dados no padrão nacional'](https://cursos.alura.com.br/course/python-collections-conjuntos-e-dicionarios):

### Aulas

<details>
    <summary>Validando CPF e acessando o PYPI</summary>
    <ul>
        <li>Introdução<li>
        <li>Validando um CPF<li>
        <li>Pacotes Python<li>
        <li>Utilizando um pacote<li>
        <li>Entendendo a validação<li>
        <li>Para saber mais<li>
        <li>Faça como eu fiz na aula<li>
        <li>O que aprendemos?<li>
    </ul>
</details>

<details>
    <summary>Validando CNPJ e construindo uma Factory</summary>
    <ul>
        <li>Validando CNPJ</li>
        <li>Máscara para CNPJ</li>
        <li>Refatorando o código</li>
        <li>Para saber mais</li>
        <li>Mais sobre Factories</li>
        <li>Faça como eu fiz na aula</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Validando telefones com expressões regulares</summary>
    <ul>
        <li>Resumo Regex</li>
        <li>Definindo padrão para Telefones</li>
        <li>Criando Máscara para o numero de telefone</li>
        <li>Fixando as regex</li>
        <li>Analisando regex</li>
        <li>Faça como eu fiz na aula</li>
        <li>O que aprendemos?</li>
    </ul>
</details>
<details>
    <summary>Manipulando e formatando datas</summary>
    <ul>
        <li>Datas no Python</li>
        <li>Formatando Datas</li>
        <li>Diferença entre datas e timedelta</li>
        <li>Relembrando strftime</li>
        <li>Um pouco mais sobre datetime</li>
        <li>Faça como eu fiz na aula</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Trabalhando com CEP e acessando uma API</summary>
    <ul>
        <li>Introducao APIs e validação de CEP</li>
        <li>Acessando APIs com Python</li>
        <li>Respostas API Via CEP</li>
        <li>Conclusão</li>
        <li>Mais sobre APIs</li>
        <li>Treinando requests</li>
        <li>Fazendo uma requisição</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

# Notas das aulas:

Para executar um script python, faça conforme o exemplo abaixo:
```sh
docker-compose run --rm app python aulas/01.py
```

## Sobre o projeto:

### Permissões de arquivos:

Ao se criar migrações, adicionar libs ou qualquer outro comando que crie arquivos dentro do contâiner Docker o proprietário para edição se torna o contâiner, sendo assim você precisará rodar o comando abaixo para alterar essas permissões e você poder editar:

```sh
sudo chown -R $USER:$USER .
```

# Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)

# Instalando

## 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

Para acessar o container da aplicação, execute:

```sh
docker-compose run --rm app bash
```

Para derrubar e subir a instância do docker novamente, execute:

```sh
docker-compose down && docker-compose up
```

# Referências utilizadas

[1° Conteinerização de scripts em Python](https://github.com/claudimf/containerized_python)

[2° Algoritmo para Validar CPF](https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/)

[3° Pacote Python para validação de documentos brasileiros](https://pypi.org/project/validate-docbr/)

[4° Factory Method](https://pt.wikipedia.org/wiki/Factory_Method)

[5° Padrão de Projeto: Factory Method](https://www.thiengo.com.br/padrao-de-projeto-factory-method)

[6° Factory Method Design Pattern](https://sourcemaking.com/design_patterns/factory_method)

[7° Factory: Encapsulating Object Creation](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html)