from flask import Flask, request,  jsonify
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
    connect = pyodbc.connect(con, autocommit=True)
    return connect


@app.route('/Pesquisar', methods=['GET'])
def pesquisar():
    nome = request.args.get('nome')
    sobrenome = request.args.get('sobrenome')
    turma = request.args.get('turma')

    query = f"SELECT * FROM LAB_ESTUDOS.alunos WHERE nome LIKE '{nome}' AND sobrenome LIKE '{sobrenome}' AND turma LIKE '{turma}';"
    con = conexao()
    cursor = con.cursor()
    cursor.execute(query)
    aluno = cursor.fetchall():
    cursor.close()
    return  jsonify(aluno)
    
  
@app.route('/cadastrar', methods=['POST'])
def inserir():
    nome = request.args.get('nome')
    sobrenome = request.args.get('sobrenome')
    turma = request.args.get('turma')
    query = f"INSERT INTO LAB_ESTUDOS.alunos VALUES ('{nome}', '{sobrenome}', '{turma}');"
    con = conexao()
    cursor = con.cursor()
    cursor.execute(query)
    cursor.close()

    return f'Registro | {nome} | {sobrenome} | {turma} | inserido com sucesso'


@app.route('/Deletar', methods=['DELETE'])
def cadastro():
    id = request.args.get('id')
    nome = request.args.get('nome')
    query = f"DELETE FROM LAB_ESTUDOS.alunos WHERE id = {id} AND nome LIKE '{nome}';"
    con = conexao()
    cursor = con.cursor()
    cursor.execute(query)
    cursor.close()

    return f'Registro | {id} | {nome} | deletado com sucesso'


if __name__ == '__main__':
    app.run()
