#arquivo onde estão as funções que convertem as instruções do tipo R, como addi, lw, sw, etc

from registradores import * #importamos os registradores, para poder usar as funções que retornam o número do registrador


# ------------------ Função ADD ------------------
def ADD(dest, src1, src2, linha_atual):
    rd = dest.replace(',', '')
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 32 # Este é o código específico para a soma (add) no MIPS
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(get_registradores()[rs], '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(get_registradores()[rd], '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função ADDU ------------------
def ADDU(dest, src1, src2, linha_atual):
   
    rd = dest.replace(',', '')
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 33 # Este é o código específico para o addu
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(get_registradores()[rs], '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(get_registradores()[rd], '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função SUB ------------------
def SUB(dest, src1, src2, linha_atual):
   
    rd = dest.replace(',', '')
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 34 # Este é o código específico para o sub
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(get_registradores()[rs], '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(get_registradores()[rd], '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função SUBU ------------------
def SUBU(dest, src1, src2, linha_atual):
   
    rd = dest.replace(',', '')
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 35 # Este é o código específico para o subu
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(get_registradores()[rs], '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(get_registradores()[rd], '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função AND ------------------
# Tive que mudar o nome para "And" pois estava dando erro quando deixava "and"
def AND(dest, src1, src2, linha_atual):
   
    rd = dest.replace(',', '')
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 36 # Este é o código específico para o And
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(get_registradores()[rs], '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(get_registradores()[rd], '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função OR ------------------
# Tive que mudar o nome para "Or" pois estava dando erro quando deixava "or"
def OR(dest, src1, src2, linha_atual):
   
    rd = dest.replace(',', '')
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 37 # Este é o código específico para o Or
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(get_registradores()[rs], '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(get_registradores()[rd], '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função SLT ------------------
def SLT(dest, src1, src2, linha_atual):
   
    rd = dest.replace(',', '')
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 42 # Este é o código específico para o slt
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(get_registradores()[rs], '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(get_registradores()[rd], '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função SLTU ------------------
def SLTU(dest, src1, src2, linha_atual):
   
    rd = dest.replace(',', '')
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 43 # Este é o código específico para o sltu
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(get_registradores()[rs], '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(get_registradores()[rd], '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função MUL ------------------
def MUL(dest, src1, src2, linha_atual):
   
    rd = dest.replace(',', '')
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    
    opcode = 28 # Única função que não tem o opcode como 0
    shamt = 0
    funct = 2 # Este é o código específico para o mul
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(get_registradores()[rs], '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(get_registradores()[rd], '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função SLL ------------------
def SLL(dest, src1, src2, linha_atual):
   
    rd = dest.replace(',', '')
    rt = src1.replace(',', '')
    
    opcode = 0
    rs = 0
    shamt = int(src2.replace(',', ''))
    funct = 0 # Este é o código específico para o sll
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(rs, '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(get_registradores()[rd], '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função SRL ------------------
def SRL(dest, src1, src2, linha_atual):
   
    rd = dest.replace(',', '')
    rt = src1.replace(',', '')
    
    opcode = 0
    rs = 0
    shamt = int(src2.replace(',', ''))
    funct = 2 # Este é o código específico para o srl
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(rs, '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(get_registradores()[rd], '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função JR ------------------
def JR(src, linha_atual):
    rs = src.replace(',', '')
    
    opcode = 0
    rt = 0
    rd = 0
    shamt = 0
    funct = 8 # Este é o código específico para o jr
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(get_registradores()[rs], '05b')
    rt = format(rt, '05b')
    rd = format(rd, '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função MFHI ------------------
def MFHI(dest, linha_atual):
    rd = dest.replace(',', '')
    
    opcode = 0
    rs = 0
    rt = 0
    shamt = 0
    funct = 16 # Este é o código específico para o mfhi
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(rs, '05b')
    rt = format(rt, '05b')
    rd = format(get_registradores()[rd], '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função MFLO ------------------
def MFLO(dest, linha_atual):
    rd = dest.replace(',', '')
    
    opcode = 0
    rs = 0
    rt = 0
    shamt = 0
    funct = 18 # Este é o código específico para o mflo
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(rs, '05b')
    rt = format(rt, '05b')
    rd = format(get_registradores()[rd], '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função MULT ------------------
def MULT(src1, src2, linha_atual):
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    
    opcode = 0
    rd = 0
    shamt = 0
    funct = 24 # Este é o código específico para o mult
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(get_registradores()[rs], '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(rd, '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função MULTU ------------------
def MULTU(src1, src2, linha_atual):
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    
    opcode = 0
    rd = 0
    shamt = 0
    funct = 25 # Este é o código específico para o multu
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(get_registradores()[rs], '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(rd, '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função DIV ------------------
def DIV(src1, src2, linha_atual):
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    
    opcode = 0
    rd = 0
    shamt = 0
    funct = 26 # Este é o código específico para o div
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(get_registradores()[rs], '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(rd, '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct

# ------------------ Função DIVU ------------------
def DIVU(src1, src2, linha_atual):
    rs = src1.replace(',', '')
    rt = src2.replace(',', '')
    
    opcode = 0
    rd = 0
    shamt = 0
    funct = 27 # Este é o código específico para o divu
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    op = format(opcode, '06b')
    rs = format(get_registradores()[rs], '05b')
    rt = format(get_registradores()[rt], '05b')
    rd = format(rd, '05b')
    shamt = format(shamt, '05b')
    funct = format(funct, '06b')
    return op + rs + rt + rd + shamt + funct