import random

# Lista de palavras
palavras = ["gato", "cachorro", "elefante", "girafa", "tigre"]

# Escolher palavra aleatória
palavra = random.choice(palavras)
tentativas = 6
letras_corretas = set()
letras_tentadas = set()

print("Bem-vindo ao jogo da forca!")

while tentativas > 0:
    # Mostrar a palavra com "_" para letras não descobertas
    palavra_oculta = "".join([letra if letra in letras_corretas else "_" for letra in palavra])
    print("\nPalavra:", palavra_oculta)
    print(f"Tentativas restantes: {tentativas}")
    
    letra = input("Digite uma letra: ").lower()

    # Verifica se a letra já foi tentada
    if letra in letras_tentadas:
        print("Você já tentou essa letra.")
        continue

    letras_tentadas.add(letra)

    if letra in palavra:
        letras_corretas.add(letra)
        print("Boa! A letra está na palavra.")
    else:
        print("Letra errada!")
        tentativas -= 1

    # Verificar se o jogador adivinhou toda a palavra
    if set(palavra) == letras_corretas:
        print(f"Parabéns! Você acertou a palavra: {palavra}")
        break

if tentativas == 0:
    print(f"Fim de jogo! A palavra era: {palavra}")


    #######################


    import random

palavras = ["banana", "abacaxi", "morango", "laranja", "manga"]
palavra = random.choice(palavras)
tentativas = 3

print("Bem-vindo ao jogo da forca!")

while tentativas > 0:
    tentativa = input("Tente adivinhar a palavra: ").lower()

    if tentativa == palavra:
        print("Parabéns! Você acertou!")
        break
    else:
        tentativas -= 1
        print(f"Errado! Tentativas restantes: {tentativas}")

if tentativas == 0:
    print(f"Você perdeu! A palavra era: {palavra}")