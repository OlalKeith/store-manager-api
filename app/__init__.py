from flask import Flask
from flask_restful import Api
from config import app_config


def create_app(config_name='testing'):

    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    api = Api(app)

    app.config.from_object(app_config['testing'])

    from .api.v1.views import ProductView
    from .api.v1.views import ProductId
    from .api.v1.sales import SalesView
    from .api.v1.sales import SalesId

    api.add_resource(ProductView, '/api/v1/product/<string:name>')
    api.add_resource(ProductId, '/api/v1/product/<int:product_id>')
    api.add_resource(SalesView, '/api/v1/sale/<string:name>')
    api.add_resource(SalesId, '/api/v1/sale/<int:sales_id>')

    return app
