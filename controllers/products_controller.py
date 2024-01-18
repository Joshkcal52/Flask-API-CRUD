from flask import jsonify
import flask

from data import product_records


def get_product(id):
    for product in product_records:
        if product["product_id"] == int(id):
            return jsonify({"message": "product_found", "results": product}), 200
    return jsonify({"message": f'Product with id {id} not found.'}), 400


def add_product(req: flask.Request) -> flask.Response:
    data = req.get_json()

    new_product = {
        'product_id': len(product_records) + 1,
        'name': data['name'],
        'description': data['description'],
        'price': data['price'],
        'active': data['active']
    }

    product_records.append(new_product)

    return jsonify({"message": "product_created", "result": new_product}), 201


def get_products():
    if product_records:
        return jsonify({"message": "products_found", "results": product_records}), 200


def get_active_products():
    active_products = []

    for product in product_records:
        if product["active"] == True:
            active_products.append(product)
    return jsonify({"message": "active products", "results": active_products}), 200


def update_product(req: flask.Request, product_id) -> flask.Response:
    post_data = req.get_json()

    record = None

    for product in product_records:
        if product["product_id"] == int(product_id):
            record = product

    name = post_data.get("name")
    description = post_data.get("description")
    price = post_data.get("price")
    active = post_data.get("active")

    if name and name is not None:
        record["name"] = name

    if description and description is not None:
        record["description"] = description

    if price and price is not None:
        record["price"] = price

    if active and active is not None:
        record["active"] = active

    return jsonify({"message": "record updated", "record": record}), 200


def delete_product(product_id):
    record = None

    for product in product_records:
        if product["product_id"] == int(product_id):
            record = product

    if record is not None:
        product_records.remove(record)
        return jsonify({"message": "record deleted"}), 200
    else:
        return jsonify({"message": "record not found"}), 404
