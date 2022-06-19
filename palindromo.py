def palindromo(frase):
    frase = frase.replace(' ', '')
    frase = frase.lower()
    frase_invertida =  frase[::-1]
    if frase == frase_invertida:
        return True
    else:
        return False


def run():
    frase = input('Escribe una frase: ')
    comprobar = palindromo(frase)
    if comprobar == True:
        print("La frase es Palindromo.")
    else:
        print("La frase no es Palindromo.")
        

if __name__ == '__main__':
    run()
