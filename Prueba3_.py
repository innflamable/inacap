from os import system
system('cls')

# variables menu
Opc = 0
Operacion = ''
i = 0

# inicializacion de variables ejercicio 1
Rutt = ''
SBase = 0
Bono = 0
Aguinaldo = 0
Grati = 0
Afp = 0 
Anticipo = 0
Sliquido = 0
St = 0

# inicializacion de variables ejercicio 2
Nomm =''
Asig =''
Not1 = 0
Not2 = 0
Not3 = 0
Examen = 0
Situ =''
PFinal = 0
PNot1 = 0
PNot2 = 0
PNot3 = 0
Promm = 0
Prom80 = 0
Exam20 = 0
PFinal = 0
AcumPr = 0

# iniciacion de variables ejercicio 3
VEntr = 0
FPago = ''
NEntr = 0
TPa = 0
Inter = 0
Dscto = 0

while(Opc <1 or Opc >4):
    from os import system 
    system("cls")
    print("     .... MENU DE OPCIONES ....")
    print("===================================")
    print("   1.- Programa calculo de sueldo  ")
    print("   2.- Programa calculo promedio ")
    print("   3.- Programa venta de entradas concierto Guns N' Roses")
    print("   4.- Autor del programa ")
    print("")

    Opc = int(input("   Ingrese opciones (1-4) : "));
    print("")

def MuestraDeDatos1():
    print()
    print( ' .... MUESTRA DE DATOS DEL TRABAJADOR',i,'.... ')
    print('================================================')
    print('El rut del trabajador es...................: ',Rutt)
    print('El sueldo base del tabajador es............: ',SBase)
    print('El bono del trabajador es..................: ',Bono)
    print('La gratificacion del trabajador es.........: ',Grati)
    print('El afp del trabajador es...................: ',Afp)
    print('El anticipo del trabajador es..............: ',Anticipo)
    print('El sueldo liquido del trabajador es........: ',Sliquido)
def CalculoDatos():
    global Rutt
    global Nomm
    global Asig
    global Not1
    global Not2
    global Not3
    global Examen
    global Situ
    global PFinal


    Rutt = input('ingrese el rut del alumno.........: ')
    Nomm = input('ingrese el nombre del alumno......: ')
    Asig = input('ingrese la asignatura del alumno..: ')
    Not1 = int(input('ingrese la nota 1 del alumno......: '))
    while(Not1 <10 or Not1 >70):
        print('')
        print('Error!!!!, la nota 1 debe ser >10 y <70')
        Not1 = int(input('Vuelva a ingresar la nota 1: '))
    Not2 = int(input('ingrese la nota 2 del alumno......: '))
    while(Not2 <10 or Not2 >70):
         print('')
         print('Error!!!!, la nota 2 debe ser >10 y <70')
         Not2 = int(input('Vuelva a ingresar la nota 2: '))
    Not3 = int(input('ingrese la nota 3 del alumno......: '))
    while(Not3 <10 or Not3 >70):
        print('')
        print('Error!!!!, la nota 3 debe ser >10 y <70')
        Not3 = int(input('Vuelva a ingresar la nota 3: '))
    Examen = int(input('ingrese la nota del examen........: '))
    while(Examen <10 or Examen >70):
        print('')
        print('Error!!!!, la nota del examen debe ser >10 y <70')
        Examen = int(input('Vuelva a ingresar la nota del examen: '))

     #CALCULOS
    global PNot1
    global PNot2
    global PNot3
    global Promm
    global Prom80
    global Exam20
            
    PNot1 = ((Not1*15)/100)
    PNot2 = ((Not2*35)/100)
    PNot3 = ((Not3*50)/100)
    Promm = (PNot1 + PNot2 + PNot3)
    Prom80 = ((Promm*80)/100)
    Exam20 = ((Examen*20)/100)
    PFinal = (Prom80 + Exam20)
                
    # CALCULO SITUACION

    if(PFinal >10 and PFinal <40):
        Situ = 'Reprobado'
    elif(PFinal >=40 and PFinal <55):
        Situ = 'Aprobado'
    elif(PFinal >=55):
        Situ = 'Eximido'       
def MuestraDatos2():
    print('')
    print(' .... MUESTRA DE DATOS .... ')
    print('============================')
    print('El rut del alumno es...........: ',Rutt)
    print('El nombre del alumno es........: ',Nomm)
    print('La asignatura del alumno es....: ',Asig)
    print('La nota 1 del alumno es........: ',Not1,'y su 15% equivale a: ',PNot1)
    print('La nota 2 del alumno es........: ',Not2,'y su 35% equivale a: ',PNot2)
    print('La nota 3 del alumno es........: ',Not3,'y su 50% equivale a: ',PNot3)
    print('El promedio es.................: ',Promm,' y su 80% equivale a:',Prom80)
    print('La nota del examen es..........: ',Examen,'y su 20% equivale a:',Exam20)
    print('El promedio final del alumno es: ',PFinal)
    print('La situacion del alumno es.....: ',Situ)
def MuestraDatos3():
    print('')
    print(' .... MUESTRA DE DATOS .... ')
    print('============================')
    print('El rut del cliente es..........:',Rutt)
    print('EL nombre del cliente es.......:',Nomm)
    print('El valor de la entrada es......:',VEntr)
    print('Total de entradas compradas es.:',NEntr)
    print('La forma de pago es............:',FPago,'y el total es:',Total)
    print('El descuento es................:',Dscto)
    print('El interes es..................:',Inter)
    print('El total a pagar es............:',TPa)

# INGRESO DE DATOS EJERCICIO 1

if (Opc == 1):
    for i in range(1,4,1):
        print("")
        print(" .... Trabajador N°",i, "....");
        print("=============================")
        Operacion = ('Ud selecciono calculo de sueldo')
        Rutt = input('ingrese su rut.............: ')
        SBase = int(input('ingrese su sueldo base.....: '))
        Aguinaldo = int(input('ingrese su aguinaldo.......: '))
        Anticipo = int(input('ingrese su anticipo........: '))
        # CALCULO DE BONO
        Bono = ((SBase*30)/100)

        # CALCULO DE GRATIFICACION
        if (SBase < 280000):
            Grati = 70000
        
        elif (SBase >= 280000):
            Grati = 40000
        
        St = (SBase + Bono + Grati)
        
        # CALCULO AFP
        Afp = ((St*15)/100)

        #CALCULO SUELDO LIQUIDO
        Sliquido = (St - Afp - Anticipo)

        MuestraDeDatos1();

#INGRESO DE DATOS EJERCICIO 2
if (Opc == 2):
    for i in range(1,4,1):
        print('')
        print(" .... Alumno N°",i, "....");
        print("=========================")
        CalculoDatos();
        MuestraDatos2();

#INGRESO DE DATOS EJERCICIO 3
if (Opc == 3):
    
    for i in range (1,4,1):
        print('')
        print(" .... Cliente N°",i, "....");
        print("=================+========")
        
        Rutt = input('ingrese su rut...................: ')
        Nomm = input('ingrese su nombre................: ')
        VEntr = int(input('ingrese el valor de las entradas.: '))
        NEntr = int(input('ingrese el numero de entradas....: '))
        while (NEntr > 3):
            print('')
            print('ERROR! solo se pueden vender hasta 3 entradas por persona')
            NEntr = int(input('ingrese nuevamente el numero de entradas: '))
        FPago = input('ingrese la forma de pago.........: ')

        # Caluculo 
        
        Total = (VEntr*NEntr)
        if (FPago == 'Efectivo'):
            Dscto = ((Total*20)/100)
        elif (FPago == 'TarjetaBanco'):
            Dscto = ((Total*10)/100)
        elif (FPago == 'TarjetaTienda'):
            Inter = ((Total*10)/100)
        elif(FPago == 'Cheque'):
            Inter = ((Total*20)/100)

        TPa = ((Total - Dscto) + Inter)

        MuestraDatos3();

# MUESTRA DE DATOS EJERCICIO 4

if (Opc == 4):
    print('Nombre autor............: Alexis Carmona')
    print('Nombre carrera..........: Ingeneria en informatica')
    print('Nombre asignatura.......: Introduccion a la programacion')
    print('Fecha creacion..........: 19-06-2022')
    print('Nombre profesor.........: Cesar Arce')
    print('')
    print('')
    

print(' .....::::ESTAS FUERA DEL PROGRAMA::::..... ')
print('\n \n')
print('                    👻')
print('\n \n \n')
