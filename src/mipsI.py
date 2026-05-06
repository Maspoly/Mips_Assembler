#arquivo onde estão as funções que convertem as instruções do tipo I, como addi, lw, sw, etc

from registradores import * #importamos os registradores, para poder usar as funções que retornam o número do registrador
from tabela_labels import Label #importamos a tabela de labels, para poder usar os endereços dos labels nas instruções de desvio

BASE = 0x00400000

def ADDI(dest, src, imm, linha_atual):
    rt = dest.replace(',', '')
    rs = src.replace(',', '')
    imm = int(imm)
    #printamos separado com o end="", para não pular linha nem adicionar espaço entre os campos
    op = format(8, '06b') #opcode
    rs = get_registradores()[rs] #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    rs = format(rs, '05b') #formatamos o número do registrador
    rt = get_registradores()[rt] #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    rt = format(rt, '05b') #formatamos o número do registrador
    imm = format(imm & 0xFFFF, '016b') #immediate
    return op + rs + rt + imm #retornamos a instrução completa, concatenando os campos

def BEQ(src1, src2, label, linha_atual):
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    pc = linha_atual
    op = format(4, '06b') #opcode
    rs = get_registradores()[rs] #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    rs = format(rs, '05b') #formatamos o número do registrador
    rt = get_registradores()[rt] #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    rt = format(rt, '05b') #formatamos o número do registrador
    imm = Label.get_tabela_index_labels().get(label, 0) - pc #calculamos o immediate, que é a diferença entre o índice do label e o pc atual
    imm = format(imm & 0xFFFF, '016b') #immediate, usando o operador & para pegar apenas os 16 bits menos significativos, para evitar problemas com números negativos
    return op + rs + rt + imm  #retornamos a instrução completa, concatenando os campos

def BNE(src1, src2, label, linha_atual):
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    pc = linha_atual
    op = format(5, '06b') #opcode
    rs = get_registradores()[rs] #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    rs = format(rs, '05b') #formatamos o número do registrador
    rt = get_registradores()[rt] #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    rt = format(rt, '05b') #formatamos o número do registrador
    imm = Label.get_tabela_index_labels().get(label, 0) - pc #calculamos o immediate, que é a diferença entre o índice do label e o pc atual
    imm = format(imm & 0xFFFF, '016b') #immediate, usando o operador & para pegar apenas os 16 bits menos significativos, para evitar problemas com números negativos
    return op + rs + rt + imm #retornamos a instrução completa, concatenando os campos

def ADDIU(dest, src, imm, linha_atual):
    rt = dest.replace(',', '')
    rs = src.replace(',', '')
    imm = int(imm, 0) #convertemos o immediate para inteiro, usando a base 0 para permitir números hexadecimais
    op = format(9, '06b') #opcode
    rs = format(get_registradores()[rs], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    rt = format(get_registradores()[rt], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    imm = format(imm & 0xFFFF, '016b') #immediate, usando o operador & para pegar apenas os 16 bits menos significativos, para evitar problemas com números negativos
    return op + rs + rt + imm #retornamos a instrução completa, concatenando os campos

def SLTI(dest, src, imm, linha_atual):
    rt = dest.replace(',', '')
    rs = src.replace(',', '')
    imm = int(imm, 0) #convertemos o immediate para inteiro, usando a base 0 para permitir números hexadecimais
    op = format(10, '06b') #opcode
    rs = format(get_registradores()[rs], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    rt = format(get_registradores()[rt], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    imm = format(imm & 0xFFFF, '016b') #immediate, usando o operador & para pegar apenas os 16 bits menos significativos, para evitar problemas com números negativos
    return op + rs + rt + imm #retornamos a instrução completa, concatenando os campos

def SLTIU(dest, src, imm, linha_atual):
    rt = dest.replace(',', '')
    rs = src.replace(',', '')
    imm = int(imm, 0) #convertemos o immediate para inteiro, usando a base 0 para permitir números hexadecimais
    op = format(11, '06b') #opcode
    rs = format(get_registradores()[rs], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    rt = format(get_registradores()[rt], '05b')  #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    imm = (format(imm & 0xFFFF, '016b')) #immediate
    return op + rs + rt + imm #retornamos a instrução completa, concatenando os campos

def ANDI(dest, src, imm, linha_atual):
    rt = dest.replace(',', '')
    rs = src.replace(',', '')
    imm = int(imm, 0)
    op = format(12, '06b') #opcode
    rs = format(get_registradores()[rs], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    rt = format(get_registradores()[rt], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    imm = format(imm & 0xFFFF, '016b') #immediate
    return op + rs + rt + imm #retornamos a instrução completa, concatenando os campos

def ANDIU(dest, src, imm, linha_atual):
    rt = dest.replace(',', '')
    rs = src.replace(',', '')
    imm = int(imm, 0) #convertemos o immediate para inteiro, usando a base 0 para permitir números hexadecimais
    op = format(12, '06b') #opcode
    rs = format(get_registradores()[rs], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    rt = format(get_registradores()[rt], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    imm = format(imm & 0xFFFF, '016b') #immediate
    return op + rs + rt + imm #retornamos a instrução completa, concatenando os campos

def ORI(dest, src, imm, linha_atual):
    rt = dest.replace(',', '')
    rs = src.replace(',', '')
    imm = int(imm, 0) #convertemos o immediate para inteiro, usando a base 0 para permitir números hexadecimais
    op = format(13, '06b') #opcode
    rs = format(get_registradores()[rs], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    rt = format(get_registradores()[rt], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    imm = format(imm & 0xFFFF, '016b') #immediate
    return op + rs + rt + imm #retornamos a instrução completa, concatenando os campos

def LUI(dest, imm, linha_atual):
    rt = dest.replace(',', '')
    imm = int(imm, 0) #convertemos o immediate para inteiro, usando a base 0 para permitir números hexadecimais
    op = format(15, '06b') #opcode
    rs = format(0, '05b') #rs é 0 para a instrução lui
    rt = format(get_registradores()[rt], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    imm = format(imm & 0xFFFF, '016b') #immediate
    return op + rs + rt + imm #retornamos a instrução completa, concatenando os campos

def LW(dest, offset_base, registro_base, linha_atual):
    rt = dest.replace(',', '')
    rs = registro_base.replace(',', '')
    #offset_base é do formato "offset(base)", onde offset é um número inteiro, e base é um registrador
    imm = int(offset_base, 0)
    op = format(35, '06b') #opcode
    rs = format(get_registradores()[rs], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    rt = format(get_registradores()[rt], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    imm = format(imm & 0xFFFF, '016b') #immediate
    return op + rs + rt + imm #retornamos a instrução completa, concatenando os campos

def SW(src, offset_base, registro_base, linha_atual):
    rt = src.replace(',', '')
    rs = registro_base.replace(',', '')
    imm = int(offset_base, 0)
    op = format(43, '06b') #opcode
    rs = format(get_registradores()[rs], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    rt = format(get_registradores()[rt], '05b') #chamamos a função get_registradores(), passando o nome do registrador, retornando o número do registrador
    imm = format(imm & 0xFFFF, '016b') #immediate
    return op + rs + rt + imm #retornamos a instrução completa, concatenando os campos