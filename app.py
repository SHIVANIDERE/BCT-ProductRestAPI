from flask import Flask, request, jsonify
from flask.helpers import make_response
from service import ProductService

app = Flask(__name__)
service = ProductService()

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = "Content-Type,Access-Control-Allow-Headers"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE, OPTIONS"

    return response

@app.route('/')
def index():
    return "Welcome to Products List"

@app.route('/products',methods = ['GET'])
def get_all_products():
    return jsonify(service.get_all())

@app.route('/products/<product_id>',methods = ['GET'])
def get_productbyid(product_id):
        return jsonify(service.get_by_id(product_id))

@app.route('/products',methods = ['POST'])
def save_user():
    return jsonify(service.create(request.form))

@app.route('/products/<product_id>',methods = ['PUT','PATCH'])
def update_product_id(product_id):
    return jsonify(service.update(product_id,request.form))

@app.route('/products/<product_id>',methods = ['DELETE'])
def delete_product_id(product_id):
    return jsonify(service.delete(product_id))

@app.errorhandler(404)
def error_not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)

if __name__ == "__main__":
    app.run(debug=True,port=8000)