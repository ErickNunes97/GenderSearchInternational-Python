import pymysql


def cadastrar():
    conn = pymysql.connect(host="aulasegunda.mysql.uhserver.com",
                           user="convidado",
                           passwd="@FiCs2021",
                           db="aulasegunda")
    conexao = conn.cursor()

    print("=================Cadastramento===================")
    pais = input(str("Digita a sigla do país (EUA, BR, JP, etc...: ")).upper()

    homens = int(input("Digite a quantidade de homens...: "))
    mulheres = int(input("Digite a quantidade de mulheres...: "))

    stringTexto = "('{}', '{}', '{}')"
    stringTexto = stringTexto.format(pais, homens, mulheres)

    conexao.execute("INSERT INTO base_grupo06(pais, homens, mulheres) " "VALUES " + stringTexto)
    conn.commit()
    conn.close()
