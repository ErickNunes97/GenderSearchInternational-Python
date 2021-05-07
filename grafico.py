import pymysql
import matplotlib.pyplot as plt
import numpy as np


def grafico():
    conn = pymysql.connect(host="aulasegunda.mysql.uhserver.com",
                           user="convidado",
                           passwd="@FiCs2021",
                           db="aulasegunda")
    conexao = conn.cursor()
    conexao.execute("SELECT `id`, `pais`, `homens`, `mulheres` FROM `base_grupo06` ORDER BY pais ASC; ")

    labels = []
    men_means = []
    women_means = []

    for linha in (conexao.fetchall()):
        labels.append(linha[1])
        men_means.append(linha[2])
        women_means.append(linha[3])

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, men_means, width, label='Homens')
    rects2 = ax.bar(x + width / 2, women_means, width, label='Mulheres')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    titulo = input(str("Digite o titutlo da pesquisa que será apresentada no gráfico:"))

    ax.set_ylabel('Quantdade')
    ax.set_title('Quantidade de Homens e Mulheres por País conforme a pesquisa realizada sobre: '+'\n'+titulo)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=2)
    ax.bar_label(rects2, padding=2)

    fig.tight_layout()

    plt.show()

    conn.close()
