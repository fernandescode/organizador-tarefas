# Organizador de Tarefas

Meu primeiro projeto desenvolvido em Python, com foco no aprendizado de programação, resolução de problemas e controle de versão com Git e GitHub.

O projeto consiste em um programa de terminal que permite gerenciar tarefas por meio de um menu interativo.

## Objetivo

Praticar os fundamentos da programação Python desenvolvendo uma aplicação funcional, com armazenamento persistente dos dados e versionamento do código.

## Funcionalidades

- **Adicionar tarefas:** cadastrar tarefas e impedir o registro de textos vazios.
- **Listar tarefas:** visualizar as tarefas cadastradas.
- **Excluir tarefas:** remover uma tarefa selecionada pelo número.
- **Editar tarefas:** alterar a descrição de uma tarefa existente.
- **Salvar tarefas:** manter os dados em um arquivo local chamado `tarefas.txt`.
- **Menu interativo:** acessar as funcionalidades e encerrar o programa.

## Tecnologias utilizadas

- Python 3
- Git
- GitHub
- Visual Studio Code
- Ubuntu no WSL2

## Como executar

Clone o repositório:

```bash
git clone https://github.com/fernandescode/organizador-tarefas.git
cd organizador-tarefas
```

Execute o programa:

```bash
python3 main.py
```

## Armazenamento dos dados

As tarefas são armazenadas localmente em `tarefas.txt`, na pasta do projeto.

O arquivo está listado no `.gitignore` para evitar sua inclusão acidental no repositório do GitHub.

## Conceitos de Python praticados

- Variáveis e tipos de dados.
- Entrada de dados com `input()`.
- Estruturas condicionais: `if`, `elif` e `else`.
- Laços de repetição: `while` e `for`.
- Listas, índices, `append()` e `len()`.
- Numeração com `enumerate()`.
- Tratamento de erros com `try` e `except`.
- Manipulação de arquivos com `open()`.
- Verificação de arquivos com `pathlib.Path`.
- Persistência de dados e menus interativos.

## Controle de versão

O Git é utilizado para registrar as alterações do projeto, enquanto o GitHub hospeda o repositório remoto.

O `.gitignore` exclui arquivos locais e arquivos gerados pelo Python do controle de versão.

## Status do projeto

Em desenvolvimento. Novas funcionalidades e melhorias serão implementadas conforme o aprendizado evoluir.

## Autor

Fernandes — estudante de programação e tecnologia.