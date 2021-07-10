import random
#-IMPORTANDO LA LIBRERIA DEL PAQUETE WERKZEUG PARA GENERAR ENCRIPTAR
from werkzeug.security import generate_password_hash


MINUSCULAS='abcdefghijklmnopqrstuvwxyz'
MAYUSCULAS=MINUSCULAS.upper()
DIGITOS='1234567890'
SIMBOLOS='!$#&()?¡¿*{[}]-_'
CADENA=MINUSCULAS+MAYUSCULAS+DIGITOS+SIMBOLOS
LONGITUD=12

#-GENERANDO CONTRASENIAS
for n in range(10):
    contrasenia=random.sample(CADENA,LONGITUD)
    contrasenia=''.join(contrasenia)
    #-ENCRIPTANDO LAS CONTRASENIAS UTILIZANDO EL PAQUETE WERKZEUG
    pass_encriptado=generate_password_hash(contrasenia)
    print(f'{contrasenia}  =>   {pass_encriptado}')
