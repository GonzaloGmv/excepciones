import re

def correo():
    s = input("Escriba su direccion de correo electronico: ")
    if re.search("@", s) != None:
        if s.count('@') != 1 or s.count('.') !=1:
            print('Cuenta bloqueada a causa de un ataque')
        else:
            posicion_arroba = re.search("@", s).start()
            posicion_punto = re.search(".", s).start()
            lista_s = list(s)
            if posicion_punto > posicion_arroba:
                print('Cuenta bloqueada a causa de un ataque')
            else:
                if lista_s[len(lista_s)-1] == '.':
                    print('Cuenta bloqueada a causa de un ataque')
                else:
                    nombre = []
                    for i in range(posicion_arroba):
                        nombre.append(lista_s[i])
                    nombre = ''.join(nombre)
                    print('¡Bienvenido', nombre,'!')
    else:
        print('Una dirección de correo electrónico debe tener el formato xxx@xxx.xx')
        correo()
correo()