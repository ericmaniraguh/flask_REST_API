from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort

# -------------------- APP SETUP --------------------
app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

# -------------------- DATABASE MODEL --------------------
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}, {self.email}>'

# -------------------- REQUEST PARSER --------------------
user_args = reqparse.RequestParser()
user_args.add_argument("username", type=str, required=True, help="Username cannot be blank!")
user_args.add_argument("email", type=str, required=True, help="Email cannot be blank!")  

userFields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String
}

# -------------------- API RESOURCES --------------------
class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        """Get all users"""
        users = UserModel.query.all()
        return users, 200

    @marshal_with(userFields)
    def post(self):
        """Create one or multiple users"""
        data = request.get_json()
        if isinstance(data, list):  # Multiple users
            new_users = []
            for u in data:
                if 'username' not in u or 'email' not in u:
                    abort(400, message="Each user must have username and email")
                if UserModel.query.filter_by(email=u['email']).first():
                    continue  # Skip duplicates by email
                user = UserModel(username=u['username'], email=u['email'])
                db.session.add(user)
                new_users.append(user)
            db.session.commit()
            return new_users, 201
        elif isinstance(data, dict):  # Single user
            if 'username' not in data or 'email' not in data:
                abort(400, message="Username and email required")
            if UserModel.query.filter_by(email=data['email']).first():
                abort(400, message="User with this email already exists")
            user = UserModel(username=data['username'], email=data['email'])
            db.session.add(user)
            db.session.commit()
            return user, 201
        else:
            abort(400, message="Invalid data format")

class User(Resource):
    @marshal_with(userFields)
    def get(self, user_id):
        """Get a single user by ID"""
        user = UserModel.query.get(user_id)
        if not user:
            abort(404, message="User not found")
        return user, 200

# put method for full updates
    @marshal_with(userFields)
    def put(self, user_id):
        """Update a user by ID"""
        user = UserModel.query.get(user_id)
        if not user:
            abort(404, message="User not found")
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        db.session.commit()
        return user, 200
    
    # patch method for partial updates
    @marshal_with(userFields)
    def patch(self, user_id):
        """Partial update"""
        user = UserModel.query.get(user_id)
        if not user:
            abort(404, message="User not found")
        data = request.get_json()
        if 'username' in data:
            user.username = data['username']
        if 'email' in data:
            user.email = data['email']
        db.session.commit()
        return user, 200

    def delete(self, user_id):
        """Delete a user by ID"""
        user = UserModel.query.get(user_id)
        if not user:
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully"}, 200

# -------------------- ROUTES --------------------
api.add_resource(Users, "/api/users/")
api.add_resource(User, "/api/users/<int:user_id>")

@app.route('/', methods=['GET'])
def home():
    return '<h1>Welcome to the Home REST API Page</h1>'

# -------------------- RUN --------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure database tables are created
    app.run(debug=True)
