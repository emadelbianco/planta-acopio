from time import sleep
import datetime 
import os
import os.path
import pickle
from traceback import print_tb
from colorama import init, Back, Fore

class Operacion:
    def __init__(self):
        self.patente = ""
        self.cod_prod = 0
        self.fecha_cupo = ""
        self.estado = ""
        self.bruto = 0
        self.tara = 0

class Producto:
    def __init__(self):
        self.cod_prod = 0
        self.nombre = ""
        self.cami = 0
        self.stock = 0
        self.alta = True

class Rubro:
    def __init__(self):
        self.cod_rubro = 0
        self.nombre = ""

class Rubro_por_producto:
    def __init__(self):
        self.cod_rubro = 0
        self.cod_prod = 0
        self.min = 0
        self.max = 0

class Silo:
    def __init__(self):
        self.cod_silo = 0
        self.nombre = ""
        self.cod_prod = 0
        self.stock = 0

def limpiarConsola():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def limpiar():
    sleep(1.25)
    limpiarConsola()

def menu():
    limpiarConsola()
    print (Fore.WHITE + Back.YELLOW +"####################################")
    print (Fore.WHITE + Back.YELLOW +"    PLANTA DE ACOPIO DE CEREALES    ")
    print (Fore.WHITE + Back.YELLOW +"####################################\n")
    print (Fore.GREEN + Back.WHITE +"1. ADMINISTRACIONES                 ")
    print (Fore.GREEN + Back.WHITE +"2. ENTREGA DE CUPOS                 ")
    print (Fore.GREEN + Back.WHITE +"3. RECEPCIÓN                        ")
    print (Fore.GREEN + Back.WHITE +"4. REGISTRAR CALIDAD                ")
    print (Fore.GREEN + Back.WHITE +"5. REGISTRAR PESO BRUTO             ")
    print (Fore.GREEN + Back.WHITE +"6. REGISTRAR DESCARGA               ")
    print (Fore.GREEN + Back.WHITE +"7. REGISTRAR TARA                   ")
    print (Fore.GREEN + Back.WHITE +"8. REPORTES                         ")
    print (Fore.GREEN + Back.WHITE +"9. LISTADO DE SILOS Y RECHAZOS      ")
    print (Fore.GREEN + Back.WHITE +"0. FIN DEL PROGRAMA                 \n")

def menu2():
    limpiarConsola()
    print (Fore.WHITE + Back.YELLOW +"     ADMINISTRACIONES      \n")
    print (Fore.GREEN + Back.WHITE +"A. TITULARES               ")
    print (Fore.GREEN + Back.WHITE +"B. PRODUCTOS               ")
    print (Fore.GREEN + Back.WHITE +"C. RUBROS                  ")
    print (Fore.GREEN + Back.WHITE +"D. RUBROS POR PRODUCTO     ")
    print (Fore.GREEN + Back.WHITE +"E. SILOS                   ")
    print (Fore.GREEN + Back.WHITE +"F. SUCURSALES              ")
    print (Fore.GREEN + Back.WHITE +"G. PRODUCTO POR TITULAR    ")
    print (Fore.GREEN + Back.WHITE +"V. VOLVER AL MENÚ PRINCIPAL\n") 

def menu3():
    print(Fore.WHITE + Back.YELLOW +'         PRODUCTOS        \n')
    print (Fore.GREEN + Back.WHITE +"A. ALTA                   ")
    print (Fore.GREEN + Back.WHITE +"B. BAJA                   ")
    print (Fore.GREEN + Back.WHITE +"C. CONSULTA               ")
    print (Fore.GREEN + Back.WHITE +"M. MODIFICACION           ")
    print (Fore.GREEN + Back.WHITE +"V. VOLVER AL MENÚ ANTERIOR\n")

def construccion():
    print(Fore.GREEN + Back.WHITE +"________________________________________")
    print(Fore.GREEN + Back.WHITE +" Esta funcionalidad está en contrucción ")
    print(Fore.GREEN + Back.WHITE +"________________________________________") 
    limpiar()

def abrir():
    global alOperaciones, alProductos, alRubros, alRubros_x_productos, alSilos, afOperaciones, afProductos, afRubros, afRubros_x_productos, afSilos
    if (os.path.exists(afOperaciones)):
        alOperaciones = open (afOperaciones, "r+b")
    else:
        alOperaciones = open (afOperaciones, "w+b")
    if (os.path.exists(afProductos)):
        alProductos = open (afProductos, "r+b")
    else:
        alProductos = open (afProductos, "w+b")
    if (os.path.exists(afRubros)):
        alRubros = open (afRubros, "r+b")
    else:
        alRubros = open (afRubros, "w+b")
    if (os.path.exists(afRubros_x_productos)):
        alRubros_x_productos = open (afRubros_x_productos, "r+b")
    else:
        alRubros_x_productos = open (afRubros_x_productos, "w+b")
    if (os.path.exists(afSilos)):
        alSilos = open (afSilos, "r+b")
    else:
        alSilos = open (afSilos, "w+b")

def cerrar():
    alOperaciones.close
    alProductos.close
    alRubros.close
    alRubros_x_productos.close
    alSilos.close

def formatearOperaciones(vsOper):
    vsOper.patente = vsOper.patente.ljust(7, ' ') 
    vsOper.cod_prod = str(vsOper.cod_prod)
    vsOper.cod_prod = vsOper.cod_prod.ljust(6, ' ')
    vsOper.fecha_cupo = str(vsOper.fecha_cupo)
    vsOper.fecha_cupo = vsOper.fecha_cupo.ljust(10, ' ')
    vsOper.bruto = str(vsOper.bruto)
    vsOper.bruto = vsOper.bruto.ljust(6, ' ')
    vsOper.tara = str(vsOper.tara)
    vsOper.tara = vsOper.tara.ljust(6, ' ')

def formatearProductos(vsProd):
    vsProd.cod_prod = str(vsProd.cod_prod)
    vsProd.cod_prod = vsProd.cod_prod.ljust(6, ' ')
    vsProd.nombre = vsProd.nombre.ljust(30, ' ')
    vsProd.cami = str(vsProd.cami)
    vsProd.cami = vsProd.cami.ljust(6, ' ')
    vsProd.stock = str(vsProd.stock)
    vsProd.stock = vsProd.stock.ljust(10, ' ')

def formatearRubro(vsRubr):
    vsRubr.cod_rubro = str(vsRubr.cod_rubro)
    vsRubr.cod_rubro = vsRubr.cod_rubro.ljust(6, ' ')
    vsRubr.nombre = vsRubr.nombre.ljust(30, ' ')

def formatearRubro_por_producto(vsRxP):
    vsRxP.cod_rubro = str(vsRxP.cod_rubro)
    vsRxP.cod_rubro = vsRxP.cod_rubro.ljust(6, ' ')
    vsRxP.cod_prod = str(vsRxP.cod_prod)
    vsRxP.cod_prod = vsRxP.cod_prod.ljust(6, ' ')
    vsRxP.min = str(vsRxP.min)
    vsRxP.min = vsRxP.min.ljust(6, ' ')
    vsRxP.max = str(vsRxP.max)
    vsRxP.max = vsRxP.max.ljust(6, ' ')    

def formatearSilo(vsSilo):
    vsSilo.cod_silo = str(vsSilo.cod_silo)
    vsSilo.cod_silo = vsSilo.cod_silo.ljust(6, ' ')
    vsSilo.nombre = vsSilo.nombre.ljust(30, ' ')
    vsSilo.cod_prod = str(vsSilo.cod_prod)
    vsSilo.cod_prod = vsSilo.cod_prod.ljust(6, ' ')
    vsSilo.stock = str(vsSilo.stock)
    vsSilo.stock = vsSilo.stock.ljust(7, ' ')

def cupo():
    global alOperaciones, afOperaciones
    opc1="C"
    while(opc1 != "F"):
        regOpe = Operacion()
        patente = str(input("Ingrese patente [debe tener una longitud entre 6 y 7 caracteres]: "))
        while validarPatente(patente):
            patente = str(input("El formato de la patente ingresada no es valido, debe ser entre 6 y 7 caracteres. Ingrese patente: "))
        fechacupo = validarFechaVto()
        if BuscarPatente(patente, fechacupo) == -1:
            consultaProducto()
            prod = int(input("Ingrese el codigo del productos: "))
            while busquedaSecProd(prod) == -1:
                prod = int(input("Codigo no asignado a un producto. Ingrese el codigo del productos: "))
            regOpe.patente = patente
            regOpe.cod_prod = prod
            regOpe.fecha_cupo = fechacupo
            regOpe.estado = "P"
            formatearOperaciones(regOpe)
            alOperaciones.seek(0,2)
            pickle.dump(regOpe, alOperaciones)
            alOperaciones.flush()
        else:
            if os.path.getsize(afOperaciones) != 0:
                print("Para esta fecha ya tiene cupo esta patente")
        print("------------------------------------------------------------------------------")
        opc1 = input("¿Desea cargar otro camion? - Ingrese 'F' para Finalizar ")
        opc1 = opc1.upper()   
        limpiar()
 
def recepcion():
    global alOperaciones, afOperaciones
    est="C"
    while est!="F":
        regOpe = Operacion()
        patente = str(input("Ingrese patente [debe tener una longitud entre 6 y 7 caracteres]: "))
        while validarPatente(patente):
            patente = str(input("El formato de la patente ingresada no es valido, debe ser entre 6 y 7 caracteres. Ingrese patente: "))
        puntero = BuscarRecep(patente, "P")
        if puntero != -1:
            alOperaciones.seek(puntero, 0)
            regOpe = pickle.load(alOperaciones)
            regOpe.estado = "A"
            print("La patente se recepciono.")
            alOperaciones.seek(puntero, 0)
            pickle.dump(regOpe, alOperaciones)
            alOperaciones.flush()
        else:
            if os.path.getsize(afOperaciones) != 0:
                print("Hoy este camion no tiene fecha asignada")
        print("------------------------------------------------------------------------------")
        est = input("¿Desea cargar otro camion? - Ingrese 'F' para Finalizar ")
        est = est.upper()
        limpiar()

def peso_bruto():
    global alOperaciones, afOperaciones
    est="C"
    while est!="F":
        regOpe = Operacion()
        patente = str(input("Ingrese patente [debe tener una longitud entre 6 y 7 caracteres]: "))
        while validarPatente(patente):
            patente = str(input("El formato de la patente ingresada no es valido, debe ser entre 6 y 7 caracteres. Ingrese patente: "))
        puntero = BuscarRecep(patente, "C")
        if puntero != -1:
            alOperaciones.seek(puntero, 0)
            regOpe = pickle.load(alOperaciones)
            bruto = float(input("Ingrese peso bruto: "))
            while bruto < 0:
                bruto = float(input("El valor de peso bruto no es correcto. Ingrese otro valor: "))
            regOpe.bruto = bruto
            regOpe.estado = "B"
            print("Se registro el peso bruto.")
            formatearOperaciones(regOpe)
            alOperaciones.seek(puntero, 0)
            pickle.dump(regOpe, alOperaciones)
            alOperaciones.flush()
        else:
            if os.path.getsize(afOperaciones) != 0:
                print("La carga no cumple con la calidad requerida")
        print("------------------------------------------------------------------------------")
        est = input("¿Desea cargar otro camion? - Ingrese 'F' para Finalizar ")
        est = est.upper()
        limpiar()

def registrar_tara():
    global alOperaciones, afOperaciones, alSilos, afSilos, alProductos, afProductos
    est="C"
    while est!="F":
        regOpe = Operacion()
        regSilo = Silo()
        regProd = Producto()
        patente = str(input("Ingrese patente [debe tener una longitud entre 6 y 7 caracteres]: "))
        while validarPatente(patente):
            patente = str(input("El formato de la patente ingresada no es valido, debe ser entre 6 y 7 caracteres. Ingrese patente: "))
        puntero = BuscarRecep(patente, "B")
        if puntero != -1:
            alOperaciones.seek(puntero, 0)
            regOpe = pickle.load(alOperaciones)
            bandera = BuscarSilo(regOpe.cod_prod)
            if bandera != -1:
                band = busquedaSecProd(regOpe.cod_prod)
                alProductos.seek(band, 0)
                regProd = pickle.load(alProductos)
                alSilos.seek(bandera, 0)
                regSilo = pickle.load(alSilos)
                tara = float(input("Ingrese tara: "))
                while tara > float(regOpe.bruto):
                    tara = float(input("El valor de tara agregada es mayor que el bruto. Ingrese otro valor de tara: "))
                regOpe.tara = tara
                regOpe.estado = "F"
                regSilo.stock = float(regSilo.stock) + (float(regOpe.bruto) - tara)
                regProd.stock = float(regProd.stock) + (float(regOpe.bruto) - tara)
                regProd.cami = int(regProd.cami) + 1
                print("Se registro la tara. Se actualizo el stock de los Silos")
                formatearOperaciones(regOpe)
                formatearSilo(regSilo)
                formatearProductos(regProd)
                alOperaciones.seek(puntero, 0)
                alSilos.seek(bandera, 0)
                alProductos.seek(band, 0)
                pickle.dump(regProd, alProductos)
                pickle.dump(regOpe, alOperaciones)
                pickle.dump(regSilo, alSilos)
                alSilos.flush()
                alOperaciones.flush()
            else:
                if os.path.getsize(afSilos) != 0:
                    print("El producto no esta registrado")
        else:
            print("Camion no registro el bruto")
        print("------------------------------------------------------------------------------")
        est = input("¿Desea cargar otro camion? - Ingrese 'F' para Finalizar ")
        est = est.upper()
        limpiar()

def ordenarRubro():
    global afRubros, alRubros
    alRubros.seek(0,0)
    aux = pickle.load(alRubros)
    tamReg = alRubros.tell()
    if tamReg != 0:      
        t = os.path.getsize(afRubros)
        cantReg = int(t / tamReg)
        for i in range(0, cantReg-1):
            for j in range(i+1, cantReg):
                alRubros.seek(i*tamReg, 0)
                auxi = pickle.load(alRubros)
                alRubros.seek(j*tamReg, 0)
                auxj = pickle.load(alRubros)
                if (int(auxi.cod_rubro) > int(auxj.cod_rubro)):
                    alRubros.seek(i*tamReg, 0)
                    pickle.dump(auxj, alRubros)
                    alRubros.seek(j*tamReg, 0)
                    pickle.dump(auxi, alRubros)
                    alRubros.flush()

def registrar_calidad():
    global alOperaciones, afOperaciones, alRubros_x_productos, afRubros_x_productos, alRubros, afRubros
    opc1="C"
    while(opc1 != "F"):
        regOpe = Operacion()
        patente = str(input("Ingrese patente [debe tener una longitud entre 6 y 7 caracteres]: "))
        while validarPatente(patente):
            patente = str(input("El formato de la patente ingresada no es valido, debe ser entre 6 y 7 caracteres. Ingrese patente: "))
        indice = BuscarRecep(patente, "A")
        if indice != -1:
            alOperaciones.seek(indice, 0)
            regOpe = pickle.load(alOperaciones)
            print("Producto: ", BuscaProductox(regOpe.cod_prod))
            alRubros_x_productos.seek(0,0)
            regRxP = Rubro_por_producto()
            t = os.path.getsize(afRubros_x_productos)
            bandera = True
            fallo = 0
            while alRubros_x_productos.tell() < t and bandera:
                regRxP = pickle.load(alRubros_x_productos)
                if int(regOpe.cod_prod) == int(regRxP.cod_prod):
                    nombre = BuscaRubro(int(regRxP.cod_rubro))
                    if nombre != "-1":
                        print(nombre)
                        print("Cota inferior ",regRxP.min, " y la Cota superior ", regRxP.max)
                        prueba = float(input("Ingrese el valor del rubro: "))
                        if prueba < float(regRxP.min) or prueba > float(regRxP.max):
                            fallo = fallo + 1
                        if fallo > 2:
                            bandera = False
            if os.path.getsize(afRubros_x_productos) != 0:
                if fallo > 2:
                    estado = "R"
                    print("Descarga Rechazada por no cumplis el standard de calidad")
                else:
                    estado = "C"
                    print("La carga paso el standard de calidad")
                regOpe.estado = estado
                alOperaciones.seek(indice, 0)
                pickle.dump(regOpe, alOperaciones)
                alOperaciones.flush()
            else:
                print("El archivo Rubros x Producto esta vacio!")
        else:
            if os.path.getsize(afOperaciones) != 0:
                print("Camion no Arribado")
        opc1 = input("¿Desea carga los datos de otro camion? - Ingrese 'F' para Finalizar ")
        opc1 = opc1.upper()  
        limpiar()

def BuscaProductox(cod):
    global alProductos, afProductos
    t = os.path.getsize(afProductos)
    alProductos.seek(0, 0) 
    regProd = Silo()
    if t>0:
        regProd = pickle.load(alProductos)
        while ((alProductos.tell()<t) and (int(cod) != int(regProd.cod_prod))):
            regProd = pickle.load(alProductos)
        if int(cod) == int(regProd.cod_prod):        
            return regProd.nombre
        else:
            return -1
    else:
        print("\n")
        print("el archivo Producto esta vacio")
        print("\n")
        return -1

def BuscaRubro (Cod):
	global afRubros, alRubros
	regRubros = Rubro()
	t = os.path.getsize(afRubros)
	if t>0:
		alRubros.seek (0,0)
		regRubros = pickle.load(alRubros)
		tamReg = alRubros.tell()
		cantReg = int(os.path.getsize(afRubros) / tamReg)
		inferior = 0
		superior = cantReg-1
		medio = inferior + superior // 2
		alRubros.seek(medio*tamReg, 0)
		regRubros= pickle.load(alRubros)
		while int(regRubros.cod_rubro)!= int(Cod) and (inferior < superior):
			if int(Cod) < int(regRubros.cod_rubro):
				superior = medio - 1
			else:
				inferior = medio + 1
			medio = (inferior + superior) //2
			alRubros.seek(medio*tamReg, 0)
			regRubros= pickle.load(alRubros)
		if int(regRubros.cod_rubro) == int(Cod):
			return regRubros.nombre
		else:
			return "-1"
	else:
            print("\n")
            print("el archivo Rubros esta vacio")
            print("\n")
            return "-1" 

def BuscarSilo(cod):
    global alSilos, afSilos
    t = os.path.getsize(afSilos)
    regSilo = Silo()
    pos = 0 
    alSilos.seek(0, 0)
    if t>0:
        regSilo = pickle.load(alSilos)
        while ((alSilos.tell()<t) and (int(cod) != int(regSilo.cod_prod))):
            pos = alSilos.tell()
            regSilo = pickle.load(alSilos)
        if int(cod) == int(regSilo.cod_prod):        
            return pos
        else:
            return -1
    else:
        print("\n")
        print("el archivo Silos esta vacio")
        print("\n")
        return -1

def BuscarRecep(pat, estado):
    global alOperaciones, afOperaciones
    fecha = datetime.datetime.now().strftime('%d/%m/%Y')
    t = os.path.getsize(afOperaciones)
    pos = 0
    alOperaciones.seek(0, 0) 
    regOpe = Operacion()
    pat = pat.ljust(7, ' ') 
    if t>0:
        regOpe = pickle.load(alOperaciones)
        while (alOperaciones.tell()<t) and ((pat != regOpe.patente) or (fecha != regOpe.fecha_cupo) or (estado != regOpe.estado)):
            pos = alOperaciones.tell()
            regOpe = pickle.load(alOperaciones)
        if ((pat == regOpe.patente) and (fecha == regOpe.fecha_cupo) and (estado == regOpe.estado)):        
            return pos
        else:
            return -1
    else:
        print("\n")
        print("el archivo Operaciones esta vacio")
        print("\n")
        return -1

def BuscarPatente(pat, fecha):
    global alOperaciones, afOperaciones
    t = os.path.getsize(afOperaciones)
    alOperaciones.seek(0, 0) 
    regOpe = Operacion()
    pos = 0
    pat = pat.ljust(7, ' ')
    if t>0:
        regOpe = pickle.load(alOperaciones)
        while ((alOperaciones.tell()<t) and ((pat != regOpe.patente) or (fecha != regOpe.fecha_cupo))):
            pos = alOperaciones.tell()
            regOpe = pickle.load(alOperaciones)
        if (pat == regOpe.patente) and (fecha == regOpe.fecha_cupo):        
            return pos
        else:
            return -1
    else:
        return -1

def validarPatente(nro):
    try:              
        nro = len(nro)      
        if nro >= 6 and nro <= 7:
            return False 
        else:
            return True  
    except:
        return True  

def validarFechaVto():
    flag = True
    while flag:
        try:
            fecha = input("Ingresa una fecha en el formato DD/MM/AAAA: ")
            datetime.datetime.strptime(fecha, '%d/%m/%Y')
            flag = False
        except ValueError:
            print("Fecha inválida")
    return fecha

def buscaRecibidos():
    global afOperaciones, alOperaciones
    regOpe = Operacion()
    t = os.path.getsize(afOperaciones)
    alOperaciones.seek(0,0)
    cont = 0
    while alOperaciones.tell() < t:
        regOpe = pickle.load(alOperaciones)
        if regOpe.estado != "P":
            cont = cont + 1
    return cont

def camxprod():
    global afProductos, alProductos
    regProd = Producto()
    alProductos.seek(0,0)
    t = os.path.getsize(afProductos)
    if noHayProductos():
        print('--- No hay productos disponibles ---\n')
    else:
        alProductos.seek(0,0)
        print("Cantidad total de camiones por producto: ")
        print('  -- Cantidad -- Nombre --')
        while alProductos.tell() < t:
            regProd = pickle.load(alProductos)
            if regProd.alta == False:
                print('    ', regProd.cami, '  ', regProd.nombre)

def netoprod():
    global afProductos, alProductos
    regProd = Producto()
    alProductos.seek(0,0)
    t = os.path.getsize(afProductos)
    if noHayProductos():
        print('--- No hay productos disponibles ---\n')
    else:
        alProductos.seek(0,0)
        print("Peso neto total de cada producto: ")
        print('  -- Cantidad -- Nombre --')
        while alProductos.tell() < t:
            regProd = pickle.load(alProductos)
            if regProd.alta == False:
                print('    ', regProd.stock, '  ', regProd.nombre)

def promprod():
    global afProductos, alProductos
    regProd = Producto()
    alProductos.seek(0,0)
    t = os.path.getsize(afProductos)
    if noHayProductos():
        print('--- No hay productos disponibles ---\n')
    else:
        alProductos.seek(0,0)
        print("Promedio del peso neto de producto por camión de ese producto: ")
        print('  -- Promedio -- Nombre --')
        while alProductos.tell() < t:
            regProd = pickle.load(alProductos)
            if regProd.alta == False:
                if(float(regProd.cami) != 0):
                    prome = float(regProd.stock) / float(regProd.cami)
                    prome2 = round(prome, 2)
                    prome2 = str(prome2)
                    prome2 = prome2.ljust(8, ' ')
                    print('    ',prome2, '  ', regProd.nombre)

def menor():
    global alOperaciones, afOperaciones, alProductos, afProductos
    t1 = os.path.getsize(afOperaciones)
    t2 = os.path.getsize(afProductos)
    regOpe= Operacion()
    regProd = Producto()
    alOperaciones.seek(0,0)
    alProductos.seek(0,0)
    while alProductos.tell() < t2:
        regProd = pickle.load(alProductos)
        menor = 9999999999999999999999999999999999999999999999999
        cont = 0
        while alOperaciones.tell() < t1:
            regOpe = pickle.load(alOperaciones)
            if float(regOpe.bruto)-float(regOpe.tara) < menor and int(regProd.cod_prod) == int(regOpe.cod_prod):
                menor = float(regOpe.bruto)-float(regOpe.tara)
                pat = regOpe.patente
                cont = cont + 1
        if cont != 0:        
            print("       ", pat, "      ", regProd.nombre )

def reporte(): 
    global alOperaciones, afOperaciones
    alOperaciones.seek(0, 0)
    regOpe = pickle.load(alOperaciones)
    t = os.path.getsize(afOperaciones)
    if  t > 0 :
        cant_cupo = t / alOperaciones.tell()
        print("Cantidad de cupos otorgados: ", int(cant_cupo))
        print("**************************************************************")
        print("Cantidad total de camiones recibidos: ", buscaRecibidos())
        print("**************************************************************")
        camxprod()
        print("**************************************************************")
        netoprod()
        print("**************************************************************")
        promprod()
        print("**************************************************************")
        print("Patente del camión de cada producto que menor cantidad de dicho producto descargó: ")
        print(" ------ Patente ------ Producto ------")
        menor()
        input()
    else:
        print("No se ingresaron camiones todavia.")
    input()

def menusilo():
    print(Fore.WHITE + Back.YELLOW +"A. SILO CON MAYOR STOCK                                  ")
    print(Fore.WHITE + Back.YELLOW +"B. LISTA DE PATENTES DE LOS CAMIONES RECHAZADOS POR FECHA")
    print(Fore.WHITE + Back.YELLOW +"V. VOLVER AL MENU ANTERIOR                               ")

def silosyrechazados():
    menusilo()
    option = input().upper()
    while option != 'V' and option != 'B'and option != 'A':
        print("Opcion invalida. Ingrese otra opcion!")
        limpiar()
        menusilo()
        option = input('Ingrese una opcion: ').upper()
    while option != "V":
        while option != 'V' and option != 'B'and option != 'A':
            print("Opcion invalida. Ingrese otra opcion!")
            limpiar()
            menusilo()
            option = input('Ingrese una opcion: ').upper()
        if option == 'A':
            silomaystock()
            limpiarConsola()
            menusilo()
            option = input('Ingrese una opcion: ').upper()
        if option == 'B':
            fechabuscar = validarFechaVto()
            listarrechazo(fechabuscar)
            limpiarConsola()
            menusilo()
            option = input('Ingrese una opcion: ').upper()

def silomaystock():
    limpiarConsola()
    global afSilos, alSilos
    regSilo = Silo()
    alSilos.seek(0,0)
    t = os.path.getsize(afSilos)
    if t >0:
        mayor = 0
        alSilos.seek(0,0)
        while alSilos.tell() < t:
            regSilo = pickle.load(alSilos)
            if float(regSilo.stock) > mayor:
                codi = regSilo.cod_silo
                nombre = regSilo. nombre
                mayor = float(regSilo.stock)
                codigo_prod = regSilo.cod_prod       
        print(Fore.WHITE + Back.YELLOW +"             --- Silo con mayor stock ---                               ")
        print(Fore.WHITE + Back.YELLOW +" Codigo Silo -- Codigo Producto -- Nombre Silo --                 Stock ")
        print("   ", codi, "      ", codigo_prod, "         ", nombre, "", mayor)
    else:
        print("No hay silos cargados.")
    input()

def listarrechazo(fecha):
    global afOperaciones, alOperaciones
    regOpe = Operacion()
    alOperaciones.seek(0,0)
    t = os.path.getsize(afOperaciones)
    cont = 0
    if t >0:
        alOperaciones.seek(0,0)
        while alOperaciones.tell() < t:
            regOpe = pickle.load(alOperaciones)
            if regOpe.estado == "R" and regOpe.fecha_cupo == fecha:
                cont = cont + 1
        if cont != 0:
            alOperaciones.seek(0,0)
            print('--- Camiones Rechazados ---')
            while alOperaciones.tell() < t:
                regOpe = pickle.load(alOperaciones)
                if regOpe.estado == "R" and regOpe.fecha_cupo == fecha:
                    print(regOpe.patente)
        else:
            print("Para la fecha ", fecha, " no tiene camiones rechazados.")
    else:
        print("No hay camiones cargados.")
    input()
    
def administraciones():
    menu2()
    option = input().upper()
    while option != 'V':
        if (option == 'A' or option == 'F' or option == 'G'):
            limpiarConsola()
            construccion()
            menu2()
            option = input('Ingrese una opcion: ').upper()
        if option == 'B':
            productos()
            limpiarConsola()
            menu2()
            option = input('Ingrese una opcion: ').upper()
        if option == 'C':
            altaRubro()
            limpiarConsola()
            menu2()
            option = input('Ingrese una opcion: ').upper()
        if option == 'D':
            altaRubroXProducto()
            limpiarConsola()
            menu2()
            option = input('Ingrese una opcion: ').upper()
        if option == 'E':
            altaSilos()
            limpiarConsola()
            menu2()
            option = input('Ingrese una opcion: ').upper()
      
def productos():
    limpiarConsola()
    menu3()
    option = input().upper()
    while option != 'V':
        if option == 'A':
            altaProducto()
            limpiarConsola()
            menu3()
            option = input('Ingrese una opcion: ').upper()
        if option == 'B':
            bajaProducto()
            limpiarConsola()
            menu3()
            option = input('Ingrese una opcion: ').upper()
        if option == 'C':
            consultaProducto()
            menu3()
            option = input('Ingrese una opcion: ').upper()
        if option == 'M':
            modificacionProducto()
            limpiarConsola()
            menu3()
            option = input('Ingrese una opcion: ').upper()

def busquedaSecProd(cod):
    global afProductos, alProductos
    t = os.path.getsize(afProductos)
    pos = 0
    alProductos.seek(0,0)
    vrProd = Producto()

    if t>0:
        vrProd = pickle.load(alProductos)
        while (alProductos.tell() < t) and ((int(cod) != int(vrProd.cod_prod)) or (vrProd.alta != False)):
            pos = alProductos.tell()
            vrProd = pickle.load(alProductos)
        if int(vrProd.cod_prod) == int(cod) and (vrProd.alta == False):
            return pos
        else: 
            return -1
    else:
        return -1

def noHayProductos(): 
    global afProductos, alProductos
    t = os.path.getsize(afProductos)
    alProductos.seek(0,0)
    prod = Producto()
    if t > 0:
        prod = pickle.load(alProductos)
        while (alProductos.tell() < t) and prod.alta == True:
            prod = pickle.load(alProductos)
        return prod.alta == True
    else:
        return True

def hayRubros(): 
    global afRubros
    t = os.path.getsize(afRubros)
    return t > 0

def busquedaSecRubro(cod):
    global afRubros, alRubros
    t = os.path.getsize(afRubros)
    pos = 0
    alRubros.seek(0,0)
    vrRubro = Rubro()

    if t>0:
        vrRubro = pickle.load(alRubros)
        while (alRubros.tell() < t ) and (int(cod) != int(vrRubro.cod_rubro)):
            pos = alRubros.tell()
            vrRubro = pickle.load(alRubros)
        if int(vrRubro.cod_rubro) == int(cod):
            return pos
        else: 
            return -1
    else:
        return -1
    
def ingresaProducto(cod, vrProd):
    vrProd.cod_prod = int(cod)
    vrProd.nombre = input('Ingrese el nombre del producto, hasta 20 caracteres\n')
    while len(vrProd.nombre) < 1 or len(vrProd.nombre) > 20:
        vrProd.nombre = input('Incorrecto - Nombre hasta 20 caracteres\n')
    vrProd.alta = False

def ingresaRubro(cod, vrRubro):
    vrRubro.cod_rubro = int(cod)
    vrRubro.nombre = input('Ingresa el nombre del rubro, hasta 20 caracteres\n')
    while len(vrRubro.nombre) < 1 or len(vrRubro.nombre) > 20:
        vrRubro.nombre = input('Incorrecto - Nombre hasta 20 caracteres\n')

def ingresaRubroXProducto(cod_prod, cod_rubro, vrRubroxProd):
    limpiarConsola()
    vrRubroxProd.cod_prod = cod_prod
    vrRubroxProd.cod_rubro = cod_rubro
    vrRubroxProd.min = float(input('Ingresa el valor minimo admitido\n'))
    while vrRubroxProd.min < 0:
        vrRubroxProd.min = float(input('El valor minimo no puede ser menor a 0. Ingresa nuevamente\n'))
    vrRubroxProd.max = float(input('Ingresa el valor maximo admitido\n'))
    while vrRubroxProd.max > 100:
        vrRubroxProd.max = float(input('El valor maximo admitido no puede ser mayor a 100. Ingresa nuevamente\n'))
    while vrRubroxProd.min > vrRubroxProd.max:
        vrRubroxProd.min = float(input('El valor minimo no puede superar al maximo. Ingrese el minimo nuevamente: '))

def ingresaSilo(cod, cod_prod, silo):
    limpiarConsola()
    silo.cod_silo = cod
    silo.cod_prod = cod_prod
    silo.nombre = input('Ingresa el nombre del silo, hasta 20 caracteres\n')
    while len(silo.nombre) < 1 or len(silo.nombre) > 20:
        silo.nombre = input('Incorrecto - Nombre hasta 20 caracteres\n')
    silo.stock = int(input('Ingresa el stock del silo\n'))
    while silo.stock < 0:
        silo.stock = int(input('El stock debe ser mayor a cero. Ingrese nuevamente\n'))

def altaRubro():
    global afRubros, alRubros
    limpiarConsola()
    cod = input('Ingrese el codigo del rubro o 0 para volver al menu anterior\n')
    while int(cod) != 0:
        regRubro = Rubro()
        if busquedaSecRubro(int(cod)) == -1:
            ingresaRubro(cod, regRubro)
            formatearRubro(regRubro)
            alRubros.seek(0,2)
            pickle.dump(regRubro, alRubros)
            print('--- Alta de rubro exitosa ---')
            alRubros.flush()
            ordenarRubro()
            alRubros.seek(0,0)
            regRubro = Rubro()
            t = os.path.getsize(afRubros)
            while alRubros.tell() < t:
                regRubro = pickle.load(alRubros)
                print(regRubro.cod_rubro, ' ', regRubro.nombre)
        else:
            print('Ya existe un rubro registrado con ese codigo')
        cod = input('Ingrese el codigo del rubro o 0 para volver al menu anterior\n')

def altaProducto(): 
    global afProductos, alProductos
    limpiarConsola()
    cod = input('Ingrese el codigo del producto o 0 para volver al menu anterior\n')
    while not cod.isnumeric():
        cod = input('El codigo debe ser un valor numerico. Ingrese nuevamente o presione 0 para volver al menu interior\n')
    while int(cod) != 0:
        if busquedaSecProd(int(cod)) == -1:
            regProd = Producto()
            ingresaProducto(cod, regProd)
            formatearProductos(regProd)
            alProductos.seek(0,2)
            pickle.dump(regProd, alProductos)
            print('--- Alta de producto exitosa ---')
            alProductos.flush() ##graba en el archivo.
            alProductos.seek(0,0)
            regProd = Producto()
            consultaProducto()
        else:
            limpiarConsola()
            print('Ya existe un producto registrado con ese codigo')
        cod = int(input('Ingrese el codigo del producto o 0 para volver al menu anterior\n'))
        limpiarConsola()

def altaRubroXProducto():
    limpiarConsola()
    global afRubros_x_productos, alRubros_x_productos
    if not noHayProductos() and hayRubros():
        regRubroxProd = Rubro_por_producto()
        consultaProducto()
        cod_prod = input('Ingrese el codigo del producto que desea registrar o 0 para volver al menu anterior\n')
        while not cod_prod.isnumeric():
            cod_prod = input('El codigo debe ser un valor numerico. Ingrese nuevamente o presione 0 para volver al menu interior\n')
        while int(cod_prod) != 0:
            while busquedaSecProd(cod_prod) == -1:
                limpiarConsola()
                consultaProducto()
                cod_prod = int(input('No se ha registrado ningun producto con dicho codigo. Ingrese nuevamente\n'))
            limpiarConsola()
            consultaRubro()
            cod_rubro = int(input('Ingrese el codigo del rubro que desea registrar\n'))

            while busquedaSecRubro(cod_rubro) == -1:
                limpiarConsola()
                consultaRubro()
                cod_rubro = int(input('No se ha registrado ningun rubro con dicho codigo. Ingrese nuevamente\n'))

            while validarRubroxProducto(cod_rubro, cod_prod):
                limpiarConsola()
                consultaRubro()
                cod_rubro = int(input('Ya se registro un producto con ese codigo de rubro. Ingrese un rubro distinto: '))
                while busquedaSecRubro(cod_rubro) == -1:
                    limpiarConsola()
                    consultaRubro()
                    cod_rubro = int(input('No se ha registrado ningun rubro con dicho codigo. Ingrese nuevamente\n'))

            limpiarConsola()
            ingresaRubroXProducto(cod_prod, cod_rubro, regRubroxProd)
            formatearRubro_por_producto(regRubroxProd)
            alRubros_x_productos.seek(0,2)
            pickle.dump(regRubroxProd, alRubros_x_productos)
            print('--- Alta de rubro x producto exitosa ---\n')
            alRubros_x_productos.flush()
            alRubros_x_productos.seek(0,0)
            regRubroxProd = Rubro_por_producto()
            consultaRubroXProducto()
            limpiar()
            print('\n \n')
            consultaProducto()
            cod_prod = int(input('Ingrese el codigo del producto o 0 para volver al menu anterior\n'))
    else:
        limpiarConsola()
        print('Debe haber rubros y productos registrados para poder registrar un Rubro x Producto\n')

def validarRubroxProducto(cod_rubro, cod_prod):
    global afRubros_x_productos, alRubros_x_productos
    t = os.path.getsize(afRubros_x_productos)
    alRubros_x_productos.seek(0,0)
    vrRubroProd = Rubro_por_producto()
    if t>0:
        vrRubroProd = pickle.load(alRubros_x_productos)
        while (alRubros_x_productos.tell() < t) and not(vrRubroProd.cod_rubro == int(cod_rubro) and vrRubroProd.cod_prod == int(cod_prod)):
            vrRubroProd = pickle.load(alRubros_x_productos)
    return int(vrRubroProd.cod_rubro) == cod_rubro and int(vrRubroProd.cod_prod) == cod_prod

def bajaProducto():
    global alProductos
    consultaProducto()
    cod = input('Ingrese el codigo del producto que desea dar de baja o 0 para volver al menu anterior ')
    while not cod.isnumeric():
        cod = input('El codigo debe ser un valor numerico. Ingrese nuevamente o presione 0 para volver al menu interior\n')
    while int(cod) != 0:
        while busquedaSecProd(cod) == -1: 
            cod = input('No se ha registrado ningun producto con dicho codigo. ')
        if cod != 0:
            pos = busquedaSecProd(cod)
            alProductos.seek(pos, 0)
            rProducto = pickle.load(alProductos)
            rProducto.alta = True
            alProductos.seek(pos, 0)
            pickle.dump(rProducto, alProductos)
            print('--- Baja de producto exitosa ---')
            alProductos.flush()
        cod = int(input('Ingrese el codigo del producto que desea dar de baja o 0 para volver al menu anterior '))

def consultaProducto():
    limpiarConsola()
    global afProductos, alProductos
    regProd = Producto()
    alProductos.seek(0,0)
    t = os.path.getsize(afProductos)
    if noHayProductos():
        print(Fore.WHITE + Back.YELLOW + '--- No hay productos disponibles ---\n')
    else:
        alProductos.seek(0,0)
        print(Fore.WHITE + Back.YELLOW + '\n--- Productos disponibles ---                  ')
        print(Fore.WHITE + Back.YELLOW + '    -- Codigo -- Nombre --                     \n')
        while alProductos.tell() < t:
            regProd = pickle.load(alProductos)
            if regProd.alta == False:
                print(Fore.GREEN + Back.WHITE + '        ' + Fore.GREEN + Back.WHITE + regProd.cod_prod + '   ' + Fore.GREEN + Back.WHITE + regProd.nombre)
    print('\n')

def consultaRubroXProducto():
    global afRubros_x_productos, alRubros_x_productos
    t = os.path.getsize(afRubros_x_productos)
    if t == 0:
        print(Fore.WHITE + Back.YELLOW + '--- No hay Rubros x Producto registrados ---')
    else:
        regRubroxProd = Rubro_por_producto()
        alRubros_x_productos.seek(0,0)
        print(Fore.WHITE + Back.YELLOW + ' --- Rubros x Producto ---                         ')
        print(Fore.WHITE + Back.YELLOW + 'Codigo producto  Codigo rubro   Minimo    Maximo   ')
        while alRubros_x_productos.tell() < t:
                regRubroxProd = pickle.load(alRubros_x_productos)
                print(Fore.GREEN + Back.WHITE + regRubroxProd.cod_prod + '           ' + regRubroxProd.cod_rubro + '         ' + regRubroxProd.min, '   ', regRubroxProd.max)

def consultaRubro():
    global afRubros, alRubros
    regRubro = Rubro()
    alRubros.seek(0,0)
    t = os.path.getsize(afRubros)
    if t == 0:
        print(Fore.WHITE + Back.YELLOW + '--- No hay rubros disponibles ---\n')
    else:
        alRubros.seek(0,0)
        print(Fore.WHITE + Back.YELLOW + '\n--- Rubros disponibles ---               ')
        print(Fore.WHITE + Back.YELLOW + '   - Codigo --- Nombre -                 \n')
        while alRubros.tell() < t:
            regRubro = pickle.load(alRubros)
            print(Fore.GREEN + Back.WHITE + '  ' + Fore.GREEN + Back.WHITE + regRubro.cod_rubro + '   ' + Fore.GREEN + Back.WHITE + regRubro.nombre)
    print('\n')

def modificacionProducto():
    global afProductos, alProductos
    limpiarConsola()
    consultaProducto()
    cod = input('Ingrese el codigo del producto que desea modificar o 0 para volver al menu anterior ')
    while not cod.isnumeric():
        cod = input('El codigo debe ser un valor numerico. Ingrese nuevamente o presione 0 para volver al menu interior\n')
    if int(cod) != 0:
        pos = busquedaSecProd(int(cod))
        if pos == -1:
            print('No se encontro ningun producto registrado con ese codigo')
        else:
            alProductos.seek(pos, 0)
            prod = pickle.load(alProductos)
            prod.nombre = input('Ingrese el nuevo nombre del producto ')
            prod.nombre = prod.nombre.ljust(30, ' ')
            alProductos.seek(pos, 0)
            pickle.dump(prod, alProductos)
            print(prod.nombre, ' ', prod.cod_prod)
            print('--- Modificacion exitosa ---')
            alProductos.flush()
        limpiar()

def altaSilos():
    global afSilos, alSilos
    limpiarConsola()
    if not noHayProductos():
        cod = input('Ingrese el codigo del silo o 0 para volver al menu anterior\n')
        while not cod.isnumeric():
            cod = input('El codigo debe ser un valor numerico. Ingrese nuevamente o presione 0 para volver al menu interior\n')
        while int(cod) != 0:
            silo = Silo()
            consultaProducto()
            cod_prod = int(input('Ingresa el codigo del producto que desea registrar\n'))
            while busquedaSecProd(cod_prod) == -1:
                limpiarConsola()
                consultaProducto()
                cod_prod = int(input('No se ha registrado ningun producto con dicho codigo. Ingrese nuevamente\n'))
            ingresaSilo(cod, cod_prod, silo)
            formatearSilo(silo)
            alSilos.seek(0,2)
            pickle.dump(silo, alSilos)
            print('--- Alta de silo exitosa ---')
            alSilos.flush()
            cod = int(input('Ingrese el codigo del silo o 0 para volver al menu anterior\n'))
            limpiar()
    else:
        print('Para registrar un silo primero debe registrar un producto\n')



#                     PROGRAMA PRINCIPAL
init(autoreset=True)
afOperaciones = "operaciones.dat" 
afProductos = "productos.dat" 
afRubros = "rubros.dat" 
afRubros_x_productos = "rubros_x_productos.dat" 
afSilos = "silos.dat" 
abrir()
opcion = "1"
while opcion != "0":
    menu()
    opcion = str(input("Elige una opción: "))
    limpiarConsola()
    while (opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6" and opcion != "7" and opcion != "8" and opcion != "0" and opcion !="9"): 
        menu()
        opcion = str(input("Opcion incorrecta. Ingrese otro valor: "))
        limpiarConsola()
    if opcion == "1":
        administraciones()
        limpiarConsola()
    elif opcion == "2":
        cupo()
        limpiarConsola()
    elif opcion == "3":
        recepcion()
        limpiarConsola()
    elif opcion == "4":
        registrar_calidad()
        limpiarConsola()
    elif opcion == "5":
        peso_bruto()
        limpiarConsola()
    elif opcion == "6":
        construccion()
    elif opcion == "7":
        registrar_tara()
        limpiarConsola()
    elif opcion == "8":
        reporte()
        limpiarConsola()
    elif opcion == "9":
        silosyrechazados()
        limpiarConsola()
cerrar()