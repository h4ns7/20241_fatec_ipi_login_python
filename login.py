import psycopg

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha


# verifica se o usuário rebebido existe na base
        
def existe(usuario):
    #abrir uma conexão com postgreSQL
    #obter uma abstração do tipo "cursor"
    #executar um comanda sql
    #verificar  resultado
    #devolver True ou False
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname= "20241_fatec_ipi_pbdi_login_python",
        user="postgres",
        password="123456"

    )   as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
            'SELECT * FROM tb_usuario WHERE login=%s AND senha =%s', 
            (usuario.login, usuario.senha)
            )
            result= cursor.fetchone()
            return result != None
    
def teste():
    print(existe(Usuario("admin","admin")))

teste()
