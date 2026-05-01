#arquivo onde estão as funções que convertem as instruções do tipo R, como addi, lw, sw, etc

from registradores import * #importamos os registradores, para poder usar as funções que retornam o número do registrador


# ------------------ Função ADD ------------------
def add(dest, src1, src2):
    # DICA: O último argumento (src2) no Assembly geralmente não tem vírgula.
    # Usar o .replace() é um pouco mais seguro e limpo que cortar com [:-1],
    # pois funciona tendo a vírgula ali ou não!
    rd = dest.replace('$', '').replace(',', '')
    rs = src1.replace('$', '').replace(',', '')
    rt = src2.replace('$', '').replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 32 # Este é o código específico para a soma (add) no MIPS
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    print(opcode, end="")
    print(globals()[rs](), end="") 
    print(globals()[rt](), end="") 
    print(globals()[rd](), end="") 
    print(shamt, end="")
    print(funct)

# ------------------ Função ADDU ------------------
def addu(dest, src1, src2):
   
    rd = dest.replace('$', '').replace(',', '')
    rs = src1.replace('$', '').replace(',', '')
    rt = src2.replace('$', '').replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 33 # Este é o código específico para o addu
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    print(opcode, end="")
    print(globals()[rs](), end="") 
    print(globals()[rt](), end="") 
    print(globals()[rd](), end="") 
    print(shamt, end="")
    print(funct)

# ------------------ Função SUB ------------------
def sub(dest, src1, src2):
   
    rd = dest.replace('$', '').replace(',', '')
    rs = src1.replace('$', '').replace(',', '')
    rt = src2.replace('$', '').replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 34 # Este é o código específico para o sub
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    print(opcode, end="")
    print(globals()[rs](), end="") 
    print(globals()[rt](), end="") 
    print(globals()[rd](), end="") 
    print(shamt, end="")
    print(funct)

# ------------------ Função SUBU ------------------
def subu(dest, src1, src2):
   
    rd = dest.replace('$', '').replace(',', '')
    rs = src1.replace('$', '').replace(',', '')
    rt = src2.replace('$', '').replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 35 # Este é o código específico para o subu
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    print(opcode, end="")
    print(globals()[rs](), end="") 
    print(globals()[rt](), end="") 
    print(globals()[rd](), end="") 
    print(shamt, end="")
    print(funct)

# ------------------ Função AND ------------------
# Tive que mudar o nome para "And" pois estava dando erro quando deixava "and"
def And(dest, src1, src2):
   
    rd = dest.replace('$', '').replace(',', '')
    rs = src1.replace('$', '').replace(',', '')
    rt = src2.replace('$', '').replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 36 # Este é o código específico para o And
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    print(opcode, end="")
    print(globals()[rs](), end="") 
    print(globals()[rt](), end="") 
    print(globals()[rd](), end="") 
    print(shamt, end="")
    print(funct)

# ------------------ Função OR ------------------
# Tive que mudar o nome para "Or" pois estava dando erro quando deixava "or"
def Or(dest, src1, src2):
   
    rd = dest.replace('$', '').replace(',', '')
    rs = src1.replace('$', '').replace(',', '')
    rt = src2.replace('$', '').replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 37 # Este é o código específico para o Or
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    print(opcode, end="")
    print(globals()[rs](), end="") 
    print(globals()[rt](), end="") 
    print(globals()[rd](), end="") 
    print(shamt, end="")
    print(funct)

# ------------------ Função SLT ------------------
def slt(dest, src1, src2):
   
    rd = dest.replace('$', '').replace(',', '')
    rs = src1.replace('$', '').replace(',', '')
    rt = src2.replace('$', '').replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 42 # Este é o código específico para o slt
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    print(opcode, end="")
    print(globals()[rs](), end="") 
    print(globals()[rt](), end="") 
    print(globals()[rd](), end="") 
    print(shamt, end="")
    print(funct)

# ------------------ Função SLTU ------------------
def sltu(dest, src1, src2):
   
    rd = dest.replace('$', '').replace(',', '')
    rs = src1.replace('$', '').replace(',', '')
    rt = src2.replace('$', '').replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 43 # Este é o código específico para o sltu
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    print(opcode, end="")
    print(globals()[rs](), end="") 
    print(globals()[rt](), end="") 
    print(globals()[rd](), end="") 
    print(shamt, end="")
    print(funct)

# ------------------ Função MUL ------------------
def mul(dest, src1, src2):
   
    rd = dest.replace('$', '').replace(',', '')
    rs = src1.replace('$', '').replace(',', '')
    rt = src2.replace('$', '').replace(',', '')
    
    opcode = 28 # Única função que não tem o opcode como 0
    shamt = 0
    funct = 2 # Este é o código específico para o mul
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    print(opcode, end="")
    print(globals()[rs](), end="") 
    print(globals()[rt](), end="") 
    print(globals()[rd](), end="") 
    print(shamt, end="")
    print(funct)

# ------------------ Função SLL ------------------
def sll(dest, src1, src2):
   
    rd = dest.replace('$', '').replace(',', '')
    rs = src1.replace('$', '').replace(',', '')
    rt = src2.replace('$', '').replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 0 # Este é o código específico para o sll
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    print(opcode, end="")
    print(globals()[rs](), end="") 
    print(globals()[rt](), end="") 
    print(globals()[rd](), end="") 
    print(shamt, end="")
    print(funct)

# ------------------ Função SRL ------------------
def srl(dest, src1, src2):
   
    rd = dest.replace('$', '').replace(',', '')
    rs = src1.replace('$', '').replace(',', '')
    rt = src2.replace('$', '').replace(',', '')
    
    opcode = 0
    shamt = 0
    funct = 2 # Este é o código específico para o srl
    
    # Imprimimos sem pular linha, seguindo a ordem: opcode, rs, rt, rd, shamt, funct
    print(opcode, end="")
    print(globals()[rs](), end="") 
    print(globals()[rt](), end="") 
    print(globals()[rd](), end="") 
    print(shamt, end="")
    print(funct)

