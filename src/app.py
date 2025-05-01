from flask import Flask, jsonify
from flask import request


todos = [
    { "label": "My first task", "done": False }
]


# Crear la instancia de la aplicación Flask
app = Flask(__name__)


# Definir el endpoint /todos con el método GET
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos), 200 


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos), 200



@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
     del todos[position]
     return jsonify(todos), 200
    else:
         return jsonify({"error": "Posición no válida"}), 400
    



# Asegurarte de que estas líneas sean las últimas en tu archivo app.py
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
