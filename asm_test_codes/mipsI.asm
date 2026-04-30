# -------- I TYPE --------

.data
mem: .word 0

.text
main:
    # valores
    addi  $t0, $zero, 5
    addi  $t1, $zero, 10

    # lógica imediata
    andi $t2, $t0, 3
    ori  $t3, $t1, 1

    # comparação
    slti  $t4, $t0, 10
    sltiu $t5, $t1, 20

    # carregar endereço
    lui $s0, 0x1001
    ori $s0, $s0, 0x0000

    # memória
    sw $t0, 0($s0)
    lw $t6, 0($s0)

    # branch
    beq $t0, $t1, label
    bne $t0, $t1, label

    j end

label:
    addi $t7, $zero, 1

end:
    addi $v0, $zero, 10
    syscall