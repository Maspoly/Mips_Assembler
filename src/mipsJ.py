from registradores import * #importamos os registradores, para poder usar as funções que retornam o número do registrador
from tabela_labels import Label #importamos a tabela de labels, para poder usar os endereços dos labels nas instruções de desvio

def J (label, linha_atual):
    op = format(2, '06b') #opcode
    address = Label.get_tabela_labels().get(label, 0) #pegamos o endereço do label na tabela de labels, usando o nome do label como chave
    address = address >> 2 #dividimos o endereço por 4, para obter o endereço em palavras, já que cada instrução tem 4 bytes
    address = format(int(address), '026b') #formatamos o endereço para 26
    return op + address #retornamos a instrução completa, concatenando os campos

def JAL(label, linha_atual):
    op = format(3, '06b') #opcode
    address = Label.get_tabela_labels().get(label, 0) #pegamos o endereço do label na tabela de labels, usando o nome do label como chave
    address = address >> 2 #dividimos o endereço por 4, para obter o endereço em palavras, já que cada instrução tem 4 bytes
    address = format(int(address), '026b') #formatamos o endereço para 26 bits
    return op + address #retornamos a instrução completa, concatenando os campos