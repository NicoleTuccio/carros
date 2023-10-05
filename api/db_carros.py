import oracledb
import traceback


def recupera_carros():
    sql = "select id, ano, montadora, modelo, placa from carro" #or "select * from carro"
    try:
        with oracledb.connect(
            user="rm99711", password="290204", 
            dsn="oracle.fiap.com.br/orcl"
        ) as conexao:
            
            with conexao.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()

    except Exception as erro:
        traceback.print_exc()
        raise erro

def insert_carro(carro):
    ins = '''insert into carro(id, ano, montadora, modelo, placa)
            values(:id, :ano, :montadora, :modelo, :placa)'''
    try:
        with oracledb.connect(
            user="rm99711", password="290204", 
            dsn="oracle.fiap.com.br/orcl"
        ) as conexao:
            
            with conexao.cursor() as cur:
                cur.execute(ins, carro)
            conexao.commit()

    except Exception as erro:
        traceback.print_exc()
        raise erro

if __name__ == '__main__':
    c = {"id": 100, "montadora": "BMW", "modelo": "X5", 
         "ano": 2019, "placa": "BMV-4629"}
    insert_carro(c)    