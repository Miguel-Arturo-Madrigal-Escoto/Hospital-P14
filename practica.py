#practica 14
#madrigal escoto miguel arturo
#flores ontiveros aide sarahi
from colorama import init,Fore,Back,Style,Cursor;
from msvcrt import getch
from datetime import datetime
import os

def ventana(x1, x2, x3, x4, i, al, ar, len, n):
    init(autoreset=True)
    while(i != x2):
        print(Cursor.POS(i,x3)+Back.WHITE+(" "))
        print(Cursor.POS(i,x4)+Back.WHITE+(" "))
        i += 1
    if len >0 and len <10:
        leyen=46
    elif len>=10 and len<17:
        leyen=42
    elif len>=17 and len<25:
        leyen=37
    if len!=0:
        print(Cursor.POS(leyen,ar)+Back.WHITE+Fore.BLACK+n)
    while(al != x4):
        print(Cursor.POS(x1,al)+Back.WHITE+(" "))
        al += 1
    while(ar != x4):
        print(Cursor.POS(x2-1,ar+1)+Back.WHITE+(" "))
        ar += 1
    for t in range(79,84):
        print(Cursor.POS(t,6)+Back.RED+" ")
    for w in range(5,8):
        print(Cursor.POS(81,w)+Back.RED+" ")
def nombre_hospital():
    nuevo_nombre = str(input(Fore.CYAN+Cursor.POS(18,8)+"Nuevo nombre: "))
    return nuevo_nombre
def direccion():
    nueva_direccion = str(input(Fore.CYAN+Cursor.POS(18,8)+"Nueva direccion: "))
    return nueva_direccion
def servicios():
    nuevos_servicios = str(input(Fore.CYAN+Cursor.POS(18,8)+"Nuevos servicios: "))
    return nuevos_servicios
def numero_paciente():
    nuevo_num_paciente = int(input(Fore.CYAN+Cursor.POS(18,9)+"Numero del paciente: "))
    return nuevo_num_paciente
def nombre_paciente():
    nuevo_nom_paciente = str(input(Fore.CYAN+Cursor.POS(18,11)+"Nombre: "))
    return nuevo_nom_paciente
def edad_paciente():
    nuevo_edad_paciente = int(input(Fore.CYAN+Cursor.POS(18,13)+"Edad: "))
    return nuevo_edad_paciente
def analisis_paciente():
    nuevo_analisis_paciente = str(input(Fore.CYAN+Cursor.POS(18,15)+"Analisis: "))
    return nuevo_analisis_paciente
def antecedentes_paciente():
    nuevo_antecedentes_paciente = str(input(Fore.CYAN+Cursor.POS(18,17)+"Antecedentes: "))
    return nuevo_antecedentes_paciente
def fecha_registro():
    fecha = datetime.now()
    return fecha
def cedula_medico():
    nueva_cedula_medico = str(input(Fore.CYAN+Cursor.POS(18,11)+"Cedula: "))
    return nueva_cedula_medico
def nombre_medico():
    nuevo_nom_medico = str(input(Fore.CYAN+Cursor.POS(18,13)+"Nombre: "))
    return nuevo_nom_medico
def cargo_medico():
    nuevo_cargo_medico = str(input(Fore.CYAN+Cursor.POS(18,15)+"Cargo: "))
    return nuevo_cargo_medico

###DATOS PACIENTES###
def main_pacientes_uno():
    print(Cursor.POS(35,10)+Back.CYAN+" 1.- AGREGAR PACIENTE ")
    print(Cursor.POS(35,12)+" 2.- ELIMINAR PACIENTE ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR PACIENTE ")
    print(Cursor.POS(35,16)+" 4.- VER PACIENTE ")
    print(Cursor.POS(35,18)+" 5.- REGRESAR ")
    print(Cursor.POS(35,20)+("Ingrese la opcion deseada: "), end="")
def main_pacientes_dos():
    print(Cursor.POS(35,10)+" 1.- AGREGAR PACIENTE ")
    print(Cursor.POS(35,12)+Back.CYAN+" 2.- ELIMINAR PACIENTE ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR PACIENTE ")
    print(Cursor.POS(35,16)+" 4.- VER PACIENTE ")
    print(Cursor.POS(35,18)+" 5.- REGRESAR ")
    print(Cursor.POS(35,20)+("Ingrese la opcion deseada: "), end="")
def main_pacientes_tres():
    print(Cursor.POS(35,10)+" 1.- AGREGAR PACIENTE ")
    print(Cursor.POS(35,12)+" 2.- ELIMINAR PACIENTE ")
    print(Cursor.POS(35,14)+Back.CYAN+" 3.- MODIFICAR PACIENTE ")
    print(Cursor.POS(35,16)+" 4.- VER PACIENTE ")
    print(Cursor.POS(35,18)+" 5.- REGRESAR ")
    print(Cursor.POS(35,20)+("Ingrese la opcion deseada: "), end="")
def main_pacientes_cuatro():
    print(Cursor.POS(35,10)+" 1.- AGREGAR PACIENTE ")
    print(Cursor.POS(35,12)+" 2.- ELIMINAR PACIENTE ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR PACIENTE ")
    print(Cursor.POS(35,16)+Back.CYAN+" 4.- VER PACIENTE ")
    print(Cursor.POS(35,18)+" 5.- REGRESAR ")
    print(Cursor.POS(35,20)+("Ingrese la opcion deseada: "), end="")
def main_pacientes_cinco():
    print(Cursor.POS(35,10)+" 1.- AGREGAR PACIENTE ")
    print(Cursor.POS(35,12)+" 2.- ELIMINAR PACIENTE ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR PACIENTE ")
    print(Cursor.POS(35,16)+" 4.- VER PACIENTE ")
    print(Cursor.POS(35,18)+Back.CYAN+" 5.- REGRESAR ")
    print(Cursor.POS(35,20)+("Ingrese la opcion deseada: "), end="")
def registrar_paciente(numero_paciente,nombre_paciente,edad_paciente,analisis_paciente,antecedentes_paciente,fecha_registro):
    init(autoreset=True)
    x = [""]
    z = [""]
    alfa = [""]
    beta = [""]
    o = [""]
    w = [""]
    h = [""]
    lista_codigos = []
    contador_codigo = 8
    archivo_codigo = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    #agregar los id a la lista para verificar que no se repita
    for codigo in leer_codigos:
        if contador_codigo % 8 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    #modo sobreescritura de archivos
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="a",encoding="utf-8")

    #ingresar y validar el id del paciente

    for i in x:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"REGISTRAR PACIENTE")
        try:
            nuevo_num_paciente = numero_paciente()
            if str(nuevo_num_paciente)+"\n" in lista_codigos or str(nuevo_num_paciente) in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  NUMERO DUPLICADO  ")
                input()
                os.system("cls")
                x.append("")
            else:
                archivo_pacientes.write("\n"+str(nuevo_num_paciente))
                x.clear();x.append("")
                break
        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  NUMERO INVALIDO  ")
            input()
            os.system("cls")
            x.append("")
    #ingresar y validar el nombre
    for a in alfa:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"REGISTRAR PACIENTE")
        try:
            nuevo_nom_paciente = nombre_paciente()
            nom_dos = nuevo_nom_paciente.replace(" ","")
            if nom_dos.isdigit():
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  NOMBRE INVALIDO  ")
                input()
                os.system("cls")
                alfa.append("")
            else:
                archivo_pacientes.write("\n"+nuevo_nom_paciente)
                alfa.clear();alfa.append("")
                break
        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  NOMBRE INVALIDO  ")
            input()
            os.system("cls")
            alfa.append("")
    #ingresar y validar edad
    for b in beta:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"REGISTRAR PACIENTE")
        try:
            nuevo_edad_paciente = edad_paciente()
            if nuevo_edad_paciente >120:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  EDAD INVALIDA  ")
                input()
                os.system("cls")
                beta.append("")
            else:
                kk=str(nuevo_edad_paciente)
                archivo_pacientes.write("\n"+kk)
                beta.clear();beta.append("")
        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  EDAD INVALIDA  ")
            input()
            os.system("cls")
            beta.append("")
    #agregar el tipo de analisis del paciente
    for i in o:
        try:
            nuevo_analisis_paciente = analisis_paciente()
            archivo_pacientes.write("\n"+nuevo_analisis_paciente)
            o.clear();o.append("")
        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  DATO INVALIDO  ")
            o.append("")
    #agregar los antecedentes del paciente
    for it in w:
        try:
            nuevo_antecedentes_paciente = antecedentes_paciente()
            archivo_pacientes.write("\n"+nuevo_antecedentes_paciente)
            w.clear();w.append("")
        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  DATO INVALIDO  ")
            w.append("")
    fecha = fecha_registro()
    archivo_pacientes.write("\n"+str(fecha))
    archivo_pacientes.write("\n"+"Resultados del analisis:")
    archivo_pacientes.write("\n"+"Medico:")
    archivo_pacientes.close()
    #eliminar espacios en blanco
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    leer_lineas = archivo_pacientes.readlines()
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="w",encoding="utf-8")
    for renglon in leer_lineas:
        if renglon != ""+"\n":
            archivo_pacientes.write(renglon)
    archivo_pacientes.close()
    input();os.system("cls")
    x.clear()
    z.clear()
    alfa.clear()
    beta.clear()
    o.clear()
    w.clear()
    h.clear()
def eliminar_paciente(numero_paciente):
    z = [""]
    contador_lineas = 1
    cont = 0
    lista_codigos = []
    contador_codigo = 8
    archivo_codigo = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    for codigo in leer_codigos:
        if contador_codigo % 8 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    for o in z:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"ELIMINAR PACIENTE")
        arc = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer = arc.read()
        if leer== '':
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  NO HAY PACIENTES  ")
            z.clear()
            break
        arc.close()
        try:
            nuevo_num_paciente = numero_paciente()
            if str(nuevo_num_paciente)+"\n" not in lista_codigos and str(nuevo_num_paciente) not in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  PACIENTE NO ENCONTRADO  ")
                input();os.system("cls");z.append("")
            else:
                z.clear();z.append("")
                break

        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            z.append("")

    try:
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas = archivo_pacientes.readlines()
        for encontrar_id in leer_lineas:
            if encontrar_id == str(nuevo_num_paciente)+"\n" or encontrar_id == str(nuevo_num_paciente):
                break
            else:
                contador_lineas+=1
        #se le resta uno, ya que comenzo en [0]
        contador_lineas-=1
        #limite de la info a eliminar
        limite = contador_lineas+8
        archivo_pacientes.close()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas_dos = archivo_pacientes.readlines()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="w",encoding="utf-8")
        for y in leer_lineas_dos:
            if cont < contador_lineas or cont >= limite:
                archivo_pacientes.write(y)
            cont+=1
    except FileNotFoundError:
        print("Archivo no encontrado y/o inexistente")
    archivo_pacientes.close();input()
    z.clear()
    os.system("cls")
def submenu_pacientes_uno():
    print(Cursor.POS(35,10)+Back.CYAN+" 1.- MODIFICAR NUMERO DE PACIENTE ")
    print(Cursor.POS(35,12)+" 2.- MODIFICAR NOMBRE ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR EDAD ")
    print(Cursor.POS(35,16)+" 4.- MODIFICAR TIPO DE ANALISIS ")
    print(Cursor.POS(35,18)+" 5.- MODIFICAR ANTECEDENTES MEDICOS ")
    print(Cursor.POS(35,20)+" 6.- REGRESAR ")
    print(Cursor.POS(35,22)+("Ingrese la opcion deseada: "), end="")
def submenu_pacientes_dos():
    print(Cursor.POS(35,10)+" 1.- MODIFICAR NUMERO DE PACIENTE ")
    print(Cursor.POS(35,12)+Back.CYAN+" 2.- MODIFICAR NOMBRE ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR EDAD ")
    print(Cursor.POS(35,16)+" 4.- MODIFICAR TIPO DE ANALISIS ")
    print(Cursor.POS(35,18)+" 5.- MODIFICAR ANTECEDENTES MEDICOS ")
    print(Cursor.POS(35,20)+" 6.- REGRESAR ")
    print(Cursor.POS(35,22)+("Ingrese la opcion deseada: "), end="")
def submenu_pacientes_tres():
    print(Cursor.POS(35,10)+" 1.- MODIFICAR NUMERO DE PACIENTE ")
    print(Cursor.POS(35,12)+" 2.- MODIFICAR NOMBRE ")
    print(Cursor.POS(35,14)+Back.CYAN+" 3.- MODIFICAR EDAD ")
    print(Cursor.POS(35,16)+" 4.- MODIFICAR TIPO DE ANALISIS ")
    print(Cursor.POS(35,18)+" 5.- MODIFICAR ANTECEDENTES MEDICOS ")
    print(Cursor.POS(35,20)+" 6.- REGRESAR ")
    print(Cursor.POS(35,22)+("Ingrese la opcion deseada: "), end="")
def submenu_pacientes_cuatro():
    print(Cursor.POS(35,10)+" 1.- MODIFICAR NUMERO DE PACIENTE ")
    print(Cursor.POS(35,12)+" 2.- MODIFICAR NOMBRE ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR EDAD ")
    print(Cursor.POS(35,16)+Back.CYAN+" 4.- MODIFICAR TIPO DE ANALISIS ")
    print(Cursor.POS(35,18)+" 5.- MODIFICAR ANTECEDENTES MEDICOS ")
    print(Cursor.POS(35,20)+" 6.- REGRESAR ")
    print(Cursor.POS(35,22)+("Ingrese la opcion deseada: "), end="")
def submenu_pacientes_cinco():
    print(Cursor.POS(35,10)+" 1.- MODIFICAR NUMERO DE PACIENTE ")
    print(Cursor.POS(35,12)+" 2.- MODIFICAR NOMBRE ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR EDAD ")
    print(Cursor.POS(35,16)+" 4.- MODIFICAR TIPO DE ANALISIS ")
    print(Cursor.POS(35,18)+Back.CYAN+" 5.- MODIFICAR ANTECEDENTES MEDICOS ")
    print(Cursor.POS(35,20)+" 6.- REGRESAR ")
    print(Cursor.POS(35,22)+("Ingrese la opcion deseada: "), end="")
def submenu_pacientes_seis():
    print(Cursor.POS(35,10)+" 1.- MODIFICAR NUMERO DE PACIENTE ")
    print(Cursor.POS(35,12)+" 2.- MODIFICAR NOMBRE ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR EDAD ")
    print(Cursor.POS(35,16)+" 4.- MODIFICAR TIPO DE ANALISIS ")
    print(Cursor.POS(35,18)+" 5.- MODIFICAR ANTECEDENTES MEDICOS ")
    print(Cursor.POS(35,20)+Back.CYAN+" 6.- REGRESAR ")
    print(Cursor.POS(35,22)+("Ingrese la opcion deseada: "), end="")
def modificar_numero_paciente(numero_paciente):
    z = ['']
    x = ['']
    contador_lineas = 1
    cont = 0
    lista_codigos = []
    contador_codigo = 8
    archivo_codigo = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    for codigo in leer_codigos:
        if contador_codigo % 8 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    for o in z:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR NUMERO DE PACIENTE")
        try:
            buscar_numero = int(input(Fore.RED+Cursor.POS(18,10)+"Numero de paciente a modificar: "))
            if str(buscar_numero)+"\n" not in lista_codigos and str(buscar_numero) not in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  PACIENTE NO ENCONTRADO  ")
                input();os.system("cls");z.append("")
            else:
                for i in x:
                    ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
                    ventana(86, 92, 8, 40, 86, 40,8, 0,"")
                    ventana(18, 92, 40, 40, 18, 35,35, 0,"")
                    print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR NUMERO DE PACIENTE")
                    try:
                        nuevo_numero = int(input(Fore.CYAN+Cursor.POS(18,12)+"Nuevo numero de paciente: "))
                        if str(nuevo_numero)+"\n" in lista_codigos or str(nuevo_numero) in lista_codigos:
                            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+" NUMERO DUPLICADO  ")
                            input();os.system("cls");x.append("")
                        else:
                            x.clear();x.append("")
                            z.clear();z.append("")
                    except ValueError:
                        print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                        print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+" NUMERO INVALIDO  ")
                        input();os.system("cls");x.append("")

        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            input();os.system("cls");z.append("")
    try:
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas = archivo_pacientes.readlines()
        for encontrar_id in leer_lineas:
            if encontrar_id == str(buscar_numero)+"\n" or encontrar_id == str(buscar_numero):
                break
            else:
                contador_lineas+=1
        #se le resta uno, ya que comenzo en [0]
        contador_lineas-=1
        archivo_pacientes.close()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas_dos = archivo_pacientes.readlines()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="w",encoding="utf-8")
        for y in leer_lineas_dos:
            if cont == contador_lineas:
                archivo_pacientes.write(y.replace(str(buscar_numero),str(nuevo_numero)))
            else:
                archivo_pacientes.write(y)
            cont+=1
    except FileNotFoundError:
        print("Archivo no encontrado y/o inexistente")
    archivo_pacientes.close();input()
    z.clear()
    x.clear()
    os.system("cls")
def modificar_nombre_paciente(numero_paciente):
    z = ['']
    x = ['']
    contador_lineas = 1
    cont = 0
    lista_codigos = []
    datos_paciente = []
    contador_codigo = 8
    archivo_codigo = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    for codigo in leer_codigos:
        if contador_codigo % 8 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    for o in z:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR NOMBRE PACIENTE")
        try:
            nuevo_num_paciente = numero_paciente()
            if str(nuevo_num_paciente)+"\n" not in lista_codigos and str(nuevo_num_paciente) not in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  PACIENTE NO ENCONTRADO  ")
                input();os.system("cls");z.append("")
            else:
                for i in x:
                    ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
                    ventana(86, 92, 8, 40, 86, 40,8, 0,"")
                    ventana(18, 92, 40, 40, 18, 35,35, 0,"")
                    print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR NOMBRE PACIENTE")
                    try:
                        nuevo_nom = str(input(Fore.CYAN+Cursor.POS(18,12)+"Nuevo nombre: "))
                        nom = nuevo_nom.replace(" ","")
                        if nom.isdigit():
                            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+" NOMBRE INVALIDO  ")
                            input();os.system("cls");x.append("")
                        else:
                            x.clear();x.append("")
                            z.clear();z.append("")
                    except ValueError:
                        print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                        print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+" NOMBRE INVALIDO  ")
                        x.append("")

        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            input();os.system("cls");z.append("")

    try:
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas = archivo_pacientes.readlines()
        for encontrar_id in leer_lineas:
            if encontrar_id == str(nuevo_num_paciente)+"\n" or encontrar_id == str(nuevo_num_paciente):
                break
            else:
                contador_lineas+=1
        #se le resta uno, ya que comenzo en [0]
        contador_lineas-=1
        #limite de la info a eliminar
        limite = contador_lineas+8
        archivo_pacientes.close()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas_dos = archivo_pacientes.readlines()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="w",encoding="utf-8")
        for y in leer_lineas_dos:
            if cont < contador_lineas or cont >= limite:
                archivo_pacientes.write(y)
            else:
                if "\n" not in y:
                    datos_paciente.append(y+"\n")
                else:
                    datos_paciente.append(y)
            cont+=1
    except FileNotFoundError:
        print("Archivo no encontrado y/o inexistente")
    datos_paciente.remove(datos_paciente[1])
    datos_paciente.insert(1,nuevo_nom)
    archivo_pacientes.close()
    #se vuelve a leer para reemplazar el nombre
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="a",encoding="utf-8")
    for yy in range(0,len(datos_paciente)):
        archivo_pacientes.write("\n"+datos_paciente[yy])
    archivo_pacientes.close()
    #eliminar renglones en blanco
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    blanco = archivo_pacientes.readlines()
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="w",encoding="utf-8")
    for k in blanco:
        if k != ""+"\n":
            archivo_pacientes.write(k)
    archivo_pacientes.close()
    z.clear()
    x.clear()
    os.system("cls")
def modificar_edad_paciente(numero_paciente):
    z = ['']
    x = ['']
    contador_lineas = 1
    cont = 0
    lista_codigos = []
    datos_paciente = []
    contador_codigo = 8
    archivo_codigo = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    for codigo in leer_codigos:
        if contador_codigo % 8 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    for o in z:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR EDAD PACIENTE")
        try:
            nuevo_num_paciente = numero_paciente()
            if str(nuevo_num_paciente)+"\n" not in lista_codigos and str(nuevo_num_paciente) not in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  PACIENTE NO ENCONTRADO  ")
                input();os.system("cls");z.append("")
            else:
                for i in x:
                    ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
                    ventana(86, 92, 8, 40, 86, 40,8, 0,"")
                    ventana(18, 92, 40, 40, 18, 35,35, 0,"")
                    print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR EDAD PACIENTE")
                    try:
                        nueva_edad = int(input(Fore.CYAN+Cursor.POS(18,12)+"Nueva edad: "))

                        x.clear();x.append("")
                        z.clear();z.append("")
                    except ValueError:
                        print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                        print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+" EDAD INVALIDA  ")
                        input();os.system("cls");x.append("")

        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            input();os.system("cls");z.append("")

    try:
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas = archivo_pacientes.readlines()
        for encontrar_id in leer_lineas:
            if encontrar_id == str(nuevo_num_paciente)+"\n" or encontrar_id == str(nuevo_num_paciente):
                break
            else:
                contador_lineas+=1
        #se le resta uno, ya que comenzo en [0]
        contador_lineas-=1
        #limite de la info a eliminar
        limite = contador_lineas+8
        archivo_pacientes.close()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas_dos = archivo_pacientes.readlines()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="w",encoding="utf-8")
        for y in leer_lineas_dos:
            if cont < contador_lineas or cont >= limite:
                archivo_pacientes.write(y)
            else:
                if "\n" not in y:
                    datos_paciente.append(y+"\n")
                else:
                    datos_paciente.append(y)
            cont+=1
    except FileNotFoundError:
        print("Archivo no encontrado y/o inexistente")
    datos_paciente.remove(datos_paciente[2])
    datos_paciente.insert(2,nueva_edad)
    archivo_pacientes.close()
    #se vuelve a leer para reemplazar el nombre
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="a",encoding="utf-8")
    for yy in range(0,len(datos_paciente)):
        archivo_pacientes.write("\n"+str(datos_paciente[yy]))
    archivo_pacientes.close()
    #eliminar renglones en blanco
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    blanco = archivo_pacientes.readlines()
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="w",encoding="utf-8")
    for k in blanco:
        if k != ""+"\n":
            archivo_pacientes.write(k)
    archivo_pacientes.close()
    z.clear()
    x.clear()
    os.system("cls")
def modificar_analisis_paciente(numero_paciente):
    z = ['']
    x = ['']
    contador_lineas = 1
    cont = 0
    lista_codigos = []
    datos_paciente = []
    contador_codigo = 8
    archivo_codigo = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    for codigo in leer_codigos:
        if contador_codigo % 8 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    for o in z:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR ANALISIS PACIENTE")
        try:
            nuevo_num_paciente = numero_paciente()
            if str(nuevo_num_paciente)+"\n" not in lista_codigos and str(nuevo_num_paciente) not in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  PACIENTE NO ENCONTRADO  ")
                input();os.system("cls");z.append("")
            else:
                for i in x:
                    ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
                    ventana(86, 92, 8, 40, 86, 40,8, 0,"")
                    ventana(18, 92, 40, 40, 18, 35,35, 0,"")
                    print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR ANALISIS PACIENTE")
                    try:
                        nuevo_analisis = str(input(Fore.CYAN+Cursor.POS(18,12)+"Nuevo analisis: "))

                        x.clear();x.append("")
                        z.clear();z.append("")
                    except ValueError:
                        print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                        print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+" ANALISIS INVALIDO  ")
                        input();os.system("cls");x.append("")

        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            input();os.system("cls");z.append("")

    try:
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas = archivo_pacientes.readlines()
        for encontrar_id in leer_lineas:
            if encontrar_id == str(nuevo_num_paciente)+"\n" or encontrar_id == str(nuevo_num_paciente):
                break
            else:
                contador_lineas+=1
        #se le resta uno, ya que comenzo en [0]
        contador_lineas-=1
        #limite de la info a eliminar
        limite = contador_lineas+8
        archivo_pacientes.close()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas_dos = archivo_pacientes.readlines()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="w",encoding="utf-8")
        for y in leer_lineas_dos:
            if cont < contador_lineas or cont >= limite:
                archivo_pacientes.write(y)
            else:
                if "\n" not in y:
                    datos_paciente.append(y+"\n")
                else:
                    datos_paciente.append(y)
            cont+=1
    except FileNotFoundError:
        print("Archivo no encontrado y/o inexistente")
    datos_paciente.remove(datos_paciente[3])
    datos_paciente.insert(3,nuevo_analisis)
    archivo_pacientes.close()
    #se vuelve a leer para reemplazar el nombre
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="a",encoding="utf-8")
    for yy in range(0,len(datos_paciente)):
        archivo_pacientes.write("\n"+str(datos_paciente[yy]))
    archivo_pacientes.close()
    #eliminar renglones en blanco
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    blanco = archivo_pacientes.readlines()
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="w",encoding="utf-8")
    for k in blanco:
        if k != ""+"\n":
            archivo_pacientes.write(k)
    archivo_pacientes.close()
    z.clear()
    x.clear()
    os.system("cls")
def modificar_antecedentes_paciente(numero_paciente):
    z = ['']
    x = ['']
    contador_lineas = 1
    cont = 0
    lista_codigos = []
    datos_paciente = []
    contador_codigo = 8
    archivo_codigo = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    for codigo in leer_codigos:
        if contador_codigo % 8 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    for o in z:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR ANTECEDENTES PACIENTE")
        try:
            nuevo_num_paciente = numero_paciente()
            if str(nuevo_num_paciente)+"\n" not in lista_codigos and str(nuevo_num_paciente) not in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  PACIENTE NO ENCONTRADO  ")
                input();os.system("cls");z.append("")
            else:
                for i in x:
                    try:
                        nuevos_antecedentes = str(input(Fore.CYAN+Cursor.POS(18,12)+"Nuevos antecedentes: "))

                        x.clear();x.append("")
                        z.clear();z.append("")
                    except ValueError:
                        print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                        print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+" ANTECEDENTES INVALIDOS  ")
                        input();os.system("cls");x.append("")

        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            input();os.system("cls");z.append("")

    try:
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas = archivo_pacientes.readlines()
        for encontrar_id in leer_lineas:
            if encontrar_id == str(nuevo_num_paciente)+"\n" or encontrar_id == str(nuevo_num_paciente):
                break
            else:
                contador_lineas+=1
        #se le resta uno, ya que comenzo en [0]
        contador_lineas-=1
        #limite de la info a eliminar
        limite = contador_lineas+8
        archivo_pacientes.close()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas_dos = archivo_pacientes.readlines()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="w",encoding="utf-8")
        for y in leer_lineas_dos:
            if cont < contador_lineas or cont >= limite:
                archivo_pacientes.write(y)
            else:
                if "\n" not in y:
                    datos_paciente.append(y+"\n")
                else:
                    datos_paciente.append(y)
            cont+=1
    except FileNotFoundError:
        print("Archivo no encontrado y/o inexistente")
    datos_paciente.remove(datos_paciente[4])
    datos_paciente.insert(4,nuevos_antecedentes)
    archivo_pacientes.close()
    #se vuelve a leer para reemplazar el nombre
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="a",encoding="utf-8")
    for yy in range(0,len(datos_paciente)):
        archivo_pacientes.write("\n"+str(datos_paciente[yy]))
    archivo_pacientes.close()
    #eliminar renglones en blanco
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    blanco = archivo_pacientes.readlines()
    archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="w",encoding="utf-8")
    for k in blanco:
        if k != ""+"\n":
            archivo_pacientes.write(k)
    archivo_pacientes.close()
    z.clear()
    x.clear()
    os.system("cls")
def main_submenu_pacientes():
    init(autoreset=True)
    a, b = [""],[""]
    for i in a:
        opcion = 1
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR PACIENTES")
        arc = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer = arc.read()
        if leer== '':
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  NO HAY PACIENTES  ")
            input()
            os.system("cls")
            break
        arc.close()
        submenu_pacientes_uno()
        print("1")
        for i in b:
            tecla = ord(getch())
            if(tecla == 224):
                tecla = ord(getch())
            if(tecla == 27):
                opcion=6
                break
            if(tecla == 80 and opcion == 1):
                submenu_pacientes_dos()
                opcion=2
                print("2")
            elif(tecla == 80 and opcion == 2):
                submenu_pacientes_tres()
                opcion = 3
                print("3")
            elif(tecla == 80 and opcion == 3):
                submenu_pacientes_cuatro()
                opcion = 4
                print("4")
            elif(tecla == 80 and opcion == 4):
                submenu_pacientes_cinco()
                opcion = 5
                print("5")
            elif(tecla == 80 and opcion == 5):
                submenu_pacientes_seis()
                opcion = 6
                print("6")
            elif(tecla == 80 and opcion == 6):
                submenu_pacientes_uno()
                opcion = 1
                print("1")
            elif(tecla == 72 and opcion == 6):
                submenu_pacientes_cinco()
                opcion = 5
                print("5")
            elif(tecla == 72 and opcion == 5):
                submenu_pacientes_cuatro()
                opcion = 4
                print("4")
            elif(tecla == 72 and opcion == 4):
                submenu_pacientes_tres()
                opcion = 3
                print("3")
            elif(tecla == 72 and opcion == 3):
                submenu_pacientes_dos()
                opcion = 2
                print("2")
            elif(tecla == 72 and opcion == 2):
                submenu_pacientes_uno()
                opcion = 1
                print("1")
            elif(tecla == 72 and opcion == 1):
                submenu_pacientes_seis()
                opcion = 6
                print("6")
            elif(tecla == 13):
                break
            elif(tecla == 49):
                submenu_pacientes_uno()
                opcion = 1
                print("1")
            elif(tecla == 50):
                submenu_pacientes_dos()
                opcion = 2
                print("2")
            elif(tecla == 51):
                submenu_pacientes_tres()
                opcion= 3
                print("3")
            elif(tecla == 52):
                submenu_pacientes_cuatro()
                opcion = 4
                print("4")
            elif(tecla == 53):
                submenu_pacientes_cinco()
                opcion = 5
                print("5")
            elif(tecla == 54):
                submenu_pacientes_seis()
                opcion = 6
                print("6")
            b.append("")
        if(opcion==1):
            os.system("cls")
            modificar_numero_paciente(numero_paciente)
            a.append("")
            continue
        elif(opcion==2):
            os.system("cls")
            modificar_nombre_paciente(numero_paciente)
            a.append("")
            continue
        elif(opcion==3):
            os.system("cls")
            modificar_edad_paciente(numero_paciente)
            a.append("")
            continue
        elif(opcion==4):
            os.system("cls")
            modificar_analisis_paciente(numero_paciente)
            a.append("")
            continue
        elif(opcion==5):
            os.system("cls")
            modificar_antecedentes_paciente(numero_paciente)
            a.append("")
            continue
        elif(opcion==6):
            a.clear()
            b.clear()
            a.append("")
            b.append("")
            os.system("cls")
            break
def ver_paciente(numero_paciente):
    init(autoreset=True)
    c = [""]
    contador_lineas = 1
    posicion = 0
    lista_codigos = []
    contador_codigo = 8
    mostrar = 0
    archivo_codigo = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    #agregar los id a la lista para verificar que no se repita
    for codigo in leer_codigos:
        if contador_codigo % 8 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    for o in c:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"VER PACIENTE")
        arc = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer = arc.read()
        if leer== '':
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  NO HAY PACIENTES  ")
            c.clear()
            break
        arc.close()
        try:
            nuevo_num_paciente = numero_paciente()
            if str(nuevo_num_paciente)+"\n" not in lista_codigos and str(nuevo_num_paciente) not in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  PACIENTE NO ENCONTRADO  ")
                input();os.system("cls");c.append("")
            else:
                c.clear();c.append("")
                break

        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            input()
            os.system("cls")
            c.append("")
    try:
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas = archivo_pacientes.readlines()
        for encontrar_id in leer_lineas:
            if encontrar_id == str(nuevo_num_paciente)+"\n" or encontrar_id == str(nuevo_num_paciente):
                break
            else:
                contador_lineas+=1
        #se le resta uno, ya que comenzo en [0]
        contador_lineas-=1
        cont = 0
        #limite de la info a eliminar
        limite = contador_lineas+8
        archivo_pacientes.close()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas_dos = archivo_pacientes.readlines()
        for y in leer_lineas_dos:
            if cont >= contador_lineas and cont <= limite:
                if mostrar == 0:
                    print(Fore.RED+Cursor.POS(18,12+posicion)+"Numero de paciente: "+Fore.WHITE+y)
                elif mostrar == 1:
                    print(Fore.RED+Cursor.POS(18,12+posicion)+"Nombre: "+Fore.WHITE+y)
                elif mostrar == 2:
                    print(Fore.RED+Cursor.POS(18,12+posicion)+"Edad: "+Fore.WHITE+y)
                elif mostrar == 3:
                    print(Fore.RED+Cursor.POS(18,12+posicion)+"Analisis: "+Fore.WHITE+y)
                elif mostrar == 4:
                    print(Fore.RED+Cursor.POS(18,12+posicion)+"Antecedentes: "+Fore.WHITE+y)
                elif mostrar == 5:
                    print(Fore.RED+Cursor.POS(18,12+posicion)+"Fecha de registro: "+Fore.WHITE+y)
                elif mostrar == 6:
                    print(Fore.RED+Cursor.POS(18,12+posicion)+y)
                elif mostrar == 7:
                    print(Fore.RED+Cursor.POS(18,12+posicion)+y)
                else:
                    mostrar = 0
                    posicion = 0
                    cont = 0
                    cont_lineas = 0
                    break
                mostrar+=1
                posicion+=2
            cont+=1

    except FileNotFoundError:
        print("Archivo no encontrado y/o inexistente")
    archivo_pacientes.close();input()
    c.clear()
    os.system("cls")
def alta_pacientes():
    """ programa en donde se:
    -agrega paciente
    -elimina paciente
    -modifica paciente: id,nombre,edad,tipo analisis o antecedentes
    -ver paciente
    -regresa al menu principal
    """
    init(autoreset=True)
    a, b = [""],[""]
    for i in a:
        opcion = 1
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE PACIENTE ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"PACIENTES")
        main_pacientes_uno()
        print("1")
        for i in b:
            tecla = ord(getch())
            if(tecla == 224):
                tecla = ord(getch())
            if(tecla == 27):
                opcion=5
                break
            if(tecla == 80 and opcion == 1):
                main_pacientes_dos()
                opcion =2
                print("2")
            elif(tecla == 80 and opcion == 2):
                main_pacientes_tres()
                opcion =3
                print("3")
            elif(tecla == 80 and opcion == 3):
                main_pacientes_cuatro()
                opcion =4
                print("4")
            elif(tecla == 80 and opcion == 4):
                main_pacientes_cinco()
                opcion =5
                print("5")
            elif(tecla == 80 and opcion == 5):
                main_pacientes_uno()
                opcion =1
                print("1")
            elif(tecla == 72 and opcion == 5):
                main_pacientes_cuatro()
                opcion=4
                print("4")
            elif(tecla == 72 and opcion == 4):
                main_pacientes_tres()
                opcion =3
                print("3")
            elif(tecla == 72 and opcion == 3):
                main_pacientes_dos()
                opcion =2
                print("2")
            elif(tecla == 72 and opcion == 2):
                main_pacientes_uno()
                opcion =1
                print("1")
            elif(tecla == 72 and opcion == 1):
                main_pacientes_cinco()
                opcion =5
                print("5")
            elif(tecla == 13):
                break
            elif(tecla == 49):
                opcion = 1
                main_pacientes_uno()
                print("1")
            elif(tecla == 50):
                opcion = 2
                main_pacientes_dos()
                print("2")
            elif(tecla == 51):
                opcion = 3
                main_pacientes_tres()
                print("3")
            elif(tecla == 52):
                opcion = 4
                main_pacientes_cuatro()
                print("4")
            elif(tecla == 53):
                opcion = 5
                main_pacientes_cinco()
                print("5")
            b.append("")
        if(opcion==1):
            os.system("cls")
            registrar_paciente(numero_paciente,nombre_paciente,edad_paciente,analisis_paciente,antecedentes_paciente,fecha_registro)
            a.append("")
            continue
        elif(opcion==2):
            os.system("cls")
            eliminar_paciente(numero_paciente)
            a.append("")
            continue
        elif(opcion==3):
            os.system("cls")
            main_submenu_pacientes()
            a.append("")
            continue
        elif(opcion==4):
            os.system("cls")
            ver_paciente(numero_paciente)
            a.append("")
            continue
        elif(opcion==5):
            a.clear()
            b.clear()
            a.append("")
            b.append("")
            os.system("cls")
            break

###DATOS MEDICOS###
def medicos_uno():
    print(Cursor.POS(35,10)+Back.CYAN+" 1.- AGREGAR MEDICO ")
    print(Cursor.POS(35,12)+" 2.- ELIMINAR MEDICO ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR MEDICO ")
    print(Cursor.POS(35,16)+" 4.- VER MEDICO ")
    print(Cursor.POS(35,18)+" 5.- ANALISIS ")
    print(Cursor.POS(35,20)+" 6.- REGRESAR ")
    print(Cursor.POS(35,24)+("Ingrese la opcion deseada: "), end="")
def medicos_dos():
    print(Cursor.POS(35,10)+" 1.- AGREGAR MEDICO ")
    print(Cursor.POS(35,12)+Back.CYAN+" 2.- ELIMINAR MEDICO ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR MEDICO ")
    print(Cursor.POS(35,16)+" 4.- VER MEDICO ")
    print(Cursor.POS(35,18)+" 5.- ANALISIS ")
    print(Cursor.POS(35,20)+" 6.- REGRESAR ")
    print(Cursor.POS(35,24)+("Ingrese la opcion deseada: "), end="")
def medicos_tres():
    print(Cursor.POS(35,10)+" 1.- AGREGAR MEDICO ")
    print(Cursor.POS(35,12)+" 2.- ELIMINAR MEDICO ")
    print(Cursor.POS(35,14)+Back.CYAN+" 3.- MODIFICAR MEDICO ")
    print(Cursor.POS(35,16)+" 4.- VER MEDICO ")
    print(Cursor.POS(35,18)+" 5.- ANALISIS ")
    print(Cursor.POS(35,20)+" 6.- REGRESAR ")
    print(Cursor.POS(35,24)+("Ingrese la opcion deseada: "), end="")
def medicos_cuatro():
    print(Cursor.POS(35,10)+" 1.- AGREGAR MEDICO ")
    print(Cursor.POS(35,12)+" 2.- ELIMINAR MEDICO ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR MEDICO ")
    print(Cursor.POS(35,16)+Back.CYAN+" 4.- VER MEDICO ")
    print(Cursor.POS(35,18)+" 5.- ANALISIS ")
    print(Cursor.POS(35,20)+" 6.- REGRESAR ")
    print(Cursor.POS(35,24)+("Ingrese la opcion deseada: "), end="")
def medicos_cinco():
    print(Cursor.POS(35,10)+" 1.- AGREGAR MEDICO ")
    print(Cursor.POS(35,12)+" 2.- ELIMINAR MEDICO ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR MEDICO ")
    print(Cursor.POS(35,16)+" 4.- VER MEDICO ")
    print(Cursor.POS(35,18)+Back.CYAN+" 5.- ANALISIS ")
    print(Cursor.POS(35,20)+" 6.- REGRESAR ")
    print(Cursor.POS(35,24)+("Ingrese la opcion deseada: "), end="")
def medicos_seis():
    print(Cursor.POS(35,10)+" 1.- AGREGAR MEDICO ")
    print(Cursor.POS(35,12)+" 2.- ELIMINAR MEDICO ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR MEDICO ")
    print(Cursor.POS(35,16)+" 4.- VER MEDICO ")
    print(Cursor.POS(35,18)+" 5.- ANALISIS ")
    print(Cursor.POS(35,20)+Back.CYAN+" 6.- REGRESAR ")
    print(Cursor.POS(35,24)+("Ingrese la opcion deseada: "), end="")
def registrar_medico(cedula_medico,nombre_medico,cargo_medico):
    init(autoreset=True)
    x = [""]
    alfa = [""]
    beta = [""]
    lista_codigos = []
    contador_codigo = 3
    archivo_codigo = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    #agregar los id a la lista para verificar que no se repita
    for codigo in leer_codigos:
        if contador_codigo % 3 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    #modo sobreescritura de archivos
    archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="a",encoding="utf-8")

    #ingresar y validar el id del paciente

    for i in x:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE MEDICO ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"REGISTRAR MEDICO")
        try:
            nueva_cedula_medico = cedula_medico()
            if nueva_cedula_medico+"\n" in lista_codigos or nueva_cedula_medico in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+" CEDULA DUPLICADA  ")
                input();os.system("cls");x.append("")
            else:
                archivo_medicos.write("\n"+nueva_cedula_medico)
                x.clear();x.append("")
                break
        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  CEDULA INVALIDA  ")
            input();os.system("cls");x.append("")
    #ingresar y validar el nombre
    for a in alfa:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE MEDICO ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"REGISTRAR MEDICO")
        try:
            nuevo_nom_medico = nombre_medico()
            nom_dos = nuevo_nom_medico.replace(" ","")
            if nom_dos.isdigit():
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  NOMBRE INVALIDO  ")
                input();os.system("cls");alfa.append("")
            else:
                archivo_medicos.write("\n"+nuevo_nom_medico)
                alfa.clear();alfa.append("")
                break
        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  NOMBRE INVALIDO  ")
            input();os.system("cls");alfa.append("")
    #ingresar y validar edad
    for b in beta:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE MEDICO ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"REGISTRAR MEDICO")
        try:
            nuevo_cargo_medico = cargo_medico()
            if nuevo_cargo_medico.isdigit():
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  CARGO INVALIDO  ")
                input();os.system("cls");beta.append("")
            else:
                archivo_medicos.write("\n"+nuevo_cargo_medico)
                beta.clear();beta.append("")
#BUSCAR CARGO INVALIDO
        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  CARGO INVALIDO ")
            input();os.system("cls");beta.append("")

    archivo_medicos.close()
    #eliminar espacios en blanco
    archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
    leer_lineas = archivo_medicos.readlines()
    archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="w",encoding="utf-8")
    for renglon in leer_lineas:
        if renglon != ""+"\n":
            archivo_medicos.write(renglon)
    archivo_medicos.close()

    x.clear()
    alfa.clear()
    beta.clear()
    input();os.system("cls")
def eliminar_medico(cedula_medico):
    z = [""]
    contador_lineas = 1
    cont = 0
    lista_codigos = []
    contador_codigo = 3
    archivo_codigo = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    for codigo in leer_codigos:
        if contador_codigo % 3 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    for o in z:

        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE MEDICO ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"ELIMINAR MEDICO")
        arc = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer = arc.read()
        if leer== '':
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  NO HAY MEDICOS  ")
            break
        arc.close()
        try:
            nueva_cedula_medico = cedula_medico()
            if nueva_cedula_medico+"\n" not in lista_codigos and nueva_cedula_medico not in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  MEDICO NO ENCONTRADO  ")
                input();os.system("cls");z.append("")
            else:
                z.clear();z.append("")
                break

        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            z.append("")

    try:
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer_lineas = archivo_medicos.readlines()
        for encontrar_id in leer_lineas:
            if encontrar_id == nueva_cedula_medico+"\n" or encontrar_id == nueva_cedula_medico:
                break
            else:
                contador_lineas+=1
        #se le resta uno, ya que comenzo en [0]
        contador_lineas-=1
        #limite de la info a eliminar
        limite = contador_lineas+3
        archivo_medicos.close()
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer_lineas_dos = archivo_medicos.readlines()
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="w",encoding="utf-8")
        for y in leer_lineas_dos:
            if cont < contador_lineas or cont >= limite:
                archivo_medicos.write(y)
            cont+=1
    except FileNotFoundError:
        print("Archivo no encontrado y/o inexistente")
    archivo_medicos.close();input()
    z.clear()
    os.system("cls")
def submenu_medicos_uno():
    print(Cursor.POS(35,10)+Back.CYAN+" 1.- MODIFICAR CEDULA ")
    print(Cursor.POS(35,12)+" 2.- MODIFICAR NOMBRE ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR CARGO ")
    print(Cursor.POS(35,16)+" 4.- REGRESAR ")
    print(Cursor.POS(35,20)+("Ingrese la opcion deseada: "), end="")
def submenu_medicos_dos():
    print(Cursor.POS(35,10)+" 1.- MODIFICAR CEDULA ")
    print(Cursor.POS(35,12)+Back.CYAN+" 2.- MODIFICAR NOMBRE ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR CARGO ")
    print(Cursor.POS(35,16)+" 4.- REGRESAR ")
    print(Cursor.POS(35,20)+("Ingrese la opcion deseada: "), end="")
def submenu_medicos_tres():
    print(Cursor.POS(35,10)+" 1.- MODIFICAR CEDULA ")
    print(Cursor.POS(35,12)+" 2.- MODIFICAR NOMBRE ")
    print(Cursor.POS(35,14)+Back.CYAN+" 3.- MODIFICAR CARGO ")
    print(Cursor.POS(35,16)+" 4.- REGRESAR ")
    print(Cursor.POS(35,20)+("Ingrese la opcion deseada: "), end="")
def submenu_medicos_cuatro():
    print(Cursor.POS(35,10)+" 1.- MODIFICAR CEDULA ")
    print(Cursor.POS(35,12)+" 2.- MODIFICAR NOMBRE ")
    print(Cursor.POS(35,14)+" 3.- MODIFICAR CARGO ")
    print(Cursor.POS(35,16)+Back.CYAN+" 4.- REGRESAR ")
    print(Cursor.POS(35,20)+("Ingrese la opcion deseada: "), end="")
def modificar_cedula(cedula_medico):
    z = ['']
    x = ['']
    contador_lineas = 1
    cont = 0
    lista_codigos = []
    contador_codigo = 3
    archivo_codigo = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    for codigo in leer_codigos:
        if contador_codigo % 3 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    for o in z:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE MEDICO ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR CEDULA")
        try:
            buscar_cedula = str(input(Fore.RED+Cursor.POS(18,10)+"Cedula a modificar: "))
            if buscar_cedula+"\n" not in lista_codigos and buscar_cedula not in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  MEDICO NO ENCONTRADO  ")
                input();os.system("cls");z.append("")
            else:
                for i in x:
                    ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE MEDICO ")
                    ventana(86, 92, 8, 40, 86, 40,8, 0,"")
                    ventana(18, 92, 40, 40, 18, 35,35, 0,"")
                    print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR CEDULA")
                    try:
                        nueva_cedula_medico = str(input(Fore.CYAN+Cursor.POS(18,12)+"Nueva cedula: "))
                        if nueva_cedula_medico+"\n" in lista_codigos or nueva_cedula_medico in lista_codigos:
                            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+" CEDULA DUPLICADA  ")
                            input();os.system("cls");x.append("")
                        else:
                            x.clear();x.append("")
                            z.clear();z.append("")
                    except ValueError:
                        print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                        print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+" CEDULA INVALIDA  ")
                        input();os.system("cls");x.append("")

        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            input();os.system("cls");z.append("")
    try:
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer_lineas = archivo_medicos.readlines()
        for encontrar_id in leer_lineas:
            if encontrar_id == buscar_cedula+"\n" or encontrar_id == buscar_cedula:
                break
            else:
                contador_lineas+=1
        #se le resta uno, ya que comenzo en [0]
        contador_lineas-=1
        archivo_medicos.close()
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer_lineas_dos = archivo_medicos.readlines()
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="w",encoding="utf-8")
        for y in leer_lineas_dos:
            if cont == contador_lineas:
                archivo_medicos.write(y.replace(buscar_cedula,nueva_cedula_medico))
            else:
                archivo_medicos.write(y)
            cont+=1
    except FileNotFoundError:
        print("Archivo no encontrado y/o inexistente")
    archivo_medicos.close();input()
    z.clear()
    x.clear()
    os.system("cls")
def modificar_nombre_medico(cedula_medico):
    z = ['']
    x = ['']
    contador_lineas = 1
    cont = 0
    lista_codigos = []
    datos_medico = []
    contador_codigo = 3
    archivo_codigo = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    for codigo in leer_codigos:
        if contador_codigo % 3 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    for o in z:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE MEDICO ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR NOMBRE MEDICO")
        try:
            nueva_cedula_medico = cedula_medico()
            if nueva_cedula_medico+"\n" not in lista_codigos and nueva_cedula_medico not in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  MEDICO NO ENCONTRADO  ")
                input();os.system("cls");z.append("")
            else:
                for i in x:
                    ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE MEDICO ")
                    ventana(86, 92, 8, 40, 86, 40,8, 0,"")
                    ventana(18, 92, 40, 40, 18, 35,35, 0,"")
                    print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR NOMBRE MEDICO")
                    try:
                        nuevo_nom = str(input(Fore.CYAN+Cursor.POS(18,12)+"Nuevo nombre: "))
                        nom = nuevo_nom.replace(" ","")
                        if nom.isdigit():
                            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+" NOMBRE INVALIDO  ")
                            input();os.system("cls");x.append("")
                        else:
                            x.clear();x.append("")
                            z.clear();z.append("")
                    except ValueError:
                        print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                        print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+" NOMBRE INVALIDO  ")
                        input();os.system("cls");x.append("")

        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            input();os.system("cls");z.append("")

    try:
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer_lineas = archivo_medicos.readlines()
        for encontrar_id in leer_lineas:
            if encontrar_id == nueva_cedula_medico+"\n" or encontrar_id == nueva_cedula_medico:
                break
            else:
                contador_lineas+=1
        #se le resta uno, ya que comenzo en [0]
        contador_lineas-=1
        #limite de la info a eliminar
        limite = contador_lineas+3
        archivo_medicos.close()
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer_lineas_dos = archivo_medicos.readlines()
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="w",encoding="utf-8")
        for y in leer_lineas_dos:
            if cont < contador_lineas or cont >= limite:
                archivo_medicos.write(y)
            else:
                if "\n" not in y:
                    datos_medico.append(y+"\n")
                else:
                    datos_medico.append(y)
            cont+=1
    except FileNotFoundError:
        print("Archivo no encontrado y/o inexistente")
    datos_medico.remove(datos_medico[1])
    datos_medico.insert(1,nuevo_nom)
    archivo_medicos.close()
    #se vuelve a leer para reemplazar el nombre
    archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="a",encoding="utf-8")
    for yy in range(0,len(datos_medico)):
        archivo_medicos.write("\n"+datos_medico[yy])
    archivo_medicos.close()
    #eliminar renglones en blanco
    archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
    blanco = archivo_medicos.readlines()
    archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="w",encoding="utf-8")
    for k in blanco:
        if k != ""+"\n":
            archivo_medicos.write(k)
    archivo_medicos.close()
    z.clear()
    x.clear()
    os.system("cls")
def modificar_cargo_medico(cedula_medico):
    z = ['']
    x = ['']
    contador_lineas = 1
    cont = 0
    lista_codigos = []
    datos_medico = []
    contador_codigo = 3
    archivo_codigo = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    for codigo in leer_codigos:
        if contador_codigo % 3 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    for o in z:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE MEDICO ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR CARGO MEDICO")
        try:
            nueva_cedula_medico = cedula_medico()
            if nueva_cedula_medico+"\n" not in lista_codigos and nueva_cedula_medico not in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  MEDICO NO ENCONTRADO  ")
                input();os.system("cls");z.append("")
            else:
                for i in x:
                    ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE MEDICO ")
                    ventana(86, 92, 8, 40, 86, 40,8, 0,"")
                    ventana(18, 92, 40, 40, 18, 35,35, 0,"")
                    print(Cursor.POS(40,7)+Fore.CYAN+"MODIFICAR CARGO MEDICO")
                    try:
                        nuevo_cargo = str(input(Fore.CYAN+Cursor.POS(18,12)+"Nuevo cargo: "))
                        cargo = nuevo_cargo.replace(" ","")
                        if cargo.isdigit():
                            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+" CARGO INVALIDO  ")
                            input();os.system("cls");x.append("")
                        else:
                            x.clear();x.append("")
                            z.clear();z.append("")
                    except ValueError:
                        print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                        print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+" CARGO INVALIDO  ")
                        input();os.system("cls");x.append("")

        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            input();os.system("cls");z.append("")

    try:
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer_lineas = archivo_medicos.readlines()
        for encontrar_id in leer_lineas:
            if encontrar_id == nueva_cedula_medico+"\n" or encontrar_id == nueva_cedula_medico:
                break
            else:
                contador_lineas+=1
        #se le resta uno, ya que comenzo en [0]
        contador_lineas-=1
        #limite de la info a eliminar
        limite = contador_lineas+3
        archivo_medicos.close()
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer_lineas_dos = archivo_medicos.readlines()
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="w",encoding="utf-8")
        for y in leer_lineas_dos:
            if cont < contador_lineas or cont >= limite:
                archivo_medicos.write(y)
            else:
                if "\n" not in y:
                    datos_medico.append(y+"\n")
                else:
                    datos_medico.append(y)
            cont+=1
    except FileNotFoundError:
        print("Archivo no encontrado y/o inexistente")
    datos_medico.remove(datos_medico[2])
    datos_medico.insert(2,nuevo_cargo)
    archivo_medicos.close()
    #se vuelve a leer para reemplazar el nombre
    archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="a",encoding="utf-8")
    for yy in range(0,len(datos_medico)):
        archivo_medicos.write("\n"+datos_medico[yy])
    archivo_medicos.close()
    #eliminar renglones en blanco
    archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
    blanco = archivo_medicos.readlines()
    archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="w",encoding="utf-8")
    for k in blanco:
        if k != ""+"\n":
            archivo_medicos.write(k)
    archivo_medicos.close()
    z.clear()
    x.clear()
    os.system("cls")
def main_submenu_medicos(a=[""],b=['']):
    init(autoreset=True)
    for i in a:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DATOS DE MEDICO ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"Modificar medico")
        arc = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer = arc.read()
        if leer== '':
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  NO HAY MEDICOS  ")
            input()
            os.system("cls")
            break
        arc.close()
        opcion = 1
        submenu_medicos_uno()
        print("1")
        for i in b:    #for teclado
            tecla = ord(getch())
            if(tecla == 224):
                tecla = ord(getch())
            if(tecla == 27):
                opcion=4
                break
            if(tecla == 80 and opcion == 1):
                submenu_medicos_dos()
                opcion = 2
                print("2")
            elif(tecla == 80 and opcion == 2):
                submenu_medicos_tres()
                opcion =3
                print("3")
            elif(tecla == 80 and opcion == 3):
                submenu_medicos_cuatro()
                opcion =4
                print("4")
            elif(tecla == 80 and opcion == 4):
                submenu_medicos_uno()
                opcion =1
                print("1")
            elif(tecla == 72 and opcion == 4):
                submenu_medicos_tres()
                opcion =3
                print("3")
            elif(tecla == 72 and opcion == 3):
                submenu_medicos_dos()
                opcion =2
                print("2")
            elif(tecla == 72 and opcion == 2):
                submenu_medicos_uno()
                opcion =1
                print("1")
            elif(tecla == 72 and opcion == 1):
                submenu_medicos_cuatro()
                opcion =4
                print("4")
            elif(tecla == 13):
                break
            elif(tecla == 49):
                submenu_medicos_uno()
                opcion = 1
                print("1")
            elif(tecla == 50):
                submenu_medicos_dos()
                opcion = 2
                print("2")
            elif(tecla == 51):
                submenu_medicos_tres()
                opcion = 3
                print("3")
            elif(tecla == 52):
                submenu_medicos_cuatro()
                opcion = 4
                print("4")
            b.append("")
        if(opcion==1):
            os.system("cls")
            modificar_cedula(cedula_medico)
            a.append("")
            continue
        elif(opcion==2):
            os.system("cls")
            modificar_nombre_medico(cedula_medico)
            a.append("")
            continue
        elif(opcion==3):
            os.system("cls")
            modificar_cargo_medico(cedula_medico)
            a.append("")
            continue
        elif(opcion==4):
            a.clear()
            b.clear()
            a.append("")
            b.append("")
            os.system("cls")
            break
def ver_medicos(cedula_medico):
    init(autoreset=True)
    c = [""]
    contador_lineas = 1
    posicion = 0
    lista_codigos = []
    num_pacientes = []
    nom_pacientes = []
    diccionario_pacientes = {}
    comprobar_m =[]
    contador_codigo = 3
    mostrar = 0
    archivo_codigo = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    #agregar los id a la lista para verificar que no se repita
    for codigo in leer_codigos:
        if contador_codigo % 3 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    for o in c:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE MEDICO ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"VER MEDICO")
        arc = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer = arc.read()
        if leer== '':
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  NO HAY MEDICOS  ")
            break
        arc.close()
        try:
            nueva_cedula_medico = cedula_medico()
            if nueva_cedula_medico+"\n" not in lista_codigos and nueva_cedula_medico not in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  MEDICO NO ENCONTRADO  ")
                input();os.system("cls");c.append("")
            else:
                c.clear();c.append("")
                break

        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            input();os.system("cls");c.append("")
    try:
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer_lineas = archivo_medicos.readlines()
        for encontrar_id in leer_lineas:
            if encontrar_id == nueva_cedula_medico+"\n" or encontrar_id == nueva_cedula_medico:
                break
            else:
                contador_lineas+=1
        #se le resta uno, ya que comenzo en [0]
        contador_lineas-=1
        cont = 0
        #limite de la info a eliminar
        limite = contador_lineas+3
        archivo_medicos.close()
        #Encontra pacientes del medico
        contador_pacientes = 8
        encontrar_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_p = encontrar_pacientes.readlines()
        #agregar los id a la lista para verificar que no se repita
        for p in leer_p:
            if contador_pacientes % 8 == 0:
                if "\n" not in p:
                    num_pacientes.append(p+"\n")
                else:
                    num_pacientes.append(p)
            elif contador_pacientes % 8 == 1:
                if "\n" not in p:
                    nom_pacientes.append(p+"\n")
                else:
                    nom_pacientes.append(p)
            contador_pacientes+=1
        for k in leer_p:
            if "Medico:" in k:
                if "\n" not in k:
                    comprobar_m.append(k+"\n")
                else:
                    comprobar_m.append(k)
        encontrar_pacientes.close()
        for find in range(0,len(comprobar_m)) and range(0,len(num_pacientes)) and range(0,len(nom_pacientes)):
            try:
                if comprobar_m[find] == "Medico:"+nueva_cedula_medico+"\n":
                    encontrado = 1
                    if "\n" in num_pacientes[find] or "\n" in nom_pacientes[find]:
                        diccionario_pacientes[num_pacientes[find].replace("\n","")] = nom_pacientes[find].replace("\n","")
                    else:
                        diccionario_pacientes[num_pacientes[find]] = nom_pacientes[find]
                else:
                    encontrado = 0
            except:
                encontrado=0
        posicion_dos = 0
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer_lineas_dos = archivo_medicos.readlines()
        textof=[]
        for y in leer_lineas_dos:
            if cont >= contador_lineas and cont <= limite:
                if mostrar == 0:
                    print(Fore.RED+Cursor.POS(18,13+posicion)+"Cédula medica: "+Fore.WHITE+y)
                elif mostrar == 1:
                    print(Fore.RED+Cursor.POS(18,13+posicion)+"Nombre: "+Fore.WHITE+y)
                elif mostrar == 2:
                    print(Fore.RED+Cursor.POS(18,13+posicion)+"Cargo: "+Fore.WHITE+y)
                elif mostrar == 3:
                    print(Fore.RED+Cursor.POS(18,13+posicion)+"Pacientes:")
                    #no tiene pacientes el medico
                    if len(comprobar_m) > 0 and len(nom_pacientes) > 0 and len(num_pacientes) > 0:
                        print(Fore.CYAN+Cursor.POS(18,19)+"Numero // Nombre")
                        for id,nom in diccionario_pacientes.items():
                            print(Cursor.POS(18,21+posicion_dos)+"%s -> %s"%(id,nom))
                            posicion_dos+=2

                else:
                    if mostrar == 0:
                        print(Fore.RED+Cursor.POS(18,13+posicion)+"Cédula medica: "+Fore.WHITE+y)
                    elif mostrar == 1:
                        print(Fore.RED+Cursor.POS(18,13+posicion)+"Nombre: "+Fore.WHITE+y)
                    elif mostrar == 2:
                        print(Fore.RED+Cursor.POS(18,13+posicion)+"Cargo: "+Fore.WHITE+y)
                    elif mostrar == 3:
                        print(Fore.RED+Cursor.POS(18,13+posicion)+"Pacientes:")
                        #no tiene pacientes el medico
                        if len(comprobar_m) > 0 and len(nom_pacientes) > 0 and len(num_pacientes) > 0:
                            print(Fore.CYAN+Cursor.POS(18,19)+"Numero // Nombre")
                            for id,nom in diccionario_pacientes.items():
                                print(Cursor.POS(18,21+posicion_dos)+"%s -> %s"%(id,nom))
                                posicion_dos+=2
            else:
                if mostrar == 0:
                    print(Fore.RED+Cursor.POS(18,13+posicion)+"Cédula medica: "+Fore.WHITE+y)
                elif mostrar == 1:
                    print(Fore.RED+Cursor.POS(18,13+posicion)+"Nombre: "+Fore.WHITE+y)
                elif mostrar == 2:
                    print(Fore.RED+Cursor.POS(18,13+posicion)+"Cargo: "+Fore.WHITE+y)
                cont+=1
            mostrar+=1
            posicion+=2


    except FileNotFoundError:
        print("Archivo no encontrado y/o inexistente")
    archivo_medicos.close();input()
    c.clear()
    os.system("cls")
def modificar_analisis(numero_paciente,cedula_medico):
    init(autoreset=True)
    z = ['']
    x = ['']
    a = [""]
    contador_lineas = 1
    cont = 0
    lista_codigos = []
    datos_paciente = []
    contador_codigo = 8
    archivo_codigo = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo.readlines()
    for codigo in leer_codigos:
        if contador_codigo % 8 == 0:
            if "\n" not in codigo:
                lista_codigos.append(codigo+"\n")
            else:
                lista_codigos.append(codigo)
        contador_codigo+=1
    archivo_codigo.close()
    for o in z:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DATOS DE MEDICO ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"AGREGAR ANALISIS")
        arc = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer = arc.read()
        if leer== '':
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  NO HAY PACIENTES  ")
            z.clear()
            x.clear()
            a.clear()
            input()
            break
        arc.close()
        try:
            nuevo_num_paciente = numero_paciente()
            if str(nuevo_num_paciente)+"\n" not in lista_codigos and str(nuevo_num_paciente) not in lista_codigos:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  PACIENTE NO ENCONTRADO  ")
                input();os.system("cls");z.append("")
            else:
                x.clear();
                x.append("")
                z.clear()
                z.append("")

        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            input();os.system("cls");z.append("")

    try:
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas = archivo_pacientes.readlines()
        for encontrar_id in leer_lineas:
            if encontrar_id == str(nuevo_num_paciente)+"\n" or encontrar_id == str(nuevo_num_paciente):
                break
            else:
                contador_lineas+=1
        #se le resta uno, ya que comenzo en [0]
        contador_lineas-=1
        #limite de la info a eliminar
        limite = contador_lineas+8
        archivo_pacientes.close()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas_dos = archivo_pacientes.readlines()
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="w",encoding="utf-8")
        for y in leer_lineas_dos:
            if cont < contador_lineas or cont >= limite:
                archivo_pacientes.write(y)
            else:
                if "\n" not in y:
                    datos_paciente.append(y+"\n")
                else:
                    datos_paciente.append(y)
            cont+=1
    except FileNotFoundError:
        print("Archivo no encontrado y/o inexistente")
    archivo_pacientes.close()
    lista_codigos_m = []
    contador_codigo = 3
    mostrar = 0
    archivo_codigo_m = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
    leer_codigos = archivo_codigo_m.readlines()
    #agregar los id a la lista para verificar que no se repita
    for codigo in leer_codigos:
        if contador_codigo % 3 == 0:
            if "\n" not in codigo:
                lista_codigos_m.append(codigo+"\n")
            else:
                lista_codigos_m.append(codigo)
        contador_codigo+=1
    archivo_codigo_m.close()
    for i in a:
        ventana(13, 87, 3, 35, 13, 3,3, 4," ALTA DATOS DE MEDICO ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"AGREGAR ANALISIS")
        arc = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer = arc.read()
        if leer== '':
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  NO HAY MEDICOS  ")
            z.clear()
            x.clear()
            a.clear()
            input()
            break
        arc.close()
        print(Cursor.POS(18,10)+"Medico a hacer el analisis:")
        nueva_cedula_medico = cedula_medico()
        if nueva_cedula_medico+"\n" not in lista_codigos_m and nueva_cedula_medico not in lista_codigos_m:
            print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  MEDICO NO ENCONTRADO  ")
            input();os.system("cls");a.append("")
        else:
            resultados = str(input(Fore.CYAN+Cursor.POS(18,13)+"Resultados del analisis: "))
            datos_paciente.remove(datos_paciente[6])
            datos_paciente.insert(6,"Resultados: "+resultados)
            datos_paciente.remove(datos_paciente[7],)
            datos_paciente.insert(7,"Medico:"+nueva_cedula_medico)
            archivo_pacientes.close()
            #se vuelve a leer para reemplazar el nombre
            archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="a",encoding="utf-8")
            for yy in range(0,len(datos_paciente)):
                archivo_pacientes.write("\n"+datos_paciente[yy])
            archivo_pacientes.close()
            #eliminar renglones en blanco
            archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
            blanco = archivo_pacientes.readlines()
            archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="w",encoding="utf-8")
            for k in blanco:
                if k != ""+"\n":
                    archivo_pacientes.write(k)
            archivo_pacientes.close()
            a.clear();a.append("")
    z.clear()
    x.clear()
    a.clear()
    os.system("cls")
def alta_medicos(a=[""],b=['']):
    """ programa en donde se:
    -agrega medico
    -elimina medico
    -modifica paciente: cedula,nombre o cargo
    -ver medico
    -añadir resultados de analisis de un paciente
    -regresa al menu principal
    """
    init(autoreset=True)
    a, b = [""],[""]
    for i in a:
        opcion = 1
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE MEDICO ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        print(Cursor.POS(40,7)+Fore.CYAN+"MEDICOS")
        medicos_uno()
        print("1")
        for i in b:
            tecla = ord(getch())
            if(tecla == 224):
                tecla = ord(getch())
            if(tecla == 27):
                opcion=6
                break
            if(tecla == 80 and opcion == 1):
                medicos_dos()
                opcion = 2
                print("2")
            elif(tecla == 80 and opcion == 2):
                medicos_tres()
                opcion = 3
                print("3")
            elif(tecla == 80 and opcion == 3):
                medicos_cuatro()
                opcion = 4
                print("4")
            elif(tecla == 80 and opcion == 4):
                medicos_cinco()
                opcion = 5
                print("5")
            elif(tecla == 80 and opcion == 5):
                medicos_seis()
                opcion = 6
                print("6")
            elif(tecla == 80 and opcion == 6):
                medicos_uno()
                opcion = 1
                print("1")
            elif(tecla == 72 and opcion == 6):
                medicos_cinco()
                opcion = 5
                print("5")
            elif(tecla == 72 and opcion == 5):
                medicos_cuatro()
                opcion = 4
                print("4")
            elif(tecla == 72 and opcion == 4):
                medicos_tres()
                opcion = 3
                print("3")
            elif(tecla == 72 and opcion == 3):
                medicos_dos()
                opcion = 2
                print("2")
            elif(tecla == 72 and opcion == 2):
                medicos_uno()
                opcion = 1
                print("1")
            elif(tecla == 72 and opcion == 1):
                medicos_seis()
                opcion = 6
                print("6")
            elif(tecla == 13):
                break
            elif(tecla == 49):
                medicos_uno()
                opcion = 1
                print("1")
            elif(tecla == 50):
                medicos_dos()
                opcion = 2
                print("2")
            elif(tecla == 51):
                medicos_tres()
                opcion= 3
                print("3")
            elif(tecla == 52):
                medicos_cuatro()
                opcion = 4
                print("4")
            elif(tecla == 53):
                medicos_cinco()
                opcion = 5
                print("5")
            elif(tecla == 54):
                medicos_seis()
                opcion = 6
                print("6")
            b.append("")
        if(opcion==1):
            os.system("cls")
            registrar_medico(cedula_medico,nombre_medico,cargo_medico)
            a.append("")
            continue
        elif(opcion==2):
            os.system("cls")
            eliminar_medico(cedula_medico)
            a.append("")
            continue
        elif(opcion==3):
            os.system("cls")
            main_submenu_medicos()
            a.append("")
            continue
        elif(opcion==4):
            os.system("cls")
            ver_medicos(cedula_medico)
            a.append("")
            continue
        elif(opcion==5):
            os.system("cls")
            modificar_analisis(numero_paciente,cedula_medico)
            a.append("")
            continue
        elif(opcion==6):
            a.clear()
            b.clear()
            a.append("")
            b.append("")
            os.system("cls")
            break

###DATOS HOSPITAL###
def hospital():
    init(autoreset=True)
    cont1=2
    servicios_lista = ""
    #se abre en modo lectura
    archivo_datos = open("d05-p14-madrigal-flores-H.txt",mode="r",encoding="utf-8")
    lineas = archivo_datos.readlines()
    archivo_datos = open("d05-p14-madrigal-flores-H.txt",mode="w",encoding="utf-8")
    print(Cursor.POS(40,6)+Fore.CYAN+"DATOS DEL HOSPITAL")
    for eliminar_blanco in lineas:
        if eliminar_blanco != ""+"\n":
            archivo_datos.write(eliminar_blanco)
    archivo_datos.close()
    archivo_datos_dos = open("d05-p14-madrigal-flores-H.txt",mode="r",encoding="utf-8")
    lineas_dos = archivo_datos_dos.readlines()
    for leer in lineas_dos:
        if cont1 == 2:
            print(Cursor.POS(18,6+cont1)+"NOMBRE: "+leer)
        elif cont1 == 4:
            print(Cursor.POS(18,6+cont1)+"DIRECCION: "+leer)
        elif cont1 >= 6:
            for serv in leer.split(" "):
                if serv not in servicios_lista:
                    servicios_lista+=serv
        cont1+=2
        servicios_lista_dos = servicios_lista.replace("\n",",")
        print(Cursor.POS(18,12)+"SERVICIOS: "+servicios_lista_dos)
    archivo_datos_dos.close()
def main_h1():
    print(Cursor.POS(35,14)+Back.CYAN+" 1.- MODIFICAR NOMBRE DEL HOSPITAL ")
    print(Cursor.POS(35,16)+" 2.- MODIFICAR DIRECCION ")
    print(Cursor.POS(35,18)+" 3.- MODIFICAR SERVICIOS ")
    print(Cursor.POS(35,20)+" 4.- PACIENTES ")
    print(Cursor.POS(35,22)+" 5.- MEDICOS ")
    print(Cursor.POS(35,24)+" 6.- VOLVER AL MENU ")
    print(Cursor.POS(35,26)+("Ingrese la opcion deseada: "), end="")
def main_h2():
    print(Cursor.POS(35,14)+" 1.- MODIFICAR NOMBRE DEL HOSPITAL ")
    print(Cursor.POS(35,16)+Back.CYAN+" 2.- MODIFICAR DIRECCION ")
    print(Cursor.POS(35,18)+" 3.- MODIFICAR SERVICIOS ")
    print(Cursor.POS(35,20)+" 4.- PACIENTES ")
    print(Cursor.POS(35,22)+" 5.- MEDICOS ")
    print(Cursor.POS(35,24)+" 6.- VOLVER AL MENU ")
    print(Cursor.POS(35,26)+("Ingrese la opcion deseada: "), end="")
def main_h3():
    print(Cursor.POS(35,14)+" 1.- MODIFICAR NOMBRE DEL HOSPITAL ")
    print(Cursor.POS(35,16)+" 2.- MODIFICAR DIRECCION ")
    print(Cursor.POS(35,18)+Back.CYAN+" 3.- MODIFICAR SERVICIOS ")
    print(Cursor.POS(35,20)+" 4.- PACIENTES ")
    print(Cursor.POS(35,22)+" 5.- MEDICOS ")
    print(Cursor.POS(35,24)+" 6.- VOLVER AL MENU ")
    print(Cursor.POS(35,26)+("Ingrese la opcion deseada: "), end="")
def main_h4():
    print(Cursor.POS(35,14)+" 1.- MODIFICAR NOMBRE DEL HOSPITAL ")
    print(Cursor.POS(35,16)+" 2.- MODIFICAR DIRECCION ")
    print(Cursor.POS(35,18)+" 3.- MODIFICAR SERVICIOS " )
    print(Cursor.POS(35,20)+Back.CYAN+" 4.- PACIENTES ")
    print(Cursor.POS(35,22)+" 5.- MEDICOS ")
    print(Cursor.POS(35,24)+" 6.- VOLVER AL MENU ")
    print(Cursor.POS(35,26)+("Ingrese la opcion deseada: "), end="")
def main_h5():
    print(Cursor.POS(35,14)+" 1.- MODIFICAR NOMBRE DEL HOSPITAL ")
    print(Cursor.POS(35,16)+" 2.- MODIFICAR DIRECCION ")
    print(Cursor.POS(35,18)+" 3.- MODIFICAR SERVICIOS ")
    print(Cursor.POS(35,20)+" 4.- PACIENTES ")
    print(Cursor.POS(35,22)+Back.CYAN+" 5.- MEDICOS ")
    print(Cursor.POS(35,24)+" 6.- VOLVER AL MENU ")
    print(Cursor.POS(35,26)+("Ingrese la opcion deseada: "), end="")
def main_h6():
    print(Cursor.POS(35,14)+" 1.- MODIFICAR NOMBRE DEL HOSPITAL ")
    print(Cursor.POS(35,16)+" 2.- MODIFICAR DIRECCION ")
    print(Cursor.POS(35,18)+" 3.- MODIFICAR SERVICIOS ")
    print(Cursor.POS(35,20)+" 4.- PACIENTES ")
    print(Cursor.POS(35,22)+" 5.- MEDICOS ")
    print(Cursor.POS(35,24)+Back.CYAN+" 6.- VOLVER AL MENU ")
    print(Cursor.POS(35,26)+("Ingrese la opcion deseada: "), end="")
def modificar_nombre_hospital(contador3):
    ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE HOSPITAL ")
    ventana(86, 92, 8, 40, 86, 40,8, 0,"")
    ventana(18, 92, 40, 40, 18, 35,35, 0,"")
    #variable usada de comparacion [aux]
    print(Cursor.POS(40,6)+Fore.CYAN+"DATOS DEL HOSPITAL")
    aux = []
    archivo_datos = open("d05-p14-madrigal-flores-H.txt",mode="r",encoding="utf-8")
    lineas = archivo_datos.readlines()
    archivo_datos = open("d05-p14-madrigal-flores-H.txt",mode="w",encoding="utf-8")
    #se abre en modo escritura
    for linea in lineas:
        aux.append(linea)
    nuevo_nombre = nombre_hospital()
    #seleccionaremos el [0] que es nombre del hospital
    for linea in lineas:
        if linea != aux[0]:
            archivo_datos.write(linea)
        else:
            archivo_datos.write(linea.replace(aux[0],nuevo_nombre+"\n"))
    archivo_datos.close()
    os.system("cls")
def modificar_direccion(contador3):
    ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE HOSPITAL ")
    ventana(86, 92, 8, 40, 86, 40,8, 0,"")
    ventana(18, 92, 40, 40, 18, 35,35, 0,"")
    print(Cursor.POS(40,6)+Fore.CYAN+"DATOS DEL HOSPITAL")
    aux = []
    archivo_datos = open("d05-p14-madrigal-flores-H.txt",mode="r",encoding="utf-8")
    lineas = archivo_datos.readlines()
    archivo_datos = open("d05-p14-madrigal-flores-H.txt",mode="w",encoding="utf-8")
    for linea in lineas:
        aux.append(linea)
    nueva_direccion = direccion()
    #seleccionaremos el [1] que es la direccion del hospital
    for linea in lineas:
        if linea != aux[1]:
            archivo_datos.write(linea)
        else:
            archivo_datos.write(linea.replace(aux[1],nueva_direccion+"\n"))
    archivo_datos.close()
    os.system("cls")
def submenu1_h3():
    print(Cursor.POS(35,8)+Back.CYAN+" 1.- AGREGAR SERVICIOS ")
    print(Cursor.POS(35,10)+" 2.- ELIMINAR SERVICIO ")
    print(Cursor.POS(35,12)+" 3.- MODIFICAR SERVICIO ")
    print(Cursor.POS(35,14)+" 4.- REGRESAR ")
    print(Cursor.POS(35,25)+("Ingrese la opcion deseada: "), end="")
def submenu2_h3():
    print(Cursor.POS(35,8)+" 1.- AGREGAR SERVICIOS ")
    print(Cursor.POS(35,10)+Back.CYAN+" 2.- ELIMINAR SERVICIO ")
    print(Cursor.POS(35,12)+" 3.- MODIFICAR SERVICIO ")
    print(Cursor.POS(35,14)+" 4.- REGRESAR ")
    print(Cursor.POS(35,25)+("Ingrese la opcion deseada: "), end="")
def submenu3_h3():
    print(Cursor.POS(35,8)+" 1.- AGREGAR SERVICIOS ")
    print(Cursor.POS(35,10)+" 2.- ELIMINAR SERVICIO ")
    print(Cursor.POS(35,12)+Back.CYAN+" 3.- MODIFICAR SERVICIO ")
    print(Cursor.POS(35,14)+" 4.- REGRESAR ")
    print(Cursor.POS(35,25)+("Ingrese la opcion deseada: "), end="")
def submenu4_h3():
    print(Cursor.POS(35,8)+" 1.- AGREGAR SERVICIOS ")
    print(Cursor.POS(35,10)+" 2.- ELIMINAR SERVICIO ")
    print(Cursor.POS(35,12)+" 3.- MODIFICAR SERVICIO ")
    print(Cursor.POS(35,14)+Back.CYAN+" 4.- REGRESAR ")
    print(Cursor.POS(35,25)+("Ingrese la opcion deseada: "), end="")
def modificar_servicio_f(e=[''],f=['']):
    lista_tres = []
    aux_dos = []
    serv = []
    cont = 0
    archivo_datos = open("d05-p14-madrigal-flores-H.txt",mode="r",encoding="utf-8")
    leer1= archivo_datos.readlines()
    #se abre en modo de sobreescritura hasta el final [a]
    archivo_datos = open("d05-p14-madrigal-flores-H.txt",mode="w",encoding="utf-8")
    for line in leer1:
        if line != ""+"\n":
            archivo_datos.write(line)
    archivo_datos.close()
    archivo_d = open("d05-p14-madrigal-flores-H.txt",mode="r",encoding="utf-8")
    leer= archivo_d.readlines()
    #se abre en modo de sobreescritura hasta el final [a]
    for w in leer:
        if "\n" not in w:
            lista_tres.append(w+"\n")
        else:
            lista_tres.append(w)
    #insertar solo los servicios en la lista
    for xx in range(0,len(lista_tres)):
        if xx > 1:
            if "\n" not in lista_tres[xx]:
                aux_dos.append(lista_tres[xx]+"\n")
            else:
                aux_dos.append(lista_tres[xx])
    se = 0
    for i in range(0,len(aux_dos)):
        try:
            se+=1
            if "\n" in aux_dos[i]:
                serv.append(aux_dos[i].replace("\n",""))
            else:
                serv.append(aux_dos[i])
        except:
            se+=0
    for validar in e:
        try:
            print(Cursor.POS(40,6)+Fore.CYAN+"MODIFICAR SERVICIO")
            ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DATOS DE HOSPITAL ")
            ventana(86, 92, 8, 40, 86, 40,8, 0,"")
            ventana(18, 92, 40, 40, 18, 35,35, 0,"")
            if se == 0:
                print(Fore.RED+Cursor.POS(18,10)+"*No hay servicios aun*");input()
                break
            elif se == 1:
                print(Fore.WHITE+Cursor.POS(18,12)+"Servicios actuales"+str(serv))
                modificar_servicio = str(input(Fore.CYAN+Cursor.POS(18,10)+"Servicio a reemplazar: "))
                if modificar_servicio.upper()+"\n" not in aux_dos and modificar_servicio.upper() not in aux_dos:
                    print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                    print(Cursor.POS(21,19)+Style.BRIGHT+Fore.RED+"->"+Fore.WHITE+"El servicio no existe")
                    input();os.system("cls")
                    e.append("")
                else:
                    for validar_dos in f:
                        print(Cursor.POS(40,6)+Fore.CYAN+"MODIFICAR SERVICIO")
                        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DATOS DE HOSPITAL ")
                        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
                        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
                        try:
                            print(Cursor.POS(40,6)+Fore.CYAN+"MODIFICAR SERVICIO")
                            reemplazar_servicio = str(input(Fore.CYAN+Cursor.POS(18,11)+"Nuevo servicio: "))
                            reemplazar_servicio_dos = reemplazar_servicio.replace(" ","")
                            archivo_datos = open("d05-p14-madrigal-flores-H.txt",mode="r",encoding="utf-8")
                            l= archivo_datos.readlines()
                            #se abre en modo de sobreescritura hasta el final [a]
                            archivo_datos = open("d05-p14-madrigal-flores-H.txt",mode="w",encoding="utf-8")
                            if reemplazar_servicio_dos.isalpha() and reemplazar_servicio.upper()+"\n" not in aux_dos:
                                for line_dos in l:
                                    if line_dos != modificar_servicio.upper()+"\n" and line_dos != modificar_servicio.upper() and line_dos != modificar_servicio+"\n" and line_dos != modificar_servicio:
                                        archivo_datos.write(line_dos)
                                        os.system("cls")
                                    else:
                                        print("fallo")
                                        archivo_datos.write(line_dos.replace(modificar_servicio.upper(),reemplazar_servicio.upper()+"\n"))
                                        os.system("cls")
                            elif reemplazar_servicio_dos.isdigit():
                                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                                input();os.system("cls")
                                f.append("")
                            elif reemplazar_servicio_dos.isalpha() and reemplazar_servicio.upper()+"\n" in aux_dos:
                                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                                print(Cursor.POS(21,19)+Style.BRIGHT+Fore.RED+"->"+Fore.WHITE+"Servicio existente")
                                input();os.system("cls")
                                f.append("")
                            else:
                                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                                input();os.system("cls")
                                f.append("")
                        except ValueError:
                            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                            print(Cursor.POS(21,19)+Style.BRIGHT+Fore.RED+"->"+Fore.WHITE+"Dato invalido")
                            input();os.system("cls")
                            f.append("")
        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(21,19)+Style.BRIGHT+Fore.RED+"->"+Fore.WHITE+"Dato invalido")
            input();os.system("cls")
            e.append("")
    e.clear();e.append("")
    f.clear();f.append("")
    archivo_datos.close()
    lista_tres.clear();aux_dos.clear()
    os.system("cls")
def eliminar_servicio(contador3,c=[""]):
    se=0
    serv=[]
    aux = []
    lista_uno = []
    archivo = open("d05-p14-madrigal-flores-H.txt",mode="r")
    leer = archivo.readlines()
    archivo = open("d05-p14-madrigal-flores-H.txt",mode="w")
    for q in leer:
        if q != ""+"\n":
            archivo.write(q)
    archivo.close()
    archivo_datos = open("d05-p14-madrigal-flores-H.txt",mode="r",encoding="utf-8")
    leer1= archivo_datos.readlines()
    #se abre en modo de sobreescritura hasta el final [a]
    for validar in c:
        print(Cursor.POS(40,6)+Fore.CYAN+"ELIMINAR SERVICIO")
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DATOS DE HOSPITAL ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        for line in leer1:
            lista_uno.append(line)
        #insertar solo los servicios en la lista
        for xx in range(0,len(lista_uno)):
            if lista_uno[xx] != ""+"\n":
                if xx > 1:
                    aux.append(lista_uno[xx])
        for i in range(0,len(aux)):
            try:
                se+=1
                if "\n" in aux[i]:
                    serv.append(aux[i].replace("\n",""))
                else:
                    serv.append(aux[i])
            except:
                se+=0
        try:
            if se == 0:
                print(Fore.RED+Cursor.POS(18,10)+"*No hay servicios aun*");input()
                archivo_datos.close()
                break
            elif se == 1:
                print(Fore.CYAN+Cursor.POS(18,10)+"Servicios actuales"+str(serv))
                eliminar_servicio = str(input(Fore.CYAN+Cursor.POS(18,12)+"Servicio a eliminar: "))
                if eliminar_servicio.upper()+"\n" not in aux and eliminar_servicio.upper() not in aux:
                    print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                    print(Cursor.POS(21,19)+Style.BRIGHT+Fore.RED+"->"+Fore.WHITE+"El servicio no existe")
                    input();os.system("cls")
                    c.append("")
                else:
                    archivo_datos = open("d05-p14-madrigal-flores-H.txt",mode="w",encoding="utf-8")
                    for line_dos in leer1:
                        if line_dos != eliminar_servicio.upper()+"\n" and line_dos != eliminar_servicio.upper():
                            archivo_datos.write(line_dos.upper())
                            os.system("cls")
        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            print(Cursor.POS(21,19)+Style.BRIGHT+Fore.RED+"->"+Fore.WHITE+"Dato invalido")
            lista_uno.clear()
            input();os.system("cls")
            c.append("")
    c.clear();c.append("")
    archivo_datos.close()
    aux.clear();lista_uno.clear()
    contador3+=1
    os.system("cls")
def agregar_servicio(contador3,g=['']):
    aux_cuatro = []
    lista_cuatro = []
    cont_lineas = 0
    archivo_datos = open("d05-p14-madrigal-flores-H.txt",mode="r",encoding="utf-8")
    leer_renglones = archivo_datos.readlines()
    archivo_datos_tres = open("d05-p14-madrigal-flores-H.txt",mode="w",encoding="utf-8")
    for line in leer_renglones:
        if line != ""+"\n":
            archivo_datos_tres.write(line)
            lista_cuatro.append(line)
        cont_lineas+=1
    archivo_datos_tres.close()
    #insertar solo los servicios en la lista
    for y in range(0,len(lista_cuatro)):
        if y > 1:
            aux_cuatro.append(lista_cuatro[y])
    #se abre en modo de sobreescritura hasta el final [a]
    archivo_datos = open("d05-p14-madrigal-flores-H.txt",mode="a",encoding="utf-8")
    for val in g:
        print(Cursor.POS(40,6)+Fore.CYAN+"AGREGAR SERVICIO")
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DATOS DE HOSPITAL ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        try:
            nuevos_servicios = servicios()
            nuevos_servicios_dos = nuevos_servicios.replace(" ","")
            if nuevos_servicios.upper()+"\n" not in aux_cuatro and nuevos_servicios.upper() not in aux_cuatro and nuevos_servicios_dos.isalpha():
                archivo_datos.write("\n"+nuevos_servicios.upper())
                os.system("cls")
            else:
                print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
                input();os.system("cls")
                g.append("")

        except ValueError:
            print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
            input();os.system("cls")
            g.append("")
    g.clear();g.append("")
    archivo_datos.close()
    contador3+=1
    os.system("cls")
def main_submenu(contador3,a=[""],b=[""]):
    init(autoreset=True)
    for i in a:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DATOS DE HOSPITAL ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        opcion = 1
        print(Cursor.POS(40,6)+Fore.CYAN+"SERVICIOS")
        submenu1_h3()
        print("1")
        for i in b:    #for teclado
            tecla = ord(getch())
            if(tecla == 224):
                tecla = ord(getch())
            if(tecla == 27):
                opcion=4
                break
            if(tecla == 80 and opcion == 1):
                submenu2_h3()
                opcion = 2
                print("2")
            elif(tecla == 80 and opcion == 2):
                submenu3_h3()
                opcion = 3
                print("3")
            elif(tecla == 80 and opcion == 3):
                submenu4_h3()
                opcion = 4
                print("4")
            elif(tecla == 80 and opcion == 4):
                submenu1_h3()
                opcion = 1
                print("1")
            elif(tecla == 72 and opcion == 4):
                submenu3_h3()
                opcion = 3
                print("3")
            elif(tecla == 72 and opcion == 3):
                submenu2_h3()
                opcion = 2
                print("2")
            elif(tecla == 72 and opcion == 2):
                submenu1_h3()
                opcion = 1
                print("1")
            elif(tecla == 72 and opcion == 1):
                submenu4_h3()
                opcion = 4
                print("4")
            elif(tecla == 13):
                break
            elif(tecla == 49):
                submenu1_h3()
                opcion = 1
                print("1")
            elif(tecla == 50):
                submenu2_h3()
                opcion = 2
                print("2")
            elif(tecla == 51):
                submenu3_h3()
                opcion = 3
                print("3")
            elif(tecla == 52):
                submenu4_h3()
                opcion = 4
                print("4")
            b.append("")
        if(opcion==1):
            os.system("cls")
            agregar_servicio(contador3)
            a.append("")
            continue
        elif(opcion==2):
            os.system("cls")
            eliminar_servicio(contador3,c=[""])
            a.append("")
            continue
        elif(opcion==3):
            os.system("cls")
            modificar_servicio_f()
            a.append("")
            continue
        elif(opcion==4):
            os.system("cls")
            a.append("")
            b.append("")
            a.clear()
            b.clear()
            break
def mostrar_todos_pacientes():
    a=[""]
    datos_paciente = []
    init(autoreset=True)
    ventana(13, 87, 3, 50, 13, 3,3, 18," ALTA DE DATOS DE HOSPITAL ")
    ventana(86, 92, 8, 55, 86, 55,8, 0,"")
    ventana(18, 92, 55, 55, 18, 50,50, 0,"")
    arc = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
    leer = arc.read()
    if leer== '':
        print(Cursor.POS(30,7)+Fore.CYAN+"PACIENTES: ")
        print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
        print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  AUN NO HAY PACIENTES  ")
        arc.close()
    else:
        archivo_hospital = open("d05-p14-madrigal-flores-H.txt",mode="r",encoding="utf-8")
        nombre_hospital = archivo_hospital.readline()
        print(Cursor.POS(30,7)+Fore.CYAN+"PACIENTES DE: "+nombre_hospital)
        archivo_hospital.close()
        mostrar = 0
        posicion = 2
        archivo_pacientes = open("d05-p14-madrigal-flores-P.txt",mode="r",encoding="utf-8")
        leer_lineas_dos = archivo_pacientes.readlines()
        for y in leer_lineas_dos:
            datos_paciente.append(y)
        for datos in range(0,len(datos_paciente)):
            if mostrar == 0:
                print(Fore.RED+Cursor.POS(18,8+posicion)+"Numero de paciente: "+Fore.WHITE+datos_paciente[datos])
            elif mostrar == 1:
                print(Fore.RED+Cursor.POS(18,8+posicion)+"Nombre: "+Fore.WHITE+datos_paciente[datos])
            elif mostrar == 2:
                print(Fore.RED+Cursor.POS(18,8+posicion)+"Edad: "+Fore.WHITE+datos_paciente[datos])
            elif mostrar == 3:
                print(Fore.RED+Cursor.POS(18,8+posicion)+"Analisis: "+Fore.WHITE+datos_paciente[datos])
            elif mostrar == 4:
                print(Fore.RED+Cursor.POS(18,8+posicion)+"Antecedentes: "+Fore.WHITE+datos_paciente[datos])
            elif mostrar == 5:
                print(Fore.RED+Cursor.POS(18,8+posicion)+"Fecha de registro: "+Fore.WHITE+datos_paciente[datos])
            elif mostrar == 6:
                print(Fore.RED+Cursor.POS(18,8+posicion)+datos_paciente[datos])
            elif mostrar == 7:
                print(Fore.RED+Cursor.POS(18,8+posicion)+datos_paciente[datos])
            else:
                posicion+=1
                print(Fore.RED+Cursor.POS(18,8+posicion)+"Numero de paciente: "+Fore.WHITE+datos_paciente[datos])
                mostrar = 0
            mostrar+=1
            posicion+=1
        archivo_pacientes.close()


    input();os.system("cls")
def mostrar_todos_medicos():
    init(autoreset=True)
    ventana(13, 87, 3, 50, 13, 3,3, 18," ALTA DE DATOS DE HOSPITAL ")
    ventana(86, 92, 8, 55, 86, 55,8, 0,"")
    ventana(18, 92, 55, 55, 18, 50,50, 0,"")
    arc = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
    leer = arc.read()
    if leer== '':
        print(Cursor.POS(30,7)+Fore.CYAN+"MEDICOS: ")
        print(Cursor.POS(58,19)+Back.RED+Fore.WHITE+Style.BRIGHT+"  ERROR  ")
        print(Cursor.POS(50,21)+Back.RED+Fore.WHITE+Style.BRIGHT+"  AUN NO HAY MEDICOS ")
        arc.close()
    else:
        archivo_hospital = open("d05-p14-madrigal-flores-H.txt",mode="r",encoding="utf-8")
        nombre_hospital = archivo_hospital.readline()
        print(Cursor.POS(30,7)+Fore.CYAN+"MEDICOS DE: "+nombre_hospital)
        archivo_hospital.close()
        mostrar = 0
        posicion = 2
        archivo_medicos = open("d05-p14-madrigal-flores-M.txt",mode="r",encoding="utf-8")
        leer_lineas = archivo_medicos.readlines()
        for datos in leer_lineas:

            if mostrar == 0:
                print(Fore.RED+Cursor.POS(18,8+posicion)+"Cedula profesional: "+Fore.WHITE+datos)
            elif mostrar == 1:
                print(Fore.RED+Cursor.POS(18,8+posicion)+"Nombre: "+Fore.WHITE+datos)
            elif mostrar == 2:
                print(Fore.RED+Cursor.POS(18,8+posicion)+"Cargo: "+Fore.WHITE+datos)
            else:
                posicion+=1
                print(Fore.RED+Cursor.POS(18,8+posicion)+"Cedula profesional: "+Fore.WHITE+datos)
                mostrar = 0
            posicion+=1
            mostrar+=1

        archivo_medicos.close()
    input();os.system("cls")
def alta_datos_hospital(nombre_hospital,contador3,a=[""],b=[""]):
    """ programa en donde se:
    -modifica nombre
    -modifica DIRECCION
    -modifica servicios: agregar, eliminar, reemplazar
    -ve todos los PACIENTES
    -ve todos los medicos
    -regresa al menu principal
    """
    init(autoreset=True)
    for i in a:
        ventana(13, 87, 3, 35, 13, 3,3, 18," ALTA DE DATOS DE HOSPITAL ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        opcion = 1
        hospital()
        main_h1()
        print("1")
        for i in b:
            tecla = ord(getch())
            if(tecla == 224):
                tecla = ord(getch())
            if(tecla == 27):
                opcion=6
                break
            if(tecla == 80 and opcion == 1):
                main_h2()
                opcion = 2
                print("2")
            elif(tecla == 80 and opcion == 2):
                main_h3()
                opcion = 3
                print("3")
            elif(tecla == 80 and opcion == 3):
                main_h4()
                opcion = 4
                print("4")
            elif(tecla == 80 and opcion == 4):
                main_h5()
                opcion = 5
                print("5")
            elif(tecla == 80 and opcion == 5):
                main_h6()
                opcion = 6
                print("6")
            elif(tecla == 80 and opcion == 6):
                main_h1()
                opcion = 1
                print("1")
            elif(tecla == 72 and opcion == 6):
                main_h5()
                opcion = 5
                print("5")
            elif(tecla == 72 and opcion == 5):
                main_h4()
                opcion = 4
                print("4")
            elif(tecla == 72 and opcion == 4):
                main_h3()
                opcion = 3
                print("3")
            elif(tecla == 72 and opcion == 3):
                main_h2()
                opcion = 2
                print("2")
            elif(tecla == 72 and opcion == 2):
                main_h1()
                opcion = 1
                print("1")
            elif(tecla == 72 and opcion == 1):
                main_h6()
                opcion = 6
                print("6")
            elif(tecla == 13):
                break
            elif(tecla == 49):
                main_h1()
                opcion = 1
                print("1")
            elif(tecla == 50):
                main_h2()
                opcion = 2
                print("2")
            elif(tecla == 51):
                main_h3()
                opcion= 3
                print("3")
            elif(tecla == 52):
                main_h4()
                opcion = 4
                print("4")
            elif(tecla == 53):
                main_h5()
                opcion = 5
                print("5")
            elif(tecla == 54):
                main_h6()
                opcion = 6
                print("6")
            b.append("")
        if(opcion==1):
            os.system("cls")
            modificar_nombre_hospital(contador3)
            a.append("")
            continue
        elif(opcion==2):
            os.system("cls")
            modificar_direccion(contador3)
            a.append("")
            continue
        elif(opcion==3):
            os.system("cls")
            main_submenu(contador3,a=[""],b=[""])
            a.append("")
            continue
        elif(opcion==4):
            os.system("cls")
            mostrar_todos_pacientes()
            a.append("")
            continue
        elif(opcion==5):
            os.system("cls")
            mostrar_todos_medicos()
            a.append("")
            continue
        elif(opcion==6):
            a.clear()
            b.clear()
            a.append("")
            b.append("")
            os.system("cls")
            break

###MENU PRINCIPAL###
def mostrar_nombre_hospital():
    try:
        archivo_hospital = open("d05-p14-madrigal-flores-H.txt",mode="r",encoding="utf-8")
        leer_hospital = archivo_hospital.readline()
    except FileNotFoundError:
        print(f"No se ha podido cargar el archivo")

    return leer_hospital
    archivo_hospital.close()
def m1():
    print(Cursor.POS(35,12)+Back.CYAN+" 1.- ALTA DE PACIENTES ")
    print(Cursor.POS(35,14)+" 2.- ALTA DE MEDICOS ")
    print(Cursor.POS(35,16)+" 3.- ALTA DE DATOS DE HOSPITAL ")
    print(Cursor.POS(35,18)+" 4.- SALIR ")
    print(Cursor.POS(35,23)+("Ingrese la opcion deseada: "), end="")
def m2():
    print(Cursor.POS(35,12)+" 1.- ALTA DE PACIENTES ")
    print(Cursor.POS(35,14)+Back.CYAN+" 2.- ALTA DE MEDICOS ")
    print(Cursor.POS(35,16)+" 3.- ALTA DE DATOS DE HOSPITAL ")
    print(Cursor.POS(35,18)+" 4.- SALIR ")
    print(Cursor.POS(35,23)+("Ingrese la opcion deseada: "), end="")
def m3():
    print(Cursor.POS(35,12)+" 1.- ALTA DE PACIENTES ")
    print(Cursor.POS(35,14)+" 2.- ALTA DE MEDICOS ")
    print(Cursor.POS(35,16)+Back.CYAN+" 3.- ALTA DE DATOS DE HOSPITAL ")
    print(Cursor.POS(35,18)+" 4.- SALIR ")
    print(Cursor.POS(35,23)+("Ingrese la opcion deseada: "), end="")
def m4():
    print(Cursor.POS(35,12)+" 1.- ALTA DE PACIENTES ")
    print(Cursor.POS(35,14)+" 2.- ALTA DE MEDICOS ")
    print(Cursor.POS(35,16)+" 3.- ALTA DE DATOS DE HOSPITAL ")
    print(Cursor.POS(35,18)+Back.CYAN+" 4.- SALIR ")
    print(Cursor.POS(35,23)+("Ingrese la opcion deseada: "), end="")
def despedida():
    init(autoreset=True)
    name= mostrar_nombre_hospital()
    print(Cursor.POS(20,5)+Back.CYAN+("----------------------------------------"))
    print(Cursor.POS(20,11)+Back.CYAN+("----------------------------------------"))
    print(Cursor.POS(24,7)+Back.CYAN+(" GRACIAS POR CONFIAR EN NOSOTROS "))
    print(Cursor.POS(33,8)+Back.CYAN+(" ")+name)
    print(Cursor.POS(28,9)+Back.CYAN+(" AGRADECE TU PREFERENCIA "))
    print("")
def menu(a=[""],contador3=0,b=['']):
    """programa que es el menu principal donde se va a poder elegir:
    -alta de PACIENTES: se agrega, elimina o modifica paciente
    -alta de medicos: se agrega, elimina o modifca medico y agrega el analisis de un paciente
    -alta datos de HOSPITAL: se modifica nombre, direccion,servicios
    -salir del programa
    """
    init(autoreset=True)
    lista = []
    c=['']
    for i in a:
        ventana(13, 87, 3, 35, 13, 3,3, 4," MENU ")
        ventana(86, 92, 8, 40, 86, 40,8, 0,"")
        ventana(18, 92, 40, 40, 18, 35,35, 0,"")
        #print(Cursor.POS(30,4)+Style.BRIGHT+Fore.BLUE+"practica 14")
        print(Cursor.POS(15,5)+Style.BRIGHT+Fore.BLUE+"madrigal escoto miguel arturo")
        print(Cursor.POS(15,6)+Style.BRIGHT+Fore.BLUE+"flores ontiveros aide sarahi")
        print(Cursor.POS(15,7)+Style.BRIGHT+Fore.BLUE+"--- PythonCracks ---")
        name=mostrar_nombre_hospital()
        print(Cursor.POS(40,9)+name)
        opcion = 1
        num = 0
        m1()
        print("1")
        for i in b:    #for teclado
            tecla = ord(getch())
            if(tecla == 224):
                tecla = ord(getch())
            if(tecla == 27):
                opcion=4
                break
            #para abajo
            if(tecla == 80 and opcion == 1):
                m2()
                opcion = 2
                print("2")
            elif(tecla == 80 and opcion == 2):
                m3()
                opcion = 3
                print("3")
            elif(tecla == 80 and opcion == 3):
                m4()
                opcion = 4
                print("4")
            elif(tecla == 80 and opcion == 4):
                m1()
                opcion = 1
                print("1")
            #para arriba
            elif(tecla == 72 and opcion == 4):
                m3()
                opcion = 3
                print("3")
            elif(tecla == 72 and opcion == 3):
                m2()
                opcion = 2
                print("2")
            elif(tecla == 72 and opcion == 2):
                m1()
                opcion = 1
                print("1")
            elif(tecla == 72 and opcion == 1):
                m4()
                opcion = 4
                print("4")
            elif(tecla == 13):
                break
            if(tecla == 49):
                m1()
                opcion = 1
                print("1")
            elif(tecla == 50):
                m2()
                opcion = 2
                print("2")
            elif(tecla == 51):
                m3()
                opcion = 3
                print("3")
            elif(tecla == 52):
                m4()
                opcion = 4
                print("4")
            b.append("")
        if(opcion==1):
            os.system("cls")
            alta_pacientes()
            a.append("")
            continue
        elif(opcion==2):
            os.system("cls")
            alta_medicos()
            a.append("")
            continue
        elif(opcion==3):
            os.system("cls")
            alta_datos_hospital(nombre_hospital,contador3)
            a.append("")
            continue
        elif(opcion==4):
            os.system("cls")
            a.append("")
            b.append("")
            a.clear()
            b.clear()
            despedida()
            break

    return contador3
menu()
