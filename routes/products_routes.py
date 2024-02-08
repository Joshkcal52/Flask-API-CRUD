from flask import Blueprint, request, Response

from controllers import products_controller

product = Blueprint('product', __name__)


@product.route('/product', methods=["POST"])
def add_product():
    return products_controller.add_product(request)


@product.route('/product/<id>', methods=["GET"])
def get_product(id):
    return products_controller.get_product(id)


@product.route('/products', methods=["GET"])
def get_products():
    return products_controller.get_products()


@product.route('/product/active', methods=["GET"])
def get_active_products():
    return products_controller.get_active_products()


@product.route('/product/<product_id>', methods=["PATCH", "PUT"])
def update_product(product_id):
    return products_controller.update_product(request, product_id)


@product.route('/product/delete/<product_id>', methods=["DELETE"])
def delete_product(product_id):
    return products_controller.delete_product(product_id)
