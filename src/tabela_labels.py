
class Label:
    #atributo estático, onde serão armazenados os labels e seus respectivos endereços de memória
    line_index = 0 #variável para armazenar o índice da linha atual, para calcular o endereço do label
    tabela_labels = {} #tabela_labels, onde serão armazenados os labels e seus respectivos endereços de memória
    tabela_index_labels = {} #tabela_index_labels, onde serão armazenados os labels e seus respectivos índices, o número da linha onde o label está localizado
    def this_label(linha_atual, linha, conteudo, BASE) -> str: #função para retornar o label da linha atual
        linha = linha.strip() #remove os espaços em branco no início e no final da linha, para facilitar a comparação
        linha = linha.split("#")[0] #remove o comentário, para facilitar a comparação
        linha = linha.strip() #remove os espaços em branco no início e no final da linha, para facilitar a comparação
        if ":" in linha: #se a linha tiver um ":", ou seja, se for um label
            label = linha.split(":") #o label é a parte da linha antes do ":"
            if label[1]: #se a parte da linha depois do ":" não for vazia, ou seja, se tiver uma instrução depois do label
                label = label[0].strip() #remove os espaços em branco no início e no final da linha, para facilitar a comparação
                label_address = BASE + Label.line_index * 4
                label_index = Label.line_index #armazenamos o índice do label
                Label.line_index += 1
                return label, label_address, label_index
            else: #se a parte da linha depois do ":" for vazia, ou seja, se não tiver uma instrução depois do label
                if linha_atual + 1 < len(conteudo): #se a próxima linha existir, para evitar um erro de índice
                    next_line = conteudo[linha_atual + 1].split("#")[0].strip() #próxima linha, sem comentário e sem espaços em branco no início e no final da linha
                    if ":" in next_line: #se a próxima linha também tiver um ":", ou seja, se tiver outro label
                        label = label[0].strip() #remove os espaços em branco no início e no final da linha, para facilitar a comparação
                        #chamamos a função recursivamente para pegar o endereço do próximo label, que é o endereço do label atual
                        line_index_atual = Label.line_index #armazenamos o índice da linha atual, para calcular o endereço do label
                        lixo, label_address, label_index = Label.this_label(linha_atual + 1, conteudo[linha_atual + 1], conteudo, BASE)
                        Label.line_index = line_index_atual #retornamos o índice da linha atual, para calcular o endereço do próximo label
                        return label, label_address, label_index
                    else: #se a próxima linha não tiver um ":", ou seja, se não tiver label
                        label = label[0].strip() #remove os espaços em branco no início e no final da linha, para facilitar a comparação
                        label_address = BASE + (Label.line_index) * 4
                        label_index = Label.line_index #armazenamos o índice do label
                        return label, label_address, label_index
                else: 
                    label = label[0].strip() #remove os espaços em branco no início e no final da linha, para facilitar a comparação
                    label_address = BASE + (Label.line_index) * 4
                    label_index = Label.line_index #armazenamos o índice do label
                    Label.line_index += 1
                    return label, label_address, label_index
        elif linha != "" and linha[0] != "#": #se a linha não for vazia e não for um comentário, ou seja, se for uma instrução
            Label.line_index += 1 #incrementamos o índice da linha, para calcular o endereço do label
            return None, None, None #retorna None, para indicar que não é um label
        else: #se a linha for vazia ou for um comentário, ou seja, se não for uma instrução
            return None, None, None #retorna None, para indicar que não é um label
    @staticmethod #função estática, para poder chamar a função sem precisar criar um objeto da classe Label
    def gerar_tabela_labels(arquivo):
        Label.line_index = 0
        Label.tabela_labels = {}
        Label.tabela_index_labels = {}
        tabela = {} #tabela_labels, onde serão armazenados os labels e seus respectivos endereços de memória
        BASE = 0x00400000 #endereço base das "linhas de código", onde as instruções serão armazenadas

        with open(arquivo, "r") as f:
            conteudo = f.readlines() #cada linha do arquivo é um elemento do vetor conteudo
        
        for linha_atual, linha in enumerate(conteudo):
            linha = linha.strip() #remove os espaços em branco no início e no final da linha, para facilitar a comparação
            label, label_address, label_index = Label.this_label(linha_atual, linha, conteudo, BASE)
            if label: #se a linha for um label, ou seja, se a função this_label retornar um label válido
                tabela[label] = label_address #armazenamos o endereço do label, usando o próprio label como chave, para facilitar a comparação
                Label.tabela_index_labels[label] = label_index #armazenamos o índice do label
    
        Label.tabela_labels = tabela #atribuimos a tabela gerada para a variável global tabela_labels, para poder usar em outros arquivos

    @staticmethod #função estática, para poder chamar a função sem precisar criar um objeto da classe Label
    def get_tabela_labels():
        return Label.tabela_labels #função para retornar a tabela de labels, para poder usar em outros arquivos
    
    @staticmethod #função estática, para poder chamar a função sem precisar criar um objeto da classe Label
    def get_tabela_index_labels():
        return Label.tabela_index_labels #função para retornar a tabela de índices dos labels, para poder usar em outros arquivos