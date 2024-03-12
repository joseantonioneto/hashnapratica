def main():
    arquivo_original = "exemplo.txt"
    hash_salvo = open(arquivo_original + "_hash.txt").read()
    if verificar_integridade(arquivo_original, hash_salvo):
        print("A integridade do arquivo foi preservada.")
    else:
        print("Atenção o arquivo foi modificado.")