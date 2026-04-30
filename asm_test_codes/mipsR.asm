# -------- R TYPE PURO --------

.text
main:
    # preparar valores
    addi $t1, $zero, 4
    addi $t2, $zero, 2

    # shift
    sll  $t0, $t1, 3
    srl  $t0, $t1, 1

    # aritmética
    add   $s0, $t1, $t2
    addu  $s1, $t1, $t2
    sub   $s2, $t1, $t2
    subu  $s3, $t1, $t2

    # lógica
    and   $s4, $t1, $t2
    or    $s5, $t1, $t2

    # comparação
    slt   $s6, $t1, $t2
    sltu  $s7, $t1, $t2

    # mult/div
    mult  $t1, $t2
    mflo  $t3
    mfhi  $t4

    multu $t1, $t2

    div   $t1, $t2
    mflo  $t5
    mfhi  $t6

    divu  $t1, $t2

    # mul
    mul   $t7, $t1, $t2

end:
    addi $v0, $zero, 10
    syscall