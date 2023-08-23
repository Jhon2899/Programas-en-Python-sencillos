print ('Hello, Contosoville!')

# This is a comment tha won't be interpreted as a command 

# Associate variable towm with the value 'Contosoville'

towm = "Contosoville"

# Print a message about the secret location 

print("The towm I am looking for is " + towm)

# Define a power (function) to chant a phrase

def chant ( phrase ):
    # Glue three copies together and print it as a message
    
    print (phrase + phrase + phrase )


# Invoke the power to chant on the phrase " Contosoville!"
chant ( "Contosoville!")

# create a function for the processor Cesar

#lower=convierte los caracteres alfabeticos en minuscula
#ord= convierte la letra en su respectivo valor en codigo ASCII

#def lasso_letter ( letter, shift_amount ):
  #letter_code = ord(letter.lower())
  #decoded_letter_code = letter_code + shift_amount
  #decoded_letter = chr(decoded_letter_code)
  #return decoded_letter


#print (lasso_letter('N',13))

#utilizamos MOD que es el signo de porcentaje (%)
#El operador mod divide dos números y devuelve el resto.

three_two = 3 % 2
eleven_four = 11 % 4
five_ten = 5 % 10

print(three_two)
print(eleven_four)
print(five_ten)


# corregimos la funcion 

def lasso_letter (letter, shift_amount):
   letter_code = ord(letter.lower())

   #The ASCII numbrer representation of lowercase letter 'a'
   a_ascii = ord('a')

   # The number of letters in the alphabet 
   alphabet_size = 26

   # The formula to calculate the ASCII number for the decoded letter
   #Take into account looping around the alphabet
   true_letter_code = a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size)

   #Convert the ASCII number to the character or letter
   decoded_letter = chr(true_letter_code)

   # Send the decoded letter back
   return decoded_letter

print(lasso_letter('a',2))


#Ejercicio: Descodificación de una palabra completa con un cifrado César

def lasso_word( word, shift_amount ):
    decoded_word = ""
    for letter in word:
        lasso_letter( letter, shift_amount )
        decoded_letter = lasso_letter(letter, shift_amount) # Invocamos una funcion dentro de lasso_word
        decoded_word = decoded_word + decoded_letter # Guardamos el valor de la palabra decoded_letter en decode_word y la vamos uniendo
    return decoded_word


# Try to decode the word "terra"
# Probamos el codigo con la palabra "terra"

print( "Shifting terra by 13 gives: \n" + lasso_word( "terra", 13 ) )


#Uso del descodificador Lasso para mostrar el mensaje secreto

#Mensaje a descrifrar
#Ncevy = 13
#gpvsui = 25
#ugflgkg = 18
#wjmmf = 1

#Agregamos la lineas para imprimir 
print( "Shifting Ncevy by 13 gives: \n" + lasso_word( "Ncevy", 13 ))
print( "Shifting gpvsui by 13 gives: \n" + lasso_word( "gpvsui", 25 )) 
print( "Shifting ugflgkg by -18 gives: \n" + lasso_word( "ugflgkg", -18 ) )
print( "Shifting wjmmf by -1 gives: \n" + lasso_word( "wjmmf", -1 ) )