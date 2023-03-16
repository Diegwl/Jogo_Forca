from random import randint


def facil():
    vidas = 6
    palavras = ['LIVRO', 'CANETA', 'COMPUTADOR']
    dicas = ['FEITO PARA LER', 'USADO PARA ESCREVER', 'TECNOLOGIA']
    numero = randint(0, len(palavras) - 1)
    palavra_secreta = palavras[numero]
    return vidas, numero, palavra_secreta, dicas[numero]


def medio():
    vidas = 3
    palavras = ['LIVRO', 'CANETA', 'COMPUTADOR']
    dicas = ['FEITO PARA LER', 'USADO PARA ESCREVER', 'TECNOLOGIA']
    while True:
        adicionar = input("Deseja adicionar novas palavras na lista?[S/N]: ").upper()
        if adicionar == 'S':
            palavras.append(input("Digite a palavra que deseja adicionar: ").upper())
            dicas.append(input("Digite a dica que deseja adicionar: ").upper())
            print(f"Palavras: {palavras}")
            print(f"Dicas: {dicas}")
            break
        elif adicionar == 'N':
            break
        else:
            print("Erro!Digite S ou N")
    while True:
        retirar = input("Deseja retirar palavras na lista?[S/N]: ").upper()
        if retirar == 'S':
            print(palavras)
            delete = int(input('Digite o índice da palavra que deseja retirar: '))
            palavras.pop(delete)
            dicas.pop(delete)
            print(f"Palavras: {palavras}")
            print(f"Dicas: {dicas}")
            break
        elif retirar == 'N':
            break
        else:
            print("Erro!Digite S ou N")
    numero = randint(0, len(palavras) - 1)
    palavra_secreta = palavras[numero]
    return vidas, numero, palavra_secreta, dicas[numero]


def dificil():
    vidas = 3
    palavras = []
    dicas = []
    texto_f = []

    while True:
        adicionar = input("Deseja adicionar novas palavras na lista?[S/N]: ").upper()
        if adicionar == 'S':
            f = open('palavras.csv', 'a')
            f.write("\n"+input("Digite a palavra que deseja adicionar: ").upper()+";"+input("Digite a dica da palavra: ").upper())
            f.close()
            break
        elif adicionar == 'N':
            break
        else:
            print("Erro!Digite S ou N")

    f = open('palavras.csv', 'r')
    texto = f.read().split('\n')
    for i in range(len(texto)):
        texto_f.append(texto[i].split(';'))
    f.close()

    while True:
        retirar = input("Deseja retirar palavras na lista?[S/N]: ").upper()
        if retirar == 'S':
            print(texto_f)
            delete = int(input('Digite o índice da palavra que deseja retirar: '))
            texto_f.pop(delete)
            for i in range(len(texto_f)):
                palavras.append(texto_f[i][0])
                dicas.append(texto_f[i][1])
            f = open('palavras.csv', 'w')
            for i in range(len(palavras)):
                f.write(palavras[i]+';'+dicas[i])
            f.close()
            break
        elif retirar == 'N':
            break
        else:
            print("Erro!Digite S ou N")

    print(palavras)
    print(dicas)
    numero = randint(0, len(palavras) - 1)
    palavra_secreta = palavras[numero]
    return vidas, numero, palavra_secreta, dicas[numero]


def dificuldade():
    print("-*"*10+"-")
    print("   JOGO DA FORCA   ")
    print("-*"*10+"-")
    d = int(input("1 - Fácil\n2 - Médio\n3 - Difícil\nEscolha a Dificuldade desejada através do índice: "))
    if d == 1:
        vidas, numero, palavra_secreta, dica = facil()
        return vidas, numero, palavra_secreta, dica
    if d == 2:
        vidas, numero, palavra_secreta, dica = medio()
        return vidas, numero, palavra_secreta, dica
    if d == 3:
        vidas, numero, palavra_secreta, dica = dificil()
        return vidas, numero, palavra_secreta, dica


def jogo():
    vidas, numero, palavra_secreta, dica = dificuldade()
    letras = [[], []]
    print(palavra_secreta)
    while vidas > 0:
        resposta = 0
        for v in palavra_secreta:
            if v in letras[0]:
                print(v, end='')
                resposta += 1
            elif v == " ":
                print(v, end='')
                resposta += 1
            else:
                print('_', end='')
        print()
        if resposta == len(palavra_secreta):
            vidas = -1
            continue
        while True:
            letra = input("Digite uma letra: ").upper()
            if letra.isalpha() is True and letra not in letras[0] and letra not in letras[1]:
                if letra in palavra_secreta:
                    letras[0].append(letra[0][:])
                elif letra == 'DICA':
                    print(f"Dica: {dica}")
                else:
                    letras[1].append(letra[0][:])
                    vidas -= 1
                break
            elif letra.isalpha() is False:
                print("Erro! Digite uma letra!")
            else:
                print("Digite uma letra que ainda não foi digitada!")
        print(letras)
        print(f"Vidas: {vidas}")
    if vidas == 0:
        print(f"Você perdeu, suas vidas acabaram!\nA palavra secreta era: {palavra_secreta}")
    if vidas == -1:
        print("Você ganhou!")


def main():
    jogo()


if __name__ == "__main__":
    main()
