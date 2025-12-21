# from flask import Flask, request, jsonify
# from bussiness import get_data
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route('/')
# def hello_world():

#     return 'HELLO WORLD!'

# @app.route('/api', methods=['GET'])
# def api():

#     data=get_data()

#     data = {"data":data}

#     return jsonify(data)

# if __name__ == '__main__':

#     app.run(port=8000, debug=True)



from flask import Flask, request, jsonify
from bussiness import get_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'HELLO WORLD!'

@app.route('/api', methods=['GET'])
def api():
    try:
        data = get_data()
        return jsonify({"data": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
