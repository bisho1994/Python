print("""

 ____ _____  _____ _    _  ____  
|  _ \_   _|/ ____| |  | |/ __ \ 
| |_) || | | (___ | |__| | |  | |
|  _ < | |  \___ \|  __  | |  | |
| |_) || |_ ____) | |  | | |__| |
|____/_____|_____/|_|  |_|\____/ 
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWK0XNNNNNNXK0000000KXXNNNNNXX0XWWWWW
WWWWWKo::cllllccloodxxdollllllcccoKWWWWW
WWWWWWXk:...,;;::::coc::c:;,..,d0XWWWWWW
WWWWWWWXo';c:,',:ol::coc,'',:;;xNWWWWWWW
WWWWWWWKc;ol,....,odoo:.....:oclKWWWWWWW
WWWWWWWKc:xx:'. .'lool,.  .'cxolKWWWWWWW
WWWWWWWNo,cxxolcllc:::llccloxo;dNWWWWWWW
WWWWWWWW0:.,:cllc;....,clllc,.;OWWWWWWWW
WWWWWWWNk:. ......''''........,xKWWWWWWW
WWWWWWM0:'..,;;::::::::;;;,,...;xNWWWWWW
WWWWWWWx'...,cloooooooolllc:'...cKMWWWWW
WWWWWWNd.  .':cclllllllcc::,..  ;KWWWWWW
WWWWWWWKc....',;;;::::;;;,,... ;ONWWWWWW
WWWWWWWWNkxx;..''''''''''..'oxdKWWWWWWWW
WWWWWWWWWWWWKo'..........'cONWWWWWWWWWWW
WWWWWWWWWWWWWN0:..ckkl..;kNWWWWWWWWWWWWW
WWWWWWWWWWWNkddoc:kNWOlclddxKWWWWWWWWWWW
WWWWWWWWWWWNKKKKKNWWWWNXKKKKXWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
""")

from datetime import datetime

now = datetime.now()
año_actual = now.year

#solicitar al usuario su nombre
nombre = input("¿cual es tu nombre?:")

# Solicitar al usuario su altura como un número decimal (float)
altura = float(input("Ingrese su altura en metros: "))


# Solicitar al usuario su año de nacimiento
año_nacimiento = int(input("Ingrese su año de nacimiento: "))

# Calcular la edad restando el año actual al año de nacimiento
edad = año_actual - año_nacimiento

# Imprimir la edad
print(nombre,"su edad es",edad, "años",f"y su altura es de {altura} metros")


es_menor_de_edad = edad < 18

# Imprimir si es menor de edad o no
if es_menor_de_edad:
    print("======> Eres menor de edad.")
else:
    print("======> Eres mayor de edad.")
