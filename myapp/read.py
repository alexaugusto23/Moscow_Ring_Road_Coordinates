class ReadFile:

    def leitura_arquivo():
        try:
            with open('log_file.txt','r', encoding='utf-8') as file:
                listas = []
                new_lista = []

                for linha in file:
                    valores = linha.split()
                    listas.append(valores)
                for item in range (0, len(listas)):
                    for sub_item in listas[item]: 
                        new_lista.append(sub_item)
                log = " ".join(new_lista)
                print(log)
                file.close()
            return log 
            
        except: return 'No file'

# log = ReadFile.leitura_arquivo()
# print(log)