# MIPS Assembler

## Autores

Máspoly Gênes de Morais Paiva Filho  
Ana Helena Alves Cosme

## Descrição

Este projeto consiste em um montador (assembler) para instruções MIPS desenvolvido em Python. O programa realiza a conversão de instruções Assembly MIPS para binário e hexadecimal, além de gerar estatísticas sobre as instruções utilizadas e calcular o CPI médio com base em uma tabela de ciclos.

O montador suporta instruções dos tipos R, I e J, incluindo tratamento de labels, comentários e diferentes formas de escrita das instruções.

---

## Estrutura do Projeto

```text
MIPS_ASSEMBLER/
│
├── src/
│   ├── montador.py
│   ├── mipsI.py
│   ├── mipsJ.py
│   ├── mipsR.py
│   ├── registradores.py
│   └── tabela_labels.py
│
├── ciclos.csv
├── README.md
└── arquivo.asm
```

---

## Requisitos

* Python 3

---

## Como Executar

O programa deve ser executado pelo terminal.

### Entrar na pasta do projeto

```bash
cd MIPS_ASSEMBLER
```

### Executar o montador

```bash
python src/montador.py arquivo.asm -b
```

ou

```bash
python src/montador.py arquivo.asm -h
```

---

## Modos de Saída

### Binário

```bash
python src/montador.py arquivo.asm -b
```

Gera um arquivo `.bin` contendo as instruções em binário.

### Hexadecimal

```bash
python src/montador.py arquivo.asm -h
```

Gera um arquivo `.hex` contendo as instruções em hexadecimal.

---

## Arquivos Gerados

Ao executar o programa:

* `arquivo.bin` → saída em binário
* `arquivo.hex` → saída em hexadecimal

O nome do arquivo gerado é baseado no nome do arquivo `.asm` utilizado na entrada.

---

## Funcionalidades

* Conversão de instruções MIPS para binário
* Conversão de instruções MIPS para hexadecimal
* Suporte a instruções dos tipos R, I e J
* Suporte a labels
* Tratamento de comentários
* Cálculo de CPI médio
* Contagem de instruções utilizadas

---

## Observações

* O programa utiliza endereço base `0x00400000` para cálculo dos labels.
* Comentários podem ser escritos utilizando `#`.
* O arquivo `ciclos.csv` é utilizado para cálculo do CPI médio.

---

## Exemplo

### Entrada

```asm
L1: add $1, $2, $3
addi $1, $2, 100
beq $1, $2, L1
```

### Execução

```bash
python src/montador.py exemplo.asm -b
```

### Saída

```text
00000000010000110000100000100000
00100000010000010000000001100100
00010000001000101111111111111101
```

---
