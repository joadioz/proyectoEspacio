from colorama import Fore  
def Mostrar():
    cont =0
    Archivo = open("ObservacionLuco.txt","r")
    linea = Archivo.readlines()
    if linea is not None:
        for kk in linea:
            cont += 1
            dodo=kk.split(',')
            print(Fore.YELLOW+"------------------------------------------------------------")
            print(Fore.BLUE+  "----------------|Día "+dodo[0] + " Mes " + dodo[1] + " Año " + dodo[2]+"|--------------------- ")
            print(Fore.YELLOW+"------------------------------------------------------------")
            print(Fore.GREEN+" Observacion de luminosidad en el sector 1.º  del cielo: "+dodo[3])
            print(Fore.GREEN+" Observacion de luminosidad en el sector 2.º  del cielo: "+dodo[4])
            print(Fore.GREEN+" Observacion de luminosidad en el sector 3.º  del cielo: "+dodo[5])
            print(Fore.GREEN+" Observacion de luminosidad en el sector 4.º  del cielo: "+dodo[6])
            print(Fore.GREEN+" Observacion de luminosidad en el sector 5.º  del cielo: "+dodo[7])
            print(Fore.GREEN+" Observacion de luminosidad en el sector 6.º  del cielo: "+dodo[8])
            print(Fore.GREEN+" Observacion de luminosidad en el sector 7.º  del cielo: "+dodo[9])
            print(Fore.GREEN+" Observacion de luminosidad en el sector 8.º  del cielo: "+dodo[10])
            print(Fore.GREEN+" Observacion de luminosidad en el sector 9.º  del cielo: "+dodo[11])
            print(Fore.GREEN+" Observacion de luminosidad en el sector 10.º del cielo: "+dodo[12])
            print(Fore.GREEN+" Observacion de luminosidad en el sector 11.º del cielo: "+dodo[13])
            print(Fore.GREEN+" Observacion de luminosidad en el sector 12.º del cielo: "+dodo[14])
            print(Fore.GREEN+" Observacion de luminosidad en el sector 13.º del cielo: "+dodo[15])
            print(Fore.GREEN+" Observacion de luminosidad en el sector 14.º del cielo: "+dodo[16])
    Archivo.close()
def SuperNova(imprimir):
    cont=2
    cantidadTotal=0
    Archivo = open("ObservacionLuco.txt","r")
    linea = Archivo.readlines()
    dodo=linea[0].split(',')
    for kk in range(3,len(dodo)):
        cont+=1
        cantidad="cantidad"+str(cont)
        cantidad= RemplazadorSuperNova(cont,"e2nergia"+str(cont),"verdad"+str(cont),"cont"+str(cont),"energia"+str(cont),imprimir)
        cantidadTotal=cantidad+cantidadTotal
    print(Fore.LIGHTCYAN_EX+"Total de SuperNovas encontradas: "+ str(cantidadTotal))
    Archivo.close()
    if(imprimir==1):
        archivo2=open("Resultados.txt","a")
        archivo2.write("\n Total de SuperNovas encontradas: "+ str(cantidadTotal)+"\n")
        archivo2.write("--------------------------------------------------------------\n")
        archivo2.close()

def RemplazadorSuperNova(numerillo,e2nergia,verdad,conto,energia,imprimir):
    Archivo = open("ObservacionLuco.txt","r")
    linea = Archivo.readlines()
    supernova = 0
    verdad=0
    conto=0
    cont =0
    if linea is not None:
        for data in linea:
            dodo=data.split(',')
            cont += 1
            e2nergia=dodo[numerillo]
            e2nergia= int(e2nergia)
            energia=dodo[numerillo]
            energia= int(energia)
            if energia > 70:
                conto+=1
                if conto == 10:
                    for i in range(cont,len(linea)):
                        dodo=linea[i].split(',')
                        energia=dodo[numerillo]
                        energia= int(energia)
                        if(energia==0 or energia==e2nergia):
                            verdad+=1
                        if((verdad + cont) == len(linea)):
                            if(energia == 0):
                                supernova+=1
                                if(imprimir==1):
                                    archivo2=open("Resultados.txt","a")
                                    archivo2.write("Una super nova en sector "+str(numerillo-2)+".º del cielo\n")
                                    
                                print(Fore.YELLOW+"Una super nova en sector "+str(numerillo-2)+".º del cielo")
                            verdad=0
    Archivo.close()
    
    return supernova

def Quazar(imprimir):
    cont=2
    cantidadTotal=0
    Archivo = open("ObservacionLuco.txt","r")
    linea = Archivo.readlines()
    dodo=linea[0].split(',')
    for kk in range(3,len(dodo)):
        cont+=1
        cantidad="cantidad"+str(cont)
        cantidad= RemplazadorQuazar(cont,"e2nergia"+str(cont),"verdad"+str(cont),"cont"+str(cont),"energia"+str(cont),imprimir)
        cantidadTotal=cantidad+cantidadTotal
    print(Fore.LIGHTCYAN_EX+"Quazar total encontrados: "+ str(cantidadTotal))
    
    Archivo.close()
    if(imprimir==1):
        archivo2=open("Resultados.txt","a")
        archivo2.write("\n Quazar total encontrados: "+ str(cantidadTotal)+"\n")
        archivo2.write("--------------------------------------------------------------\n")
        archivo2.close()

def RemplazadorQuazar(numerillo,e2nergia,verdad,conto,energia,imprimir):
    verdad=0
    conto=0
    quazar=0
    cont =0
    Archivo = open("ObservacionLuco.txt","r")
    linea = Archivo.readlines()
    if linea is not None:
        for data in linea:
            dodo=data.split(',')
            cont += 1
            e2nergia=dodo[numerillo]
            e2nergia= int(e2nergia)
            energia=dodo[numerillo]
            energia= int(energia)
            if energia > 70:
                if(conto==0):
                    dia=dodo[0]
                    dia= int(dia)
                    año=dodo[2]
                    año= int(año)
                    mes=dodo[1]
                    mes= int(mes)
                conto+=1
                if conto == 10:
                    for i in range(cont,len(linea)):
                        dodo=linea[i].split(',')
                        energia=dodo[numerillo]
                        energia= int(energia)
                        if( energia==e2nergia):
                            verdad+=1
                        if((verdad + cont) == 60):
                            if(energia == e2nergia):
                                quazar+=1
                                if(imprimir==1):
                                    archivo2=open("Resultados.txt","a")
                                    archivo2.write("\nQuazar encontrado en la zona "+ str(numerillo-2)+ "º del Día "+str(dia) + " Mes " + str(mes) + " Año " + str(año)+"\n")
                                print(Fore.YELLOW+"Quazar encontrado en la zona "+ str(numerillo-2)+ "º del Día "+str(dia) + " Mes " + str(mes) + " Año " + str(año))
                            verdad=0
                  
    Archivo.close()
    return quazar 

def Planeta(imprimir):    
    cont=2
    cantidadTotal=0
    Archivo = open("ObservacionLuco.txt","r")
    linea = Archivo.readlines()
    dodo=linea[0].split(',')
    for kk in range(3,len(dodo)):
        cont+=1
        cantidad="cantidad"+str(cont)
        cantidad= RemplazadorPlaneta(cont,"e2nergia"+str(cont),"verdad"+str(cont),"conto"+str(cont),"energia"+str(cont),imprimir)
        cantidadTotal=cantidad+cantidadTotal
    print(Fore.LIGHTCYAN_EX+"Planetas total encontrados: "+ str(cantidadTotal))
    Archivo.close()
    if(imprimir==1):
        archivo2=open("Resultados.txt","a")
        archivo2.write("\n Planetas total encontrados: "+ str(cantidadTotal)+"\n")
        archivo2.write("--------------------------------------------------------------\n")
        archivo2.close()

def RemplazadorPlaneta(numerillo,e2nergia,verdad,conto,energia,imprimir):
    verdad=0
    conto=0
    planeta=0
    cont =0
    e2nergia=0
    contZero=0
    kk=0
    Archivo = open("ObservacionLuco.txt","r")
    linea = Archivo.readlines()
    if linea is not None:
        for data in linea:
            dodo=data.split(',')
            cont += 1
            energia=dodo[numerillo]
            energia= int(energia)
            if energia > 0 and kk==0:
                e2nergia=dodo[numerillo]
                e2nergia= int(e2nergia)
                kk=1
            if energia > 0 and e2nergia != energia and kk==1:
                kk=2
            if energia ==0 and e2nergia > 0 and kk!=2:
                conto+=1
                if conto == 2:
                    for i in range(cont,len(linea)):
                        dodo=linea[i].split(',')
                        energia=dodo[numerillo]
                        energia= int(energia)
                        if(energia==0):
                            contZero+=1
                        if(contZero==2):
                            verdad+=2
                            contZero=0
                        if((energia==e2nergia) and (energia > 0)):
                            verdad+=1
                        if((verdad + cont) == 60):
                            planeta+=1
                            print(Fore.YELLOW+"Planeta encontrado en la zona "+ str(numerillo-2)+"º del cielo")
                            if(imprimir==1):
                                    archivo2=open("Resultados.txt","a")
                                    archivo2.write("Planeta encontrado en la zona "+ str(numerillo-2)+".º del cielo\n")
                            verdad=0
                            contZero+=0 
    Archivo.close()
    return planeta 

def Pulsar(imprimir):
    cont=2
    cantidadTotal=0
    Archivo = open("ObservacionLuco.txt","r")
    linea = Archivo.readlines()
    dodo=linea[0].split(',')
    for kk in range(3,len(dodo)):
        cont+=1
        cantidad="cantidad"+str(cont)
        cantidad= RemplazadorPulsar(cont,"e2nergia"+str(cont),"verdad"+str(cont),"conto"+str(cont),"energia"+str(cont),imprimir)
        cantidadTotal=cantidad+cantidadTotal
    print(Fore.LIGHTCYAN_EX+"Pulsar total encontrados: "+ str(cantidadTotal))
    Archivo.close()
    if(imprimir==1):
        archivo2=open("Resultados.txt","a")
        archivo2.write("\n Pulsar total encontrados: "+ str(cantidadTotal)+"\n")
        archivo2.write("--------------------------------------------------------------\n")
        archivo2.close()

def RemplazadorPulsar(numerillo,e2nergia,verdad,conto,energia,imprimir):
    verdad=0
    conto=0
    pulsar=0
    cont =0
    e2nergia=0
    contZero=0
    kk=0
    Archivo = open("ObservacionLuco.txt","r")
    linea = Archivo.readlines()
    if linea is not None:
        for data in linea:
            dodo=data.split(',')
            cont += 1
            energia=dodo[numerillo]
            energia= int(energia)
            if energia > 0 and energia < 80:
                e2nergia=dodo[numerillo] # e2nergia=45
                e2nergia= int(e2nergia)
                kk+=1
            if energia > 80 and  kk>6:
                conto+=1
                if conto == 7:
                    for i in range(cont,len(linea)):
                        dodo=linea[i].split(',')
                        energia=dodo[numerillo]
                        energia= int(energia)
                        if(energia == 0):
                            contZero+=1
                        if(contZero > 10):
                            verdad=0
                        verdad+=1
                        if((verdad + cont) == 60):
                            pulsar+=1
                            if(imprimir==1):
                                    archivo2=open("Resultados.txt","a")
                                    archivo2.write("Pulsar encontrado en la zona "+ str(numerillo-2)+".º del cielo\n")
                            print(Fore.YELLOW+"Pulsar encontrado en la zona "+ str(numerillo-2))
                            verdad=0
                            contZero+=0 
    Archivo.close()
    return pulsar

            
def CrearTxt():
    archivo=open("Resultados.txt","w")
    SuperNova(1)
    Pulsar(1)
    Planeta(1)
    Quazar(1)
    archivo.close()
def Menu():
    print(Fore.RED+"  ------------------")
    print(Fore.RED+" |    "+Fore.WHITE+" Opciones "+Fore.RED+"    |")
    print(Fore.RED+"----------------------")
    print(Fore.RED+" | "+Fore.RED+"1-"+Fore.YELLOW+"SuperNovas"+Fore.RED+"     |")
    print(Fore.RED+" | "+Fore.RED+"2-"+Fore.YELLOW+"Quazar"+Fore.RED+"         |")
    print(Fore.RED+" | "+Fore.RED+"3-"+Fore.YELLOW+"Planeta"+Fore.RED+"        |")
    print(Fore.RED+" | "+Fore.RED+"4-"+Fore.YELLOW+"Pulsar"+Fore.RED+"         |")
    print(Fore.RED+" | "+Fore.RED+"5-"+Fore.YELLOW+"Mostrar"+Fore.RED+"        |")
    print(Fore.RED+" | "+Fore.RED+"6-"+Fore.YELLOW+"Ver informes"+Fore.RED+"   |")
    print(Fore.RED+" | "+Fore.RED+"7-"+Fore.YELLOW+"Informe en txt"+Fore.RED+" |")
    print(Fore.RED+" | "+Fore.RED+"8-"+Fore.YELLOW+"Salir"+Fore.RED+"          |")
    print(Fore.RED+"----------------------")

Menu()
koko=True
while koko==True:
    op = int(input(Fore.GREEN+"Opcion: "+Fore.YELLOW))
    if op == 1:
        SuperNova(0)       
    elif op == 2:
        Quazar(0)
    elif op == 3:
        Planeta(0)
    elif op == 4:
        Pulsar(0)
    elif op == 5:
        Mostrar()
        print(Fore.YELLOW+"¿Desea ver los informes?")
        print(Fore.RED+"1-Si | 2-No")
        opo=3
        while opo==3:
            opa = int(input(Fore.YELLOW+"Opcion: "))
            if opo is None:
                opo==3
                print("Solo se permite usar el '1' y el '2'")
            if opa == 1:
                SuperNova(0)
                Quazar(0)
                Planeta(0)
                Pulsar(0)
                opo=4
                Menu()
            elif opa == 2:
                Menu()
                opo=4
    elif op == 6:
        SuperNova(0)
        Quazar(0)
        Planeta(0)
        Pulsar(0)
    elif op == 7:
        CrearTxt()
    elif op == 8:
        print("Adios")
        koko = False
    elif op > 8 or op is None:
        print("Solo se permiten numeros del menu (1-8)")
        koko = True
    

        

    
