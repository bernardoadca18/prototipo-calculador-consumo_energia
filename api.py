from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

#############################################################
# RETORNANDO JSON
@app.route("/")
def index():
    return jsonify({"mensagem": "Hello Json!"})

#############################################################
# UTILIZANDO METALINGUAGEM JINJA
@app.route('/hello/')
@app.route('/hello/<nome>')
def hello(nome=None):
    return render_template('exemplo_hello.html', name=nome)

#############################################################
# PASSAGEM DE PARÂMETRO - NÚMERO INTEIRO
@app.route('/show/<int:id>')
def show(id):
    return 'Valor recebido id = %d' % id

#############################################################
# VERIFICANDO O METODO (VERBO HTTP) UTILIZADO
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Login via POST'
    else:
        return '''
            <html>
                <body>
                    <form method="post">
                    <p><input type=text name=username>
                    <p><input type=submit value=Login>
                    </form>
                </body>
            </html>
        '''

@app.route('/soma/<float:num_a>/<float:num_b>', methods=['GET'])
def soma(num_a, num_b):
    return jsonify({"soma": num_a + num_b})

@app.route('/subtrai/<float:num_a>/<float:num_b>', methods=['GET'])
def subtrai(num_a, num_b):
    return jsonify({"subtracao": num_a - num_b})

@app.route('/multiplica/<float:num_a>/<float:num_b>', methods=['GET'])
def multiplica(num_a, num_b):
    return jsonify({"multiplicacao": num_a * num_b})

@app.route('/divide/<float:num_a>/<float:num_b>', methods=['GET'])
def divide(num_a, num_b):
    if num_b == 0:
        return jsonify({"erro": "Divisao por zero!"}), 400
    return jsonify({"divisao": num_a / num_b})

@app.route('/soma/<int:num_a>/<int:num_b>', methods=['GET'])
def somaint(num_a, num_b):
    return jsonify({"soma": num_a + num_b})

@app.route('/subtrai/<int:num_a>/<int:num_b>', methods=['GET'])
def subtraiint(num_a, num_b):
    return jsonify({"subtracao": num_a - num_b})

@app.route('/multiplica/<int:num_a>/<int:num_b>', methods=['GET'])
def multiplicaint(num_a, num_b):
    return jsonify({"multiplicacao": num_a * num_b})

@app.route('/divide/<int:num_a>/<int:num_b>', methods=['GET'])
def divideint(num_a, num_b):
    if num_b == 0:
        return jsonify({"erro": "Divisao por zero!"}), 400
    return jsonify({"divisao": float(num_a) / float(num_b)})

@app.route('/soma/<float:num_a>/<int:num_b>', methods=['GET'])
def soma_float_int(num_a, num_b):
    return jsonify({"soma": num_a + float(num_b)})

@app.route('/soma/<int:num_a>/<float:num_b>', methods=['GET'])
def soma_int_float(num_a, num_b):
    return jsonify({"soma": float(num_a) + num_b})

@app.route('/subtrai/<float:num_a>/<int:num_b>', methods=['GET'])
def subtrai_float_int(num_a, num_b):
    return jsonify({"subtracao": num_a - float(num_b)})

@app.route('/subtrai/<int:num_a>/<float:num_b>', methods=['GET'])
def subtrai_int_float(num_a, num_b):
    return jsonify({"subtracao": float(num_a) - num_b})

@app.route('/multiplica/<float:num_a>/<int:num_b>', methods=['GET'])
def multiplica_float_int(num_a, num_b):
    return jsonify({"multiplicacao": num_a * float(num_b)})

@app.route('/multiplica/<int:num_a>/<float:num_b>', methods=['GET'])
def multiplica_int_float(num_a, num_b):
    return jsonify({"multiplicacao": float(num_a) * num_b})

@app.route('/divide/<float:num_a>/<int:num_b>', methods=['GET'])
def divide_float_int(num_a, num_b):
    if num_b == 0:
        return jsonify({"erro": "Divisao por zero!"}), 400
    return jsonify({"divisao": num_a / float(num_b)})

@app.route('/divide/<int:num_a>/<float:num_b>', methods=['GET'])
def divide_int_float(num_a, num_b):
    if num_b == 0:
        return jsonify({"erro": "Divisao por zero!"}), 400
    return jsonify({"divisao": float(num_a) / num_b})

#############################################################
# Pagina nao encontrada - erro 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('exemplo_error.html'), 404

#############################################################
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
