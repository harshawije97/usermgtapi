from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db = SQLAlchemy(app)
api = Api(app)


# Create class model
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    dob = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"User(name={self.name}, email={self.email}, dob={self.dob})"


user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'dob': fields.Integer
}

validate = reqparse.RequestParser()
validate.add_argument('name', type=str, required=True,
                      help="User's name is required")
validate.add_argument('email', type=str, required=True,
                      help="User's email is required")
validate.add_argument('dob', type=str, required=False)


# create a resource & get all resources
class Users(Resource):
    @marshal_with(user_fields)
    def get(self):
        users = UserModel.query.all()
        return users

    @marshal_with(user_fields)
    def post(self):
        # validate data
        args = validate.parse_args()
        new_user = UserModel(
            name=args["name"], email=args["email"], dob=args["dob"])
        db.session.add(new_user)
        db.session.commit()
        return "User Created Successfully", 201


# get the resource by Id
class User(Resource):
    @marshal_with(user_fields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User cannot be found")
        return user

    # TODO:: Test this
    @marshal_with(user_fields)
    def patch(self, id):
        update_user = reqparse.request.get_json() or {}
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User cannot be found")

        # Guard which field user has access to
        allowed_fields = ['name', 'email', 'dob']

        for field, value in update_user.items():
            if field in allowed_fields and hasattr(user, field):
                setattr(user, field, value)
            else:
                return f"Field '{field}' does not exist on User model", 404

        db.session.commit()
        return user

    @marshal_with(user_fields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User cannot be found")
        db.session.delete(user)
        db.session.commit()
        return user, 204


# inisialize the resources
api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/user/<int:id>')


@app.route("/")
def index():
    return '<h2>Hello dear flask user 👋 This is your index route </h2>'


if __name__ == "__main__":
    app.run(debug=True)
