import re


def carregar_wordlist(arquivo_wordlist):
    with open(arquivo_wordlist, 'r') as file:
        palavras = file.read().splitlines()
    return palavras

def ler_arquivo_embaralhado(arquivo_embaralhado):
    with open(arquivo_embaralhado, 'r') as file:
        palavras_embaralhadas = file.read().splitlines()
    return palavras_embaralhadas

def ordenar_palavra(palavra):
    return ''.join(sorted(palavra))

def desembaralhar_palavra(palavra_embaralhada, wordlist):
    palavra_ordenada = ordenar_palavra(palavra_embaralhada)
    for palavra in wordlist:
        if ordenar_palavra(palavra) == palavra_ordenada:
            return palavra
    return palavra_embaralhada  # Retorna a palavra embaralhada se não encontrar uma correspondência
def remover_caracteres_especiais(texto):
    return re.sub(r'[^A-Za-z0-9\s]', '', texto)
def escrever_arquivo_desembaralhado(arquivo_saida, palavras):
    with open(arquivo_saida, 'w') as file:
        for palavra in palavras:
            palavra_limpa = remover_caracteres_especiais(palavra).strip()
            file.write(palavra_limpa + '\n')

linhas = []

print("Digite as linhas de texto (digite uma linha vazia para terminar):")

# Coletar as linhas de entrada do usuário
while True:
    linha = input()
    if linha == "":
        break
    linhas.append(linha + '\n')  # Adicionar a nova linha ao final de cada entrada

# Nome do arquivo onde as linhas serão armazenadas
palavra_embaralhada = 'palavra_embaralhada.txt'
# Abrir o arquivo em modo de escrita ('w')
with open(palavra_embaralhada, 'w') as arquivo:
    arquivo.writelines(linhas)

# Substitua 'wordlist.txt' e 'embaralhado.txt' pelos caminhos dos seus arquivos
wordlist = carregar_wordlist('wordlist.txt')
palavras_embaralhadas = ler_arquivo_embaralhado('palavra_embaralhada.txt')

# Desembaralhar palavras
palavras_desembaralhadas = [desembaralhar_palavra(palavra, wordlist) for palavra in palavras_embaralhadas]

# Escrever palavras desembaralhadas em um novo arquivo
escrever_arquivo_desembaralhado('desembaralhado.txt', palavras_desembaralhadas)
#print(palavras_desembaralhadas)
final_desembaralhado = ",".join(palavras_desembaralhadas)
print(final_desembaralhado)