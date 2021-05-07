import pymysql
import time


def visualizar():
    conn = pymysql.connect(host="aulasegunda.mysql.uhserver.com",
                           user="convidado",
                           passwd="@FiCs2021",
                           db="aulasegunda")
    conexao = conn.cursor()
    conexao.execute("SELECT `id`,`pais`, `homens`, `mulheres` FROM `base_grupo06` ORDER BY pais ASC;")
    print ('=============Visualizar dados==============')
    for linha in (conexao.fetchall()):
        stringTexto = "id: {}, pais: {}, homens: {}, mulheres: {}"
        id = linha[0]
        pais = linha[1]
        ano = linha[2]
        nascimentos = linha[3]
        stringTexto = stringTexto.format(id, pais, ano, nascimentos)
        print(stringTexto)
        time.sleep(1.5)

    conn.close()
