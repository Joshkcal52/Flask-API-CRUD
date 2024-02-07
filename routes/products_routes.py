from flask import Blueprint, request, Response

import controllers

product = Blueprint('product', __name__)


@product.route('/product', methods=["POST"])
def add_product():
    return controllers.add_product(request)


@product.route('/product/<id>', methods=["GET"])
def get_product(id):
    return controllers.get_product(id)


@product.route('/products', methods=["GET"])
def get_products():
    return controllers.get_products()


@product.route('/product/active', methods=["GET"])
def get_active_products():
    return controllers.get_active_products()


@product.route('/product/<product_id>', methods=["PATCH", "PUT"])
def update_product(product_id):
    return controllers.update_product(request, product_id)


@product.route('/product/delete/<product_id>', methods=["DELETE"])
def delete_product(product_id):
    return controllers.delete_product(product_id)
