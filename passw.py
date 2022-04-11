
def password(password):
    validator = False #que se vayan cumpliendo los requisitos uno a uno.
    lenght = len(password) #Calcula la longitud de la contraseña
    space = False  #variable para identificar espacios
    caps = False #variable para identificar letras mayúsculas
    lower = False #variable para contar identificar letras minúsculas
    numbers = False #variable para identificar números
    alphanumeric = password.isalnum()#si es alfanumérica retona True
    correct = True #verifica que hayan mayuscula, minuscula, numeros y no alfanuméricos       
    
    for character in password: #ciclo for que recorre caracter por caracter en la contraseña

        if character.isspace() == True: #Saber si el caracter es un espacio
            space = True #si encuentra un espacio se cambia el valor user
        if character.isupper() == True: #saber si hay mayuscula
            caps = True #acumulador o contador de mayusculas
        if character.islower() == True: #saber si hay minúsculas
            lower = True #acumulador o contador de minúsculas
        if character.isdigit() == True: #saber si hay números
            numbers = True #acumulador o contador de numeros

    if space==True: #hay espacios en blanco
            print("spaces are invalid")
    else:
        validator = True #se cumple el primer requisito que no hayan espacios
                    
    if lenght < 8:
        print("use 8 characters as minimum")
        validator = False #cambia a Flase si no se cumple el requisito móinimo de caracteres
    elif lenght >= 8:
        validator = True

    if caps == True and lower == True and numbers == True and alphanumeric == True and validator == True:
        validator = True #Cumple el requisito de tener mayuscula, minuscula, numeros y no alfanuméricos
    else:
        correct = False #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple
        
    if validator == False and correct == False:
        print("the password is not valid, try again")
    elif validator == True and correct == True:
        return True

