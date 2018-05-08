from flask import Flask
from src.common.database import Database

app = Flask(__name__)
app.config.from_object('src.config')
app.secret_key = "123"  # should be random 32 characters

@app.before_first_request
def init_db():
    Database.initialze()


from src.models.users.views import user_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")



