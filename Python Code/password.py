def is_valid(c):        
    if len(c) >= 7:             
        if c[0].isupper():            
            if c[-1].isdigit():                     
                print('La contraseña es correcta!')                 
            else:                     
                print('Tiene que acabar en número')             
        else:                
             print('Tiene que empezar en mayúscula')        
    else:             
        print('tiene que tener 7 o mas caracteres') 


for i in range(4):
    contraseña = input('Introduce la contraseña:')
    is_valid(contraseña)

     
    
  
