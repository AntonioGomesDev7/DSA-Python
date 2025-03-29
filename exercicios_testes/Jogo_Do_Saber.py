import random

# Lista de palavras do Jogo do Saber
palavras = ["UDV", "CAINHANO", "HOSACA", "MARIRI", "TIUCO", "CHACRONA", "MESTRE", "CDI", "ELZA", "GABRIEL", "SALOMÃO", "MISTERIO"]

def escolher_palavra():
    return random.choice(palavras)  # Escolhe uma palavra aleatória

def jogar_jogo_do_saber():
    palavra = escolher_palavra()
    letras_corretas = set(palavra)
    letras_adivinhadas = set()
    tentativas = 6  

    print("🎓 Bem-vindo ao Jogo do Saber! 🎓")

    while tentativas > 0:
        palavra_oculta = " ".join([letra if letra in letras_adivinhadas else "_" for letra in palavra])
        print("\nPalavra:", palavra_oculta)
        print(f"Tentativas restantes: {tentativas}")
        
        letra = input("Digite uma letra: ").upper()

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra.")
            continue

        letras_adivinhadas.add(letra)

        if letra in letras_corretas:
            print("Boa! A letra está na palavra.")
        else:
            print("Letra errada!")
            tentativas -= 1

        if letras_corretas.issubset(letras_adivinhadas):
            print(f"🎉 Parabéns! Você acertou a palavra: {palavra} 🎉")
            break

    if tentativas == 0:
        print(f"💀 Fim de jogo! A palavra era: {palavra}")

if __name__ == "__main__":
    jogar_jogo_do_saber()