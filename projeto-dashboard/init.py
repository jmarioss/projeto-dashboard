import csv 

def show_csv(arquivo_csv):
    try:
        with open(arquivo_csv, newline='', mode='r') as file:
            reader = csv.reader(file)
            colunas = next(reader, None)
            if colunas:
                for coluna in colunas:
                    print(coluna) 
            else:
                print("Arquivo vazio")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

if __name__ == '__main__':
    show_csv('./data.csv')