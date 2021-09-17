from flask import Flask
from views.view_index import index_blueprint
from views.view_test import test_blueprint
from views.view_coverage import coverage_blueprint

app = Flask(__name__)
app.register_blueprint(index_blueprint)
app.register_blueprint(test_blueprint)
app.register_blueprint(coverage_blueprint)
# print(app)

if __name__ == '__main__':
    app.run(debug=True)