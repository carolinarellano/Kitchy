def username(user_name):

        lenght = len(user_name) #Calcular la longitud del nomre de usuario
        alphanumeric_values = user_name.isalnum() #Calcula que la cadena contenga valores alfanuméricos
        
        if  alphanumeric_values == False: # La cadena contiene valores no alfanuméricos
            #print("Username only can use letters and numbers")
            if lenght <= 8 and lenght >= 12:
            #print("Username length has to be between 8 and 12 characters")
                if lenght >5 and lenght <13 and alphanumeric_values == True:
                    return False
        return True


                
                
            
                
    
    
        
        
                
        
        
            
        
        
                
    
    
