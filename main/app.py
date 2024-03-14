from flask import Flask, jsonify, request

app = Flask(__name__)

users = [{'name':'sla','id':1}]

@app.route('/users', methods=["GET"])
def readUser():
    return jsonify({"users":users})


@app.route('/users', methods=["POST"])
def createUser():    
    data = request.json
    user = {'name':data['name'], 'id':len(users)+1}
    users.append(user)

@app.route('/usuarios/<int:id>', methods=["DELETE"])
def user_delete(id):
    for id in range(len(users)):
            if id == users['id']:
                users.remove(id)



if __name__ == '__main__':
    app.run(debug=True)