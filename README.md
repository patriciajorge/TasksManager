## TasksManager

Um gerenciador de tarefas simples baseado em linha de comando que utiliza um banco de dados SQLite para armazenar e gerenciar suas tarefas. Ele oferece uma interface de menu interativa, permitindo adicionar, visualizar, marcar como concluídas e remover tarefas.

## Funcionalidades

- Exibir Tarefas: Mostra todas as tarefas cadastradas, indicando se estão concluídas ou pendentes.
- Adicionar Tarefas: Permite ao usuário adicionar uma nova tarefa com uma descrição.
- Marcar Tarefas como Concluídas: Facilita a marcação de tarefas específicas como concluídas.
- Remover Tarefas: Permite a exclusão de tarefas da lista.
- Salvar Tarefas: As alterações e novas tarefas são salvas automaticamente no banco de dados SQLite, garantindo a persistência dos dados.

## Requisitos

- Python 3.x
- Bibliotecas Python: rich, sqlite3

## Configuração

1. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o script:
   ```bash
   python app.py
   ```
   
3. Se preferir, baixe e execute o executável `app.exe` que se encontra na tag
