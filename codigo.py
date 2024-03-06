import pandas as pd

if __name__ == '__main__':
    tables = pd.read_html("file:///C:/Users/Jo%C3%A3o%20Vittor/OneDrive/Documentos/VS%20s/DEVWEB1/index.html")

    tb = tables[0]
    tb.columns = ['codigo', 'nome', 'professor', 'notas', 'faltas']
    tb_grouped = tb.groupby('codigo')

    print(tb)

    index_materia_mais_misses = tb_grouped["faltas"].sum().idxmax()
    print("Disciplina com mais faltas: " + tb.at[index_materia_mais_misses, 'nome'])

    print("Média de Notas: " + str(tb["notas"].mean()))

    professor_mais_disciplinas = tb['professor'].value_counts().idxmax()
    print("Professor com mais disciplinas: " + professor_mais_disciplinas)

    ordenado_por_falta_crescente = tb.sort_values(by=['professor', 'faltas'], ascending=[True, True])
    print(ordenado_por_falta_crescente)
