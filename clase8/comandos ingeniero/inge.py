# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 23:18:14 2022

@author: ACER
"""

Interfaz de clase :
    def  __init__ ( self , ventana ):
        #Inicializar la ventana con un titulo
        uno mismo ventana = ventana
        uno mismo ventana . title ( "Calculadora" )

        #Agregar una caja de texto para que sea la pantalla de la calculadora
        uno mismo pantalla = Texto ( ventana , estado = "deshabilitado" , ancho = 40 , alto = 3 , fondo = "orquídea" , primer plano = "blanco" , fuente = ( "Helvetica" , 15 ))

        #Ubicar la pantalla en la ventana
        uno mismo pantalla . cuadrícula ( fila = 0 , columna = 0 , columna = 4 , padx = 5 , pady = 5 )

        #Inicializar la operación mostrada en pantalla como string vacío
        uno mismo operación = ""

        #Crear los botones de la calculadora
        boton1 = yo . crear boton ( 7 )
        botón2 = uno mismo . crear boton ( 8 )
        boton3 = yo . crear boton ( 9 )
        boton4 = yo . crearBoton ( u" \u232B " , escribir = False )
        boton5 = yo . crear boton ( 4 )
        boton6 = yo . crear boton ( 5 )
        boton7 = yo . crear boton ( 6 )
        boton8 = yo . crear boton ( u" \u00F7 " )
        boton9 = yo . crear boton ( 1 )
        boton10 = yo . crear boton ( 2 )
        boton11 = yo . crear boton ( 3 )
        boton12 = yo . crear boton ( "*" )
        boton13 = yo . crear boton ( "." )
        boton14 = yo . crear boton ( 0 )
        boton15 = yo . crear boton ( "+" )
        boton16 = yo . crear boton ( "-" )
        boton17 = yo . crearBoton ( "=" , escribir = Falso , ancho = 20 , alto = 2 )

        #Ubicar los botones con el gestor grid
        botones = [ boton1 , boton2 , boton3 , boton4 , boton5 , boton6 , boton7 , boton8 , boton9 , boton10 , boton11 , boton12 , boton13 , boton14 , boton15 , boton16 , boton17 ]
        contador = 0
        para  fila  en el  rango ( 1 , 5 ):
            para  columna  en  rango ( 4 ):
                botones [ contador ]. grilla ( fila = fila , columna = columna )
                contador += 1
        #Ubicar el último botón al final
        botones [ 16 ]. cuadrícula ( fila = 5 , columna = 0 , columna = 4 )

        regreso


    #Crea un botón mostrando el valor pasado por parámetro
    def  crearBotón ( self , valor , escribir = True , ancho = 9 , alto = 1 ):
         botón de retorno ( self . ventana , text = valor , width = ancho , height = alto , font = ( "Helvetica" , 15 ), command = lambda : self . click ( valor , escribir ))


    #Controla el evento disparado al hacer clic en un botón
    def  click ( self , texto , escribir ):
        #Si el parámetro 'escribir' es True, entonces el parámetro texto debe mostrarse en pantalla. Si es Falso, no.
        si  no  escribo :
            #Sólo calcula si hay una operación a ser evaluada y si el usuario presionó '='
            si  texto == "="  y  uno mismo . operación != "" :
                #Reemplazar el valor unicode de la división por el operador división de Python '/'
                uno mismo operación = re . sub ( u" \u00F7 " , "/" , auto . operación )
                resultado = str ( eval ( auto.operacion ) ) _
                uno mismo operación = ""
                uno mismo limpiarPantalla ()
                uno mismo mostrarEnPantalla ( resultado )
            #Si se presionó el botón de borrado, limpiar la pantalla
            elif  texto == u" \u232B " :
                uno mismo operación = ""
                uno mismo limpiarPantalla ()
        #Mostrar texto
        más :
            uno mismo operación += str ( texto )
            uno mismo mostrarEnPantalla ( texto )
        regreso


    #Borra el contenido de la pantalla de la calculadora
    def  limpiarPantalla ( self ):
        uno mismo pantalla . configurar ( estado = "normal" )
        uno mismo pantalla . borrar ( "1.0" , FIN )
        uno mismo pantalla . configurar ( estado = "deshabilitado" )
        regreso


    #Muestra en la pantalla de la calculadora el contenido de las operaciones y los resultados
    def  mostrarEnPantalla ( self , valor ):
        uno mismo pantalla . configurar ( estado = "normal" )
        uno mismo pantalla . insertar ( FIN , valor )
        uno mismo pantalla . configurar ( estado = "deshabilitado" )
        regreso


ventana_principal = Tk ()
calculadora = Interfaz ( ventana_principal )
ventana_principal . bucle principal ()