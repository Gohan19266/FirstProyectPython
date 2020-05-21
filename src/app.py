from flask import Flask, jsonify, request
from UsuarioDAO import Usuario
from FacultyDAO import Faculty
users = Usuario()
facul = Faculty()
app = Flask(__name__)


@app.route('/home',methods=['GET'])
def listar():
  	return jsonify({'mensaje':'Bienvenidos a Flask'})



'''Usuarios'''
@app.route('/usuarios/readAll', methods=['GET'])
def productos():
    try:
        rows = users.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)

@app.route('/usuarios/read/<int:id>')
def ReadUser(id):
	try:
		users.idusuario = id
		row = users.ReadUser()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
        
@app.route('/usuarios/add', methods=['POST'])
def AddUsers():
    try:
        _json = request.json
        users.nomuser=_json['nombre']
        users.clave=_json['passs']
        print(users.clave,users.nomuser)
        if request.method=='POST':
            resp=users.AddUsuario()
            resp=jsonify('USUARIO')
            resp.status_code=200
        return resp
    except Exception as e:
        print(e)

@app.route('/usuarios/update', methods=['PUT'])
def updateuser():
    try:
        _json=request.json
        users.nomuser=_json['name']
        users.clave=_json['passs']
        users.estado=_json['state']
        users.idusuario=_json['iduser']
        if request.method == 'PUT':
            resp = users.Updateuser()
            resp = jsonify('Usuario Modificado')
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
@app.route('/faculty/add', methods=['POST'])
def AddFaculty():
    try:
        _json = request.json
        facul.nombre=_json['name']
        facul.director=_json['direct']
        print(facul.director,facul.nombre)
        if request.method=='POST':
            resp=users.AddUsuario()
            resp=jsonify('USUARIO')
            resp.status_code=200
        return resp
    except Exception as e:
        print(e)


#---Faculty---#

@app.route('/faculty/readAll', methods=['GET'])
def FacultyReadAll():
    try:
        rows = facul.ReadAllFaculty()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)


if __name__ == "__main__":
	app.run(host="localhost", port=5000, debug=True)