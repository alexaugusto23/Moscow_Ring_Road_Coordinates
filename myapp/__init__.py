from flask import Flask
from .views import index_blueprint
import os

API_KEY = os.environ.get('API_KEY')

app = Flask(__name__)
app.register_blueprint(index_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
    print(API_KEY)