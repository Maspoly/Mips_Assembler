import sys
import os

from mipsI import * #importa todas as funções do arquivo mipsI.py, onde estão as funções que convertem as instruções
from tabela_labels import Label #importa a classe Label do arquivo tabela_labels.py
from mipsR import * #importa todas as funções do arquivo mipsR.py, onde estão as funções que convertem as instruções do tipo R
from mipsJ import * #importa todas as funções do arquivo mipsJ.py, onde estão as funções que convertem as instruções do tipo J

BASE = 0x00400000 #endereço base das "linhas de código", onde as instruções serão armazenadas

def ler_csv_ciclos(caminho):
    tabela = {}

    with open(caminho, "r") as f:
        linhas = f.readlines()

        for linha in linhas[1:]:  # pula cabeçalho
            #divide a linha com a virgula
            instr, ciclos = linha.strip().split(",")
            tabela[instr.lower()] = int(ciclos)

    return tabela

def calcular_cpi(contagem, tabela_ciclos):
    total_instr = sum(contagem.values())

    if total_instr == 0:
        return 0

    soma = 0

    for instr, qtd in contagem.items():
        ciclos = tabela_ciclos.get(instr, 1)
        soma += qtd * ciclos

    return soma / total_instr

binario_convertido = [] #vetor onde serão armazenados os binários convertidos, para facilitar a escrita no arquivo de saída
#arquivo = input("Digite o nome do arquivo: ")

contagem = {}

def ler_csv_ciclos(caminho):
    tabela = {}

    with open(caminho, "r") as f:
        linhas = f.readlines()

        for linha in linhas[1:]:  # pula cabeçalho
            #divide a linha com a virgula
            instr, ciclos = linha.strip().split(",")
            tabela[instr.lower()] = int(ciclos)

    return tabela

def calcular_cpi(contagem, tabela_ciclos):
    total_instr = sum(contagem.values())

    if total_instr == 0:
        return 0

    soma = 0

    for instr, qtd in contagem.items():
        ciclos = tabela_ciclos.get(instr, 1)
        soma += qtd * ciclos

    return soma / total_instr

#lê o comando do usuário, onde ele deve digitar o nome do arquivo e o modo de saída (binário ou hexadecimal)
partes = sys.argv[1:]

if len(partes) < 2:
    print("Entrada inválida!")
    sys.exit(1)

arquivo = partes[0] #parte[0] é o nome do arquivo
modo = partes[1] if len(partes) >= 2 else "-b"
#parte[0] é o nome do programa, parte[1] é o nome do arquivo, parte[2] é o modo de saída (opcional, padrão é -b)

Label.gerar_tabela_labels(arquivo) #geramos a tabela de labels, passando o nome do arquivo como parâmetro

#aqui, abrimos o arquivo e atribuimos cada linha a um vetor, onde cada posição é uma linha do arquivo
with open(arquivo, "r") as f:
    conteudo = f.readlines() #cada linha do arquivo é um elemento do vetor conteudo

#a função lower() e upper() são usadas para transformar todas as letras em minúsculas, para facilitar a comparação
#a função split() é usada para separar a linha em palavras, usando o espaço como separador

op = 0 #variável para controlar a linha atual, para calcular o endereço do label

for linha in conteudo:
    linha = linha.strip() #remove os espaços em branco no início e no final da linha, para facilitar a comparação
    
    if linha != "" and linha[0] != "#":#se a linha não for vazia e não for um comentário
        linha = linha.split("#")[0] #remove o comentário
        if ":" in linha: #se a linha tiver um ":", ou seja, se for um label
            importante = linha.split(":")[1] #o label é a parte da linha antes do ":"
            importante = importante.strip() #remove os espaços em branco no início e no final da linha, para facilitar a comparação
            if importante != "": #se a parte da linha depois do ":" não for vazia, ou seja, se tiver uma instrução depois do label
                op += 1 #incrementamos a variável op, para calcular o endereço do label
                linha = linha.replace(",", " ") #remove as vírgulas, para facilitar a comparação
                linha = linha.replace("(", " ") #remove os parênteses, para facilitar a comparação
                linha = linha.replace(")", " ") #remove os parênteses, para facilitar a comparação
                linha = importante.split() #um vetor onde cada posição é uma palavra da linha,
                #aqui, usamos a função globals() para chamar a função
                #os parâmetros da função são passados usando o operador *, que desempacota o vetor linha, ou seja,
                resultado = globals()[linha[0].upper()]( *linha[1:], op)
                binario_convertido.append(resultado)
                # aqui, fazemos a contagem de cada instrução, para gerar o relatório de contagem no final do programa
                instrucao = linha[0].lower()
                if instrucao in contagem:
                    contagem[instrucao] += 1
                else:
                    contagem[instrucao] = 1
        else:
            op += 1 #incrementamos a variável op, para calcular o endereço do label
            linha = linha.replace(",", " ") #remove as vírgulas, para facilitar a comparação
            linha = linha.replace("(", " ") #remove os parênteses, para facilitar a comparação
            linha = linha.replace(")", " ") #remove os parênteses, para facilitar a
            linha = linha.split() #um vetor onde cada posição é uma palavra da linha
            #aqui, usamos a função globals() para chamar a função
            resultado = globals()[linha[0].upper()]( *linha[1:], op)
            binario_convertido.append(resultado)
            instrucao = linha[0].lower()
            if instrucao in contagem:
                contagem[instrucao] += 1
            else:
                contagem[instrucao] = 1

# cria nome do arquivo de saída baseado no .asm
saida_base = os.path.splitext(arquivo)[0]

if modo == "-b":
    #escreve o arquivo .bin, onde cada linha é uma instrução em binário
    with open(saida_base + ".bin", "w") as f:
        for instr in binario_convertido:
            f.write(instr + "\n") #não necessário converter, pois as funções já retornam o binário como string


elif modo == "-h":
    #escreve o arquivo .hex, onde cada linha é uma instrução em hexadecimal, convertida a partir do binário
    with open(saida_base + ".hex", "w") as f:
        f.write("v2.0 raw\n")
        # aqui, convertemos binário para hexadecimal, com 8 dígitos
        for instr in binario_convertido:
            valor_hex = format(int(instr, 2), "08x") #tudo que vem à esquerda, será zero
            f.write(valor_hex + "\n")


# printa quantidades de cada tipo de instrução
print("\nQuantidades por tipo de instruções:")
for instr, qtd in contagem.items():
    print(f"{instr}: {qtd}")

tabela_ciclos = ler_csv_ciclos("ciclos.csv")

cpi = calcular_cpi(contagem, tabela_ciclos)

print(f"\nCPI médio: {cpi:.2f}")

