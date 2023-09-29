nota=float(input("Introduce tu nota del examen"))
asistencia=float(input("Ahora introduce tu porcentaje de asistencia"))

if nota>100 and asistencia>100:
    print("Aqui algo anda mal, prueba a ponerlo sobre 100")

elif nota>=70 and asistencia>=80:
    print("Estas aprobado, puedes descansar tranquilo")

else: 
    print("Vete estudiando para junio maquina")
