from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [{'name':'sla','id':1}]

@app.route('/usuarios', methods=["GET"])
def ler_user():
    return jsonify({"usuarios":usuarios})


@app.route('/usuarios', methods=["POST"])
def criarUsuario():    
    data = request.json
    usuario = {'name':data['name'], 'id':len(usuarios)+1}
    usuarios.append(usuario)

@app.route('/usuarios/<int:id>', methods=["DELETE"])
def user_delete(id):
    for id in range(len(usuarios)):
            if id == usuarios['id']:
                usuarios.remove(id)



if __name__ == '__main__':
    app.run(debug=True)