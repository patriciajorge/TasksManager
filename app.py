from rich.console import Console
import sqlite3

# criar uma instância do Console para imprimir texto colorido e formatado
console = Console()

# conectar-se a um banco de dados (ou criar se não existir)
connection = sqlite3.connect('tasks.db')
# criar um cursor para interagir com o banco de dados
cursor = connection.cursor()

# criar tabela de tarefas no banco de dados, se não existir
def create_table_in_database():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            status TEXT NOT NULL
        );
    ''')
    connection.commit()

# criar lista de tarefas
tasks = []

def options_menu():
    # criar menu de opções
    width = 54
    title = "MENU DE OPÇÕES"
    
    console.print("═" * width, style="bold green")
    console.print(f"║{title.center(width - 2)}║", style="bold #d3046c")
    console.print("═" * width, style="bold green")
    
    # definir opções do menu
    options = [
        "[1] - Exibir todas as tarefas",
        "[2] - Adicionar uma nova tarefa com uma descrição",
        "[3] - Marcar uma tarefa específica como concluída",
        "[4] - Remover uma tarefa específica da lista",
        "[5] - Salvar a lista de tarefas",
        "[0] - Sair"
    ]
    
    # exibir cada opção no menu
    for option in options:
        console.print(f"║ {option.ljust(width - 4)} ║", style="#d3046c")
    
    console.print("═" * width, style="bold green")

def show_tasks():
    # buscar tarefas do banco de dados
    cursor.execute('SELECT * FROM Tasks')
    rows = cursor.fetchall()
    
    # mostrar tarefas na tela
    console.print('-'*54, style='yellow')
    console.print('Lista de Tarefas:', style='bold #ff69b4')
    for row in rows:
        status = ':white_check_mark: Concluída' if row[2] == 'concluida' else 'Pendente'
        console.print(f'{row[0]}. {row[1]} - {status}')
        console.print('⋯'*54, style='yellow')

def add_tasks_to_the_database():
    # adicionar uma nova tarefa na lista
    description = console.input('[bold white on purple]Escreva uma descrição para essa nova tarefa:[/] ')
    status = 'pendente'
    tasks.append({'descricao': description, 'concluida': False})
    console.print('Tarefa adicionada com sucesso!', style='bold green')
    
    cursor.execute('INSERT INTO Tasks (descricao, status) VALUES (?, ?)', (description, status))
    connection.commit()

def mark_task_as_done():
    # marcar uma tarefa como concluída
    show_tasks()
    index = int(console.input('[bold white on green]Digite o número da tarefa a ser marcada como concluída:[/] '))
    cursor.execute('UPDATE Tasks SET status = ? WHERE id = ?', ('concluida', index))
    connection.commit()
    console.print('Tarefa marcada como concluída!', style='bold green')

def delete_task():
    # remover uma tarefa da lista
    show_tasks()
    index = int(console.input('[bold white on red]Digite o número da tarefa que deseja excluir da lista:[/] '))
    cursor.execute('DELETE FROM Tasks WHERE id = ?', (index,))
    connection.commit()
    console.print('Tarefa excluída com sucesso!', style='bold green')

def save_tasks_to_the_database():
    # salvar tarefas no banco de dados (já implementado nas funções específicas)
    console.print('[bold green]Todas as tarefas/alterações já foram salvas no banco de dados, com o arquivo [yellow]"tasks.db"[/]')

def main():
    create_table_in_database()
    while True:
        # exibir menu de opções
        options_menu()
        choice = console.input("Escolha uma opção: ")

        # executar ação com base na escolha do usuário
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_tasks_to_the_database()
        elif choice == '3':
            mark_task_as_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks_to_the_database()
        elif choice == '0':
            break
        else:
            console.print("Opção inválida! Tente novamente.", style="bold red")

# ponto de entrada do programa
if __name__ == '__main__':
    main()
