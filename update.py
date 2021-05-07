import pymysql


def atualizar():
    conn = pymysql.connect(host="aulasegunda.mysql.uhserver.com",
                           user="convidado",
                           passwd="@FiCs2021",
                           db="aulasegunda")
    conexao = conn.cursor()

    print("========================Atualizar===========================")
    id = int(input("ID: "))
    pais = input(str("Digita a sigla do país (EUA, BR, JP, etc...: ")).upper()

    homens = int(input("Digite a quantidade de homens...: "))
    mulheres = int(input("Digite a quantidade de mulheres...: "))

    stringTexto = "`homens` = {}, `mulheres` = {}, `pais` = '{}' WHERE `id` = {};"
    stringTexto = stringTexto.format(homens, mulheres, pais, id)
    conexao.execute("UPDATE `base_grupo06` SET " + stringTexto)
    conexao.execute("COMMIT;")
    conn.close()
