#arquivo onde estão as funções que convertem as instruções do tipo I, como addi, lw, sw, etc

from registradores import * #importamos os registradores, para poder usar as funções que retornam o número do registrador

def addi(dest, src, imm):
    #removemos os caracteres '$' e ',' dos registradores, para facilitar a conversão
    #[1:] remove o primeiro caractere, que é '$', e [:-1] remove o último caractere, que é ','
    rt = dest[1:]; rt = rt[:-1]
    rs = src[1:]; rs = rs[:-1]
    imm = int(imm)
    #printamos separado com o end="", para não pular linha nem adicionar espaço entre os campos
    print(8, end="") #opcode
    print(globals()[rs](), end="") #chamamos a função com o globals(), passando o nome do resgitradaor, retornando o número do registrador
    print(globals()[rt](), end="") #chamamos a função com o globals(), passando o nome do resgitradaor, retornando o número do registrador
    print(imm) #immediate