# 1. Entrada
# Proyecto
# Agenda Médica Institucional
# Reservas. Historial. Control de citas.


#Por definir historiales/ pacientes/ reportes

#DATOS PARA RESERVA

"tipo                  Variables                     Validación
str                     Nombre_del_paciente             (No dejar vacío)
int                     Cédula                          (10 digitos random)
int                     Edad                            (random de 1-100)
str                     Especialidad                    (Opcional)
int                     Fecha_de_cita                   (Variable/random/formato: DD/MM/AAAA))
float                   Hora_de_cita                    (Variable/random de 8 am- 15 pm)
str                     Motivo                          (No menos de letras 5 letras)
int                     Codigo_de_cita                  (random)
int                     Turno                           (random)

#DATOS PARA CITA

"tipo"                  "Variables"                     "Validación"
str                     Cédula_del_paciente             (10 digitos/random)
int                     Fecha_de_atencion               (Variable/random/formato: DD/MM/AAAA)
str                     Especialidad                    (Opción, no se puede quedar vacío)
str                     Diagnostico                     (No dejar vacío)
str                     Tratamiento                     (No dejar vacío)

#DATOS PARA EL CONTROL DE CITAS

"tipo"                  "Variables"                     "Validación"
str                     Código_de_cita                  (random)
str                     Estado                          (opción)
str                     Observaciones                   (opcional)


#CREACION DEL HISTORIAL
# En este paso se crea o define un historial que se usará de respuesta ante una opción futura
# Todos los datos para los historiales serán definidos en el proceso

                                        "HISTORIAL"
Nombre_del_paciente = "Juan Rodriguez"  #Nombre Definido solo para el historial de prueba
Cédula = 1717202045                     #importar el módulo de random/ radom.radint() 
Edad = 25                               #importar el módulo de random/ radom.radint()
Especialidad = Medicina General         #Opcional
Fecha_de_cita = 7/12/2025               #importar el módulo de random/ radom.radint()(formato: DD/MM/AAAA)
Hora_de_cita = 9:50                     #Variable/random de 8 am- 15 pm)
Motivo = "Mareos, Dolores de cabeza"    #No menos de letras 5 letras)
Codigo_de_cita = 557298                 #importar el módulo de random/ radom.radint()

print(                                  "HISTORIAL")
print("\n Nombre del paciente: ",Nombre_del_paciente)
print(" Cédula: ",Cédula)
print(" Edad: ", Edad)
print(" Especialidad: ",Especialidad)
print(" Fecha de cita: ",Fecha_de_cita)
print(" Hora de cita: ",Hora_de_cita)
print(" Motivo: ",Motivo)
print(" Código de cita: ",Codigo_de_cita)