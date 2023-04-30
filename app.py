from flask import Flask, request
import pyodbc


app = Flask(__name__)
SECRET_KEY='CRYP2023'

def conexao():
    # Variaveis de conexão
    DRIVERNAME = 'Teradata Database ODBC Driver 17.20'
    hostname = '192.168.15.4'
    uid = 'dbc'
    pwd = 'dbc'
    con = f"DRIVER={DRIVERNAME}; DBCNAME={hostname}; UID={uid};PWD={pwd}"

    # Iniciando conexão
    connect = pyodbc.connect(connect, autocommit=True)
    return connect


@app.route('/Pesquisar', methods=['GET'])
def pesquisar():
    nome = request.args.get('nome')
    sobrenome = request.args.get('sobrenome')
    turma = request.args.get('turma')

    aluno = []
    con = conexao()
    cursor = con.cursor()
    cursor.execute('SEL * FROM LAB_ESTUDOS.alunos')

    for row in cursor.fetchall():
        aluno.append({f"nome: {row[0]}, sobrenome: {row[1]}, turma: {row[2]}"})

    return aluno
    
  
@app.route('/cadastrar', methods=['POST'])
def inserir():
    nome = request.args.get('nome')
    sobrenome = request.args.get('sobrenome')
    turma = request.args.get('turma')
    
    query = f'INSERT INTO LAB_ESTUDOS.alunos VALUES ({nome}, {sobrenome}, {turma})'

    con = conexao()
    cursor = con.cursor()
    cursor.execute(query)
    cursor.close()

    return f'{nome}, {sobrenome}, {turma}'


@app.route('/Deletar', methods=['DELETE'])
def cadastro():
    nome = request.args.get('nome')
    sobrenome = request.args.get('sobrenome')
    turma = request.args.get('turma')

    query = f'DELETE FROM LAB_ESTUDOS.alunos WHERE nome= {nome} AND sobrenome = {sobrenome} AND turma = {turma})'

    con = conexao()
    cursor = con.cursor()
    cursor.execute(query)
    cursor.close()

    return f'{nome}, {sobrenome}, {turma}'


if __name__ == '__main__':
    app.run()