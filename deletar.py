import pymysql


def deletar():
    conn = pymysql.connect(host="aulasegunda.mysql.uhserver.com",
                           user="convidado",
                           passwd="@FiCs2021",
                           db="aulasegunda")
    conexao = conn.cursor()

    print('====================================Deletar================================================')
    id = int(input("ID: "))
    conexao.execute("DELETE FROM `base_grupo06` WHERE `base_erick`.`id` =" + str(id) + ";")
    conexao.execute("COMMIT;")
    print('ID do país deletado: ' + str(id) + ' Este país foi deletado da sua base de dados...')
    print('===========================================================================================')
    conn.close()
