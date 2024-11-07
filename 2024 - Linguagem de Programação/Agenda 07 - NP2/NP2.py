import csv

# Abrindo o arquivo CSV em modo de leitura com o delimitador correto
with open('/home/lucas/Documents/GitHub/ExerciciosDaFaculdade/2024 - Linguagem de Programação/Agenda 07 - NP2/ocorrencia.csv', mode='r', encoding='utf-8') as csvfile:
    # Usando o leitor csv para processar o conteúdo do arquivo, com delimitador ";"
    reader = csv.reader(csvfile, delimiter=';')
    
    # Pulando o cabeçalho (primeira linha)
    next(reader)
    
    # Abrindo o arquivo de saída em modo de escrita
    with open('joinville_ocorrencias.txt', mode='w', encoding='utf-8') as txtfile:
        for row in reader:
            # Verificando se a linha tem pelo menos 9 colunas (índice 8)
            if len(row) > 8:
                cidade = row[8].strip().upper()  # Remover espaços extras e comparar em maiúsculo
                print(f"Cidade: {cidade}")  # Imprimindo para ver o que está sendo lido
                
                # Verificando se o incidente foi em JOINVILLE
                if cidade == 'JOINVILLE':
                    # Capturando os campos desejados
                    codigo_ocorrencia = row[0]
                    ocorrencia_classificacao = row[5]
                    ocorrencia_dia = row[12]
                    investigacao_status = row[15]
                    
                    # Formatando a linha conforme o especificado
                    linha = (
                        codigo_ocorrencia + ' | ' +
                        ocorrencia_classificacao + ' | ' +
                        ocorrencia_dia + ' | ' +
                        investigacao_status + '\n'
                    )
                    
                    # Escrevendo a linha no arquivo de saída
                    txtfile.write(linha)
                    # Imprimindo a linha no console para ver se está sendo processada corretamente
                    print(f"Linha escrita: {linha.strip()}")
