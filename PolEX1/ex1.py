# Criado por: Roberto Affonso Araújo
# RA: 21504993
# Construção de compiladores
# UniCEUB
# Professor Leonardo Pol Suarez

# Essa variável atribui o número de espaços em branco como zero
numero_espacos = 0

# Essa variável atribui o número de caracteres como zero
numero_caracteres = 0

# Aqui, o IDE vai iniciar um prompt pedindo para que o usuário digite
# uma frase qualquer, após a inserção de uma frase, o Python vai atribuir
# o valor dessa frase na variável 'entrada'
entrada = input("Por favor insira alguma frase: ")

# Essa variável vai ser a nova string criada após percorrer toda a variável
# 'entrada'
novo_string = ""

# Loop para percorrer todos os caracteres da variável 'entrada'
for i in range(0, len(entrada)):
    # Caso encontrar um espaço em branco
    if entrada[i] == " ":
        # incrementar a variável 'numero_espacos'
        numero_espacos += 1
    # Caso ele não encontre nenhum espaço em branco
    # então só pode ser um caractere
    else:
        # incrementar a variável 'numero_caracteres'
        numero_caracteres += 1
        # concatenar a variável 'novo_string' com o
        # caractere correspondente a posição [i] da
        # variável 'entrada'
        novo_string += entrada[i]

# Retorna o total de espaços em branco
print("Total de espaços em branco: {}".format(numero_espacos))
print("\n")
# Retorna o total de caracteres
print("Total de caracteres: {}".format(numero_caracteres))
print("\n")
# Retorna a nova string criada, sem os espaços em branco
print("{}".format(novo_string))
