#Invertir palabras de una cadena dada.

str = 'código de práctica de prueba de geeks'

def reverseString(cadena):
    words = cadena.split(' ')
    
    reverse_sentence = ' '.join(reversed(words))
    
    return reverse_sentence

if __name__ == "__main__":
    print(reverseString(str))