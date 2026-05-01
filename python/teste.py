from mipsI import * #importa todas as funções do arquivo mipsI.py, onde estão as funções que convertem as instruções

#arquivo = input("Digite o nome do arquivo: ")

#por hora, usaremos um padrão, remover depois
arquivo = "asm_test_codes/mipsR.asm"

#aqui, abrimos o arquivo e atribuimos cada linha a um vetor, onde cada posição é uma linha do arquivo
with open(arquivo, "r") as f:
    conteudo = f.readlines() #cada linha do arquivo é um elemento do vetor conteudo

#para um teste, pegamos a linha 5 do arquivo, que é a primeira linha de código,
#e transformamos em um vetor de palavras, onde cada posição é uma palavra da linha
#a função lower() é usada para transformar todas as letras em minúsculas, para facilitar a comparação
#a função split() é usada para separar a linha em palavras, usando o espaço como separador

teste = conteudo[5].lower().split() #um vetor onde cada posição é uma palavra da linha 5 do arquivo
#conteudo[5] é "addi $t1, $zero, 4"
#nesse caso, teste[0] é "addi", teste[1] é "$t1,", teste[2] é "$zero," e teste[3] é "4"

#aqui, usamos a função globals() para chamar a função, nesse caso, addi
globals()[teste[0]](*teste[1:])
#os parâmetros da função são passados usando o operador *, que desempacota o vetor teste, ou seja,
#passa cada elemento do vetor como um parâmetro separado para a função addi
#nesse caso, a função addi é chamada com os parâmetros "$t1,", "$zero," e "4"