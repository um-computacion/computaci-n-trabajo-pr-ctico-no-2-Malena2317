import re  #divide , reemplaza o buscra usando patrones en textos

def is_palindrome(s):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower() # elimina todo lo que no sea una palabra o numero y lo escribe en miniscula 
    return cleaned == cleaned[::-1] #compara con su reverso


if __name__ == "__main__":

    try:
    
        entrada = input("Ingresá una palabra o frase: ")
        if is_palindrome(entrada):
            print("Es un palíndromo")
        else:
            print("No es un palíndromo")

    except KeyboardInterrupt:
        print("\nPrograma finalizado por el usuario con Ctrl + C")  #captura la interrupcion crtl+c y nuestra un mensaje amigable 

