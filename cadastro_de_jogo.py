
print("Bem-vindo ao sistema de cadastro de jogadores! Insira suas informações para calcular sua pontuação.") # Introdução ao Programa.

# 1 - Programa para cadastro dos jogadores com informações básicas:

while True: # Loop para validação do nome do jogador.
    
        Nome_do_jogador = input("Digite seu nome:") # Entrada do jogador
    
        if len(Nome_do_jogador) < 3:
            print("Erro: O nome inserido deve conter no mínimo 3 caracteres e não pode ser espaço vazio.")
        
        else:
            print("Nome válido.")
            break

while True: # Loop para verificação de mínimo e máximo de idade permitida.

    try:
    
        Idade = int(input("Insira sua idade:")) # Entrada da idade do jogador.
    
        if Idade < 10 or Idade  > 80:
            print("A idade permitida é entre 10 a 80 anos!") # Retorno se verdadeiro;
    
        else:
            print("Idade permitida!") # Retorno se falso.
            break
   
    except ValueError:
        print("Erro: Por favor, insira um número válido para idade.")

while True: # Loop para validação de tempo de jogo.

    try:
    
        tempo_de_jogo = float(input("Digite seu tempo de jogo (somente números):")) # Tempo de jogo em número decimal.
    
        if tempo_de_jogo < 0:
            print("O tempo de jogo não pode ser negativo.")
        
        else:
            print("Tempo de jogo válido.")
            break
    
    except ValueError:
        print("Erro: Por favor, insira um número válido para tempo de jogo.")

while True:
    try:

        partidas_vencidas = int(input("Insira a quantidade de partidas vencidas (somente números(:)")) # Quantidade de partidas vencidas em número inteiro.
        if partidas_vencidas < 0:
            print("Erro: Por favor, insira um número válido para as partidas vencidas.")
        
        else:
            print("Número de partidas vencidas válido.")
            break
    
    except ValueError:
        print("Erro: Por favor, insira um número válido para partidas vencidas.")
        
# 2a - Condições de bonificação para cada jogador em sua determinada situação:

pontuacao_inicial = partidas_vencidas * 10

if Idade > 18:
    pontuacao_inicial += 10 # Adiciona 10 pontos bônus se maior de idade.
else:
    pontuacao_inicial -= 5 # Subtração de pontos caso seja de menor.

# 2b - Pontos bônus por tempo de jogo:

if tempo_de_jogo > 20: 
    pontuacao_inicial += 20 ## Adiciona 2o pontos por ser tempo de jogo maior que 20 horas.

else:
    pontuacao_inicial -= 5

# Cálculo da média por partida

if partidas_vencidas > 0:
    media_pontuacao = pontuacao_inicial / partidas_vencidas
else:
    media_pontuacao = 0
    print("Não é possível calcular a média porque o número de partidas vencidas é 0.")

# Evitar pontuação negativa

if pontuacao_inicial < 0:
    pontuacao_inicial = 0
if partidas_vencidas < 0:
    partidas_vencidas = 0

# Resultado final

print(f"Jogador: {Nome_do_jogador}")
print(f"Idade: {Idade}")
print(f"Tempo de jogo: {tempo_de_jogo}")
print(f"Partidas vencidas: {partidas_vencidas}")
print(f"Pontos iniciais: {pontuacao_inicial}")
print(f"Sua média de pontos por partida é de: {media_pontuacao}")





