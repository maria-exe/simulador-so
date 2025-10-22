# Função para ler as configurações de um arquivo texto (.txt)
def ler_arquivo(caminho):
   
    with open(caminho, 'r', encoding='utf-8') as txt:
    
    # Lê primeira linha para definir o Escalonador e o Quantum
        p_linha = txt.readline().strip('\n')
        p_linha = p_linha.split(';')
        
        algortimo = p_linha[0]
        quantum = p_linha[1]
   
        next(txt) # Pula a primeira linha

    # Loop para as configurações restantes
        for linha in txt:
            n_linha = linha.strip()
            linha = n_linha.split(';')
            print(linha)
    
    # Falta: Salvar as informações de cada tarefa no TCB --

ler_arquivo('conf.txt')