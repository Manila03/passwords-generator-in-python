import string
import random

largo= int(input("que tan larga quieres que sea la contraseña: "))
numbs= int(input("cuantos numeros quieres en tu contraseña: "))
mayus= int(input("cuantas letras mayusculas quieres en tu contraseña: "))
specials= int(input("cuantas letras especiales quieres en tu contraseña: "))

letras= list(string.ascii_lowercase)
numerosos= list(string.digits)
especiales= list(string.punctuation)

indice_numeros = random.sample(range(largo), numbs)
indice_numeros.sort()

indice_mayus = random.sample(range(largo - numbs), mayus)
indice_mayus.sort()

indice_specials = random.sample(range(largo - (numbs+mayus)), specials)
indice_specials.sort()

contra=[]
letra_actual=0
mayuscula_actual=0
numero_actual=0
caracSpecial_actual=0

for i in range(largo):
    if letra_actual in indice_numeros:
        contra.append(random.choice(numerosos))
        numero_actual+=1
        letra_actual+=1
    elif letra_actual in indice_specials:
        contra.append(random.choice(especiales))
        caracSpecial_actual+=1
        letra_actual+=1
    elif letra_actual in indice_mayus:
        contra.append(random.choice(letras).upper())
        mayuscula_actual+=1
        letra_actual+=1
    else:
        contra.append(random.choice(letras))
        letra_actual+=1
        
sitio= input("a que sitio pertenecera esta contraseña? por ej: 'contraseña de bing' ")
usuario= input("dinos tu nombre de usuario: (opcional)")    
contraseña = ''.join(contra)
print(f"la contraseña que hemos diseñado especialmente para ti es: {contraseña}")
#ahora quiero que cada vez que me cree una contraseña me pregunte de que plataforma sera y un archivo de texto q se modifique para agregar las contraseñas y a donde pertenecen

f = open("C:\\Users\\anoni\\OneDrive\\Desktop\\CODIGO uwu\\Python\\curso Dalto\\generar contraseñas\\archivo.txt", "a", encoding="UTF-8")
f.write(f" \n - hemos creado una contraseña para: {sitio} \n usuario: {usuario} \n contraseña: {contraseña}")
f.close()
print("hemos enviado la contraseña y el usuario al archivo de texto ubicado en la misma carpeta donde esta localizado el archivo .py")
