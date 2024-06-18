import os
from datetime import datetime
rut=[]
fecha=[]
hora=[]
monto=[]
reclamo=[]
def validar_formato_rut(rut):
    if not rut or not isinstance(rut, str):
        return False
    parts = rut.split('-')
    if len(parts) != 2:
        return False
    num, dv = parts
    if not num.isdigit() or not dv.isalnum():
        return False
    return True

def guardar_datos(rut, fecha, hora, monto,reclamo):
    archivo_nombre = "diego.csv"
    with open(archivo_nombre, 'w') as csvfile:
        for i in range(len(rut)):
            csvfile.write(f"{rut[i]}; {fecha[i]}; {hora[i]}; {monto[i]}; {reclamo[i]}\n")
    print("Archivo creado correctamente")

while True:
    op=int(input("1. registrar reclamo\n2. Listar reclamo\n3. Respaldar Reclamos\n4. Salir del programa\n"))
    if op==1:
        while True:
            rut_=input("Ingrese RUT: ")
            if validar_formato_rut(rut_):
                print("rut valido")
                rut.append(rut_)
                break
            else:
                print("rut no valido")

            
        while True:
            fecha_ = input("Ingrese la fecha y hora en formato dd/mm/yyyy:\n ")
            try:
                fecha_1 = datetime.strptime(fecha_, '%d/%m/%Y')
                fecha.append(fecha_)
                break
            except ValueError:
                print("Formato incorrecto. Por favor, ingrese la fecha y hora en el formato especificado.")
        
        while True:
            hora_=input("Ingrese Hora en formato HH:MM:SS\n")
            try:
                hora_1= datetime.strptime(hora_, '%H:%M:%S')
                hora.append(hora_)
                break
            except ValueError:
                print("Ingrese una hora valida")

        while True:
            try:
                monto_=int(input("Ingrese Monto: "))
                monto_=monto_/1000
                abs(monto_)
                monto.append(monto_)
                break
            except ValueError:
                print("ingrese Monto Valido: ")
        while True:
            entrada = input("Ingrese un texto de máximo 20 caracteres: ")
            if len(entrada) <= 20:
                reclamo.append(entrada)
                print("reclamo enviado exitosamente")
                break
            else:
                print("El texto ingresado tiene más de 20 caracteres. Inténtelo nuevamente.")

    elif op==2:
        print("\nListado de Trabajadores:")
        for i in range(len(rut)):
            print({fecha[i]}, {hora[i]}, {reclamo[i]}, {monto[i]})

    elif op==3:
        guardar_datos(rut, fecha, hora, monto, reclamo)

    elif op==4:
        break
    else:
        print("ingrese opcion valida")
    
