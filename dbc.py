# DATABASE CONTAINER 
import pyodbc


# CREATE LINK OF CONNECT 
DRIVERNAME = 'Teradata Database ODBC Driver 17.20'
hostname = '192.168.15.4'
uid = 'dbc'
pwd = 'dbc'

connect = f"DRIVER={DRIVERNAME}; DBCNAME={hostname}; UID={uid};PWD={pwd}"
try:
# CREATE CONNECTIONS                
    with pyodbc.connect(connect, autocommit=True) as connect:

        query = "CREATE SET TABLE LAB_ESTUDOS.alunos, FALLBACK, NO BEFORE JOURNAL, NO AFTER JOURNAL, CHECKSUM = DEFAULT, DEFAULT MERGEBLOCKRATIO, MAP = TD_MAP1 ( id INT GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1 MINVALUE 0 MAXVALUE 99999 NO CYCLE), nome VARCHAR(20) CHARACTER SET LATIN NOT CASESPECIFIC, sobrenome VARCHAR(20) CHARACTER SET LATIN NOT CASESPECIFIC, turma VARCHAR(20) CHARACTER SET LATIN NOT CASESPECIFIC) PRIMARY INDEX ( id, nome );"
        cursor = connect.cursor()
        cursor.execute(query)
        
except pyodbc.DatabaseError as Err:
        print(f"Conexão mal sucedida, {Err}")
        connect.rollback()
finally:
    cursor.close()
    connect.close()
    print('Conexão encerrada')

