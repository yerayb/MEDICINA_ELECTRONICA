from flask import Flask, request, jsonify, Response, render_template, make_response, send_from_directory
from flask_pymongo import PyMongo
from flask_pymongo import pymongo
import hashlib
from bson import json_util
import os
import logging

app = Flask(__name__,template_folder='templates')

client = pymongo.MongoClient("mongodb+srv://admin:CZQswrnqp0s2BZOx@cluster0.7tlre.mongodb.net/medb?retryWrites=true&w=majority")  
collection_medicos = client.medb.medicos
collection_users = client.medb.users
collection_pacientes = client.medb.pacientes
collection_prescripciones = client.medb.prescripciones

# --------------------- HTML RENDERS ---------------------
@app.route('/', methods=["GET"])
def login_index():
     return render_template('FrontPM/Login/index.html')

@app.route('/Admin/index.html', methods=["GET"])
def admin_index():
     return render_template('FrontPM/Admin/index.html')

@app.route('/Admin/Medicos/ver-medicos.html', methods=["GET"])
def ver_medicos():
     return render_template('FrontPM/Admin/Medicos/ver-medicos.html')

@app.route('/Admin/Medicos/agregar-medico.html', methods=["GET"])
def agregar_medicos():
     return render_template('FrontPM/Admin/Medicos/agregar-medico.html')

@app.route('/Admin/Medicos/busqueda-modificar-medico.html', methods=["GET"])
def busqueda_modificar_medicos():
     return render_template('FrontPM/Admin/Medicos/busqueda-modificar-medico.html')

@app.route('/Admin/Medicos/modificar-medico.html', methods=["GET"])
def modificar_medicos():
     return render_template('FrontPM/Admin/Medicos/modificar-medico.html')

@app.route('/Admin/Medicos/borrar-medico.html', methods=["GET"])
def borrar_medico():
     return render_template('FrontPM/Admin/Medicos/borrar-medico.html')

@app.route('/Admin/Pacientes/ver-pacientes.html', methods=["GET"])
def ver_paciente():
     return render_template('FrontPM/Admin/Pacientes/ver-pacientes.html')

@app.route('/Admin/Pacientes/agregar-paciente.html', methods=["GET"])
def agregar_pacientes():
     return render_template('FrontPM/Admin/Pacientes/agregar-paciente.html')

@app.route('/Admin/Pacientes/busqueda-modificar-paciente.html', methods=["GET"])
def busqueda_modificar_pacientes():
     return render_template('FrontPM/Admin/Pacientes/busqueda-modificar-paciente.html')

@app.route('/Admin/Pacientes/borrar-paciente.html', methods=["GET"])
def borrar_pacientes():
     return render_template('FrontPM/Admin/Pacientes/borrar-paciente.html')

@app.route('/Admin/Pacientes/modificar-paciente.html', methods=["GET"])
def modificar_pacientes():
     return render_template('FrontPM/Admin/Pacientes/modificar-paciente.html')

@app.route('/WebMedico/configPass.html', methods=["GET"])
def generar_pass_medico():
     return render_template('FrontPM/WebMedico/configPass.html')

@app.route('/WebMedico/index.html', methods=["GET"])
def app_medico():
     return render_template('FrontPM/WebMedico/index.html')
    
@app.route('/sw.js')
def sw():
    response=make_response(
                     send_from_directory('static',filename='Pwa/sw.js'))
    #change the content header file
    response.headers['Content-Type'] = 'application/javascript'
    return response

@app.route('/main.js')
def main_js():
    response=make_response(
                     send_from_directory('static',filename='Pwa/main.js'))
    #change the content header file
    response.headers['Content-Type'] = 'application/javascript'
    return response

@app.route('/WebMedico/Prescripcion/ver-prescripciones', methods=["GET"])
def ver_prescripciones():
     return render_template('FrontPM/WebMedico/Prescripcion/ver-prescripcion.html')

@app.route('/WebMedico/Prescripcion/agregar-prescripcion', methods=["GET"])
def agregar_prescripciones():
     return render_template('FrontPM/WebMedico/Prescripcion/agregar-prescripcion.html')

@app.route('/WebMedico/Prescripcion/borrar-prescripcion', methods=["GET"])
def borrar_prescripciones():
     return render_template('FrontPM/WebMedico/Prescripcion/borrar-prescripcion.html')
##/WebMedico/Prescripcion/borrar-prescripcion
# --------------------- USERS ---------------------
@app.route('/user', methods=['GET'])
def validar_usuario():
    # Obtener Request Params
    usuario = request.args.get('user')
    contraseña = request.args.get('contraseña')

    # Cifrar
    contraseña_cifrada = hashlib.sha512(contraseña.encode())

    # Buscar Usuario en la DB
    # Devuelve JSON con toda la informacion
    userDB = collection_users.find_one({'usuario': usuario})

    # Usuario no existe en la DB
    if userDB == None:
        return {"usuarioValido": False}

    # Usuario es Admin
    elif userDB['usuario'] == "admin" and userDB['contraseña'] == contraseña_cifrada.hexdigest():
        return {"usuarioValido": True, "tipoUsuario": 0}

    #Usuario es Medico y no ha configurado contraseña
    elif userDB['usuario'] != "admin" and not "contraseña" in userDB:
        return {"usuarioValido": True, "tipoUsuario": 1, "usuario": userDB['usuario']}

    #Usuario es Medico y tiene contraseña
    # Usuario es Medico y no ha configurado contraseña
    elif userDB['usuario'] != "admin" and "contraseña" in userDB and userDB['contraseña'] == contraseña_cifrada.hexdigest():
        return {"usuarioValido": True, "tipoUsuario": 2, "usuario": userDB['usuario']}

    else:
        return {"usuarioValido": False}

@app.route('/user/<dni>', methods=['DELETE'])
def delete_user(dni):
    print(dni)
    collection_users.delete_one({'dni': str(dni)})
    response = jsonify({'message': 'Usuario ' + dni + 'borrado'})
    return response

@app.route('/user/<nickname>', methods=['POST'])
def crear_pass_user(nickname):
    nicknameJSON = nickname
    contraseñaJSON = request.json['contraseña']


    # Cifrar
    contraseña_cifrada = hashlib.sha512(contraseñaJSON.encode())

    if nicknameJSON and contraseñaJSON:
        userDB = collection_users.find_one({'usuario': str(nicknameJSON)})
        if userDB != None:
            collection_users.update_one({'usuario': str(nicknameJSON)}, {'$set': {
                    'contraseña': contraseña_cifrada.hexdigest()

            }})

            response = jsonify({'message': 'usuario' + nickname + 'ha obtenido su contraseña correctamente.'})
            return response

# --------------------- MEDICOS ---------------------
@app.route('/medicos', methods=['GET'])
def obtener_medicos():
    # Buscar Medicos en la DB
    # Devuelve BSON con toda la informacion
    medicosDB = collection_medicos.find().sort([("centroMedico", 1)])

    # Convierte BSON en JSON
    medicos = json_util.dumps(medicosDB)

    return Response(medicos, mimetype='application/json')


@app.route('/medico', methods=['POST'])
def agregar_medico():
    dniJSON = request.json['dni']
    nombreJSON = request.json['nombre']
    primerApellidoJSON = request.json['primerApellido']
    segundoApellidoJSON = request.json['segundoApellido']
    centroMedicoJSON = request.json['centroMedico']
    anyoNacimientoJSON = request.json['anyoNacimiento']
    anyoContratacionJSON = request.json['anyoContratacion']
    salarioJSON = request.json['salario']
    especialidadJSON = request.json['especialidad']

    # validar que se rellenan todos los campos
    if dniJSON and nombreJSON and primerApellidoJSON and segundoApellidoJSON and centroMedicoJSON and anyoNacimientoJSON and anyoContratacionJSON and salarioJSON and especialidadJSON:

        # validar dni
        if len(dniJSON) != 9:
            response = not_found500("El DNI introducido es incorrecto")
            return response

        # validar año nacimiento
        if len(anyoNacimientoJSON) != 4:
            response = not_found500("El año de nacimiento introducido es incorrecto")
            return response

        if len(anyoContratacionJSON) != 4:
            response = not_found500("El año de contratacion introducido es incorrecto")
            return response

        # validar que no existe el usuario
        if collection_medicos.find_one({'dni': dniJSON}) is None:
            collection_medicos.insert_one(
                {
                    'dni': dniJSON,
                    'nombre': nombreJSON,
                    'primerApellido': primerApellidoJSON,
                    'segundoApellido': segundoApellidoJSON,
                    'centroMedico': centroMedicoJSON,
                    'anyoNacimiento': anyoNacimientoJSON,
                    'anyoContratacion': anyoContratacionJSON,
                    'salario': salarioJSON,
                    'especialidad': especialidadJSON

                }
            )
            nombreUsuario = nombreJSON[:2].lower() + primerApellidoJSON[:2].lower()+ segundoApellidoJSON[:2].lower()

            collection_users.insert_one(
                {
                    'dni': dniJSON,
                    'usuario': nombreUsuario.lower()
            })

            response = jsonify({'message': 'medico' + dniJSON + 'modificado correctamente.'})


        # usuario existe
        else:
            response = not_found500("El medico introducido ya existe")

    return response


@app.route('/medico/<dni>', methods=['DELETE'])
def delete_medico(dni):
    print(dni)
    collection_medicos.delete_one({'dni': str(dni)})
    response = jsonify({'message': 'Medico ' + dni + 'borrado'})
    return response


@app.route('/medico/<dni>', methods=['GET'])
def obtener_medico(dni):
    medicoDB = collection_medicos.find_one({'dni': str(dni)})

    # Convierte BSON en JSON
    medico = json_util.dumps(medicoDB)

    return Response(medico, mimetype='application/json')


@app.route('/medico/<dni>', methods=['POST'])
def modificar_medico(dni):
    dniJSON = request.json['dni']
    nombreJSON = request.json['nombre']
    primerApellidoJSON = request.json['primerApellido']
    segundoApellidoJSON = request.json['segundoApellido']
    centroMedicoJSON = request.json['centroMedico']
    anyoNacimientoJSON = request.json['anyoNacimiento']
    anyoContratacionJSON = request.json['anyoContratacion']
    salarioJSON = request.json['salario']
    especialidadJSON = request.json['especialidad']

    if dniJSON and nombreJSON and primerApellidoJSON and segundoApellidoJSON and centroMedicoJSON and anyoNacimientoJSON and anyoContratacionJSON and salarioJSON and especialidadJSON:
        medicoDB = collection_medicos.find_one({'dni': str(dni)})
        if medicoDB != None:
            collection_medicos.update_one({'dni': str(dni)}, {'$set': {
                'nombre': nombreJSON,
                'primerApellido': primerApellidoJSON,
                'segundoApellido': segundoApellidoJSON,
                'centroMedico': centroMedicoJSON,
                'anyoNacimiento': anyoNacimientoJSON,
                'anyoContratacion': anyoContratacionJSON,
                'salario': salarioJSON,
                'especialidad': especialidadJSON

            }})

            nombreUsuario = nombreJSON[:2]+primerApellidoJSON[:2] +segundoApellidoJSON[:2]
            collection_users.update_one({'dni': str(dni)}, {'$set': {
                'usuario': nombreUsuario.lower()
            }})

            response = jsonify({'message': 'medico' + dni + 'modificado correctamente.'})

            return Response(response, mimetype='application/json')




# --------------------- PACIENTES ---------------------
@app.route('/pacientes', methods=['GET'])
def obtener_pacientes():
    # Buscar Medicos en la DB
    # Devuelve BSON con toda la informacion
    pacientesDB = collection_pacientes.find().sort([("nombre", 1)])

    # Convierte BSON en JSON
    pacientes = json_util.dumps(pacientesDB)

    return Response(pacientes, mimetype='application/json')


@app.route('/paciente', methods=['POST'])
def agregar_paciente():
    dniJSON = request.json['dni']
    nombreJSON = request.json['nombre']
    primerApellidoJSON = request.json['primerApellido']
    segundoApellidoJSON = request.json['segundoApellido']
    direccionJSON = request.json['direccion']
    anyoNacimientoJSON = request.json['anyoNacimiento']
    cpJSON = request.json['cp']
    municipioJSON = request.json['municipio']
    provinciaJSON = request.json['provincia']
    telefonoJSON = request.json['telefono']
    emailJSON = request.json['email']
    sexoJSON = request.json['sexo']

    # validar que se rellenan todos los campos
    if dniJSON and nombreJSON and primerApellidoJSON and segundoApellidoJSON and direccionJSON and anyoNacimientoJSON and cpJSON and municipioJSON and provinciaJSON and telefonoJSON and emailJSON and sexoJSON:
        # validar dni
        if len(dniJSON) != 9:
            response = not_found500("El DNI introducido es incorrecto")
            return response

        # validar año nacimiento
        if len(anyoNacimientoJSON) != 4:
            response = not_found500("El año de nacimiento introducido es incorrecto")
            return response

        # validar telefono
        if len(telefonoJSON) != 9:
            response = not_found500("El numero de telefono introducido es incorrecto")
            return response

        # validar email
        if "@" not in emailJSON or "." not in emailJSON:
            response = not_found500("El correo electronico introducido es incorrecto")
            return response

        # validar que no existe el usuario
        if collection_pacientes.find_one({'dni': dniJSON}) is None:
            collection_pacientes.insert_one(
                {
                    'dni': dniJSON,
                    'nombre': nombreJSON,
                    'primerApellido': primerApellidoJSON,
                    'segundoApellido': segundoApellidoJSON,
                    'direccion': direccionJSON,
                    'anyoNacimiento': anyoNacimientoJSON,
                    'CP': cpJSON,
                    'municipio': municipioJSON,
                    'provincia': provinciaJSON,
                    'telefono': telefonoJSON,
                    'email': emailJSON,
                    'sexo': sexoJSON

                }
            )
            response = {
                'dni': dniJSON
            }

        # usuario existe
        else:
            response = not_found500("El medico introducido ya existe")

    return response


@app.route('/paciente/<dni>', methods=['DELETE'])
def delete_paciente(dni):
    print(dni)
    collection_pacientes.delete_one({'dni': str(dni)})
    response = jsonify({'message': 'Paciente ' + dni + 'borrado'})
    return response


@app.route('/paciente/<dni>', methods=['GET'])
def obtener_paciente(dni):
    pacienteDB = collection_pacientes.find_one({'dni': str(dni)})

    if pacienteDB != None:
        response = json_util.dumps(pacienteDB)

        return Response(response, mimetype='application/json')

    else:
        return not_found500("El paciente no existe")




@app.route('/paciente/<dni>', methods=['POST'])
def modificar_paciente(dni):
    dniJSON = request.json['dni']
    nombreJSON = request.json['nombre']
    primerApellidoJSON = request.json['primerApellido']
    segundoApellidoJSON = request.json['segundoApellido']
    direccionJSON = request.json['direccion']
    anyoNacimientoJSON = request.json['anyoNacimiento']
    cpJSON = request.json['CP']
    municipioJSON = request.json['municipio']
    provinciaJSON = request.json['provincia']
    telefonoJSON = request.json['telefono']
    emailJSON = request.json['email']
    sexoJSON = request.json['sexo']

    if dniJSON and nombreJSON and primerApellidoJSON and segundoApellidoJSON and direccionJSON and anyoNacimientoJSON and cpJSON and municipioJSON and provinciaJSON and telefonoJSON and emailJSON and sexoJSON:
        pacienteDB = collection_pacientes.find_one({'dni': str(dni)})
        if pacienteDB != None:
            collection_pacientes.update_one({'dni': str(dni)}, {'$set': {
                    'nombre': nombreJSON,
                    'primerApellido': primerApellidoJSON,
                    'segundoApellido': segundoApellidoJSON,
                    'direccion': direccionJSON,
                    'anyoNacimiento': anyoNacimientoJSON,
                    'CP': cpJSON,
                    'municipio': municipioJSON,
                    'provincia': provinciaJSON,
                    'telefono': telefonoJSON,
                    'email': emailJSON,
                    'sexo': sexoJSON

            }})

            response = jsonify({'message': 'paciente' + dni + 'modificado correctamente.'})
            return Response(response, mimetype='application/json')


# --------------------- CONFIG ---------------------
@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE");

    return response


@app.errorhandler(500)
def not_found500(msg, error=None):
    response = jsonify({
        'mensaje': msg,
        'status': 500
    })

    response.status_code = 500

    return response


# --------------------- PRESCRIPCIONES ---------------------
@app.route('/prescripciones', methods=['GET'])
def obtener_prescripciones():
    prescripcionesDB = collection_prescripciones.find().sort([("FechaEmision", 1)])

    # Convierte BSON en JSON
    prescripciones = json_util.dumps(prescripcionesDB)

    return Response(prescripciones, mimetype='application/json')

@app.route('/prescripcion', methods=['POST'])
def agregar_prescripcion():
    idPrescripcionJSON = request.json['idPrescripcion']
    dniJSON = request.json['dniPaciente']
    especialidadJSON = request.json['especialidad']
    prestacionJSON = request.json['prestacion']
    fechaEmisionJSON = request.json['fechaEmision']
    cantidadJSON = request.json['cantidad']
    observacionesJSON = request.json['observaciones']


    # validar que se rellenan todos los campos
    if dniJSON  and especialidadJSON and prestacionJSON and fechaEmisionJSON and cantidadJSON and idPrescripcionJSON:
        # validar dni
        if len(dniJSON) != 9:
            response = not_found500("El DNI introducido es incorrecto")
            return response

        # validar año nacimiento
        if cantidadJSON.isnumeric() is False:
            response = not_found500("La cantidad introducida es incorrecta")
            return response

        # validar que  existe el usuario
        userDB = collection_pacientes.find_one({'dni': dniJSON})
        if userDB is not None:
            collection_prescripciones.insert_one(
                {
                    'idPrescripcion': idPrescripcionJSON,
                    'dniPaciente': dniJSON,
                    'Paciente': userDB['nombre'] + " "+  userDB['primerApellido']+ " " +userDB['segundoApellido'],
                    'Especialidad': especialidadJSON,
                    'Prestacion': prestacionJSON,
                    'FechaEmision': fechaEmisionJSON,
                    'Cantidad': cantidadJSON,
                    'Observaciones': observacionesJSON

                }
            )
            response = {
                'dni': dniJSON
            }

        # usuario existe
        else:
            response = not_found500("El paciente introducido no existe")

    return response

@app.route('/prescripcion/<idPrescripcion>', methods=['GET'])
def obtener_prescripcion_byID(idPrescripcion):
    prescripcionDB = collection_prescripciones.find_one({'idPrescripcion': str(idPrescripcion)})
    if prescripcionDB != None:
        response = json_util.dumps(prescripcionDB)

        return Response(response, mimetype='application/json')
    else:
        return not_found500("El paciente no existe")

    return response
    

@app.route('/prescripcion/<idPrescripcion>', methods=['DELETE'])
def delete_prescripcion(idPrescripcion):
    collection_prescripciones.delete_one({'idPrescripcion': str(idPrescripcion)})
    response = jsonify({'message': 'Paciente ' + idPrescripcion + 'borrado'})
    return response


# --------------------- LEVANTAR BACKEND ---------------------

if __name__ == "__main__":
    app.run(debug=True)
