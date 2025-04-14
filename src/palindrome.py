
def is_palindrome(s):
    return s == s[::-1] # invierte un strig los compara y si es igual es palindromo

if __name__ == "__main__":
    
    
    entrada = input("Ingresá una palabra o frase: ")
    if is_palindrome(entrada):
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")

