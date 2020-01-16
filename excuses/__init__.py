from flask import Flask
from .settings import DevelopmentConfig, ProductionConfig, TestingConfig

def create_app(config=None):
    app = Flask(__name__)

    if config == 'prod':
        app.config.from_object(ProductionConfig)
    elif config == 'test':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    @app.route('/health')
    def health():
        return 'healthy'

    return app

