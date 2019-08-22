import sys

def ano_bissexto(ano):
    return (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

if __name__ == "__main__":
    for indice, ano in enumerate(sys.argv):
        if indice!=0:
            e_ano_bissexto = ano_bissexto(int(ano))
            print("É ano bissexto" if e_ano_bissexto else "Não é ano bissexto")