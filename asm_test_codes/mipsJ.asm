# -------- J TYPE PURO --------

.text
main:
    j destino

destino:
    jal func

    j fim

func:
    addi $t0, $zero, 42
    jr $ra

fim:
    addi $v0, $zero, 10
    syscall