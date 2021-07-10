from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# Class to store pokemon Data
class PokeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    type1 = db.Column(db.String, nullable=False)
    type2 = db.Column(db.String, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    sp_att = db.Column(db.Integer, nullable=False)
    sp_def = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    generation = db.Column(db.Integer, nullable=False)
    legendary = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Pokemon(Name={name}, Types={type1}, {type2} TotalStats={total}, HP={hp}, ATT={attack}, DEF={defense}, SP_ATT={sp_att}, SP_DEF={sp_def}, SPD={speed}. GENERATION: {generation}. LEGENDARY: {legendary}.)"


# Requestparser, to format data in a specific format.
poke_put_args = reqparse.RequestParser()
poke_put_args.add_argument(
    "name", type=str, help="Name of Pokemon is required.", required=True)
poke_put_args.add_argument(
    "type1", type=str, help="Type1 of Pokemon is required.", required=True)
poke_put_args.add_argument(
    "type2", type=str, help="Type2 of Pokemon is required.", required=True)
poke_put_args.add_argument(
    "total", type=int, help="TotalStat of Pokemon is required.", required=True)
poke_put_args.add_argument(
    "hp", type=int, help="HP of Pokemon is required.", required=True)
poke_put_args.add_argument(
    "attack", type=int, help="Attack of Pokemon is required.", required=True)
poke_put_args.add_argument(
    "defense", type=int, help="Defense of Pokemon is required.", required=True)
poke_put_args.add_argument(
    "sp_att", type=int, help="Sp Attack of Pokemon is required.", required=True)
poke_put_args.add_argument(
    "sp_def", type=int, help="Sp Defense of Pokemon is required.", required=True)
poke_put_args.add_argument(
    "speed", type=int, help="Speed of Pokemon is required.", required=True)
poke_put_args.add_argument(
    "generation", type=int, help="Generation of Pokemon is required.", required=True)
poke_put_args.add_argument(
    "legendary", type=str, help="Legendary? Pokemon is required.", required=True)


# UpdateRequestParser
poke_update_args = reqparse.RequestParser()
poke_update_args.add_argument(
    "name", type=str, help="Name of Pokemon is required.")
poke_update_args.add_argument(
    "type1", type=str, help="Type1 of Pokemon is required.")
poke_update_args.add_argument(
    "type2", type=str, help="Type2 of Pokemon is required.")
poke_update_args.add_argument(
    "total", type=int, help="TotalStat of Pokemon is required.")
poke_update_args.add_argument(
    "hp", type=int, help="HP of Pokemon is required.")
poke_update_args.add_argument(
    "attack", type=int, help="Attack of Pokemon is required.")
poke_update_args.add_argument(
    "defense", type=int, help="Defense of Pokemon is required.")
poke_update_args.add_argument(
    "sp_att", type=int, help="Sp Attack of Pokemon is required.")
poke_update_args.add_argument(
    "sp_def", type=int, help="Sp Defense of Pokemon is required.")
poke_update_args.add_argument(
    "speed", type=int, help="Speed of Pokemon is required.")
poke_update_args.add_argument(
    "generation", type=int, help="Generation of Pokemon is required.")
poke_update_args.add_argument(
    "legendary", type=str, help="Legendary? Pokemon is required.")

# Create database
# db.create_all()

# Resource fields, to parse data into database with marshal with
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'type1': fields.String,
    'type2': fields.String,
    'total': fields.Integer,
    'hp': fields.Integer,
    'attack': fields.Integer,
    'defense': fields.Integer,
    'sp_att': fields.Integer,
    'sp_def': fields.Integer,
    'speed': fields.Integer,
    'generation': fields.Integer,
    'legendary': fields.String
}


class Pokemon(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        result = PokeModel.query.filter_by(id=id).first()
        if not result:
            abort(404, message=f"Could not find Pokemon with the id <{id}>.")

        return result

    @marshal_with(resource_fields)
    def put(self, id):
        args = poke_put_args.parse_args()
        result = PokeModel.query.filter_by(id=id).first()
        if result:
            abort(409, message=f"Pokemon with id <{id}> already exists.")
        pokemon = PokeModel(id=id, name=args['name'], type1=args['type1'], type2=args['type2'], total=args['total'], hp=args['hp'], attack=args['attack'],
                            defense=args['defense'], sp_att=args['sp_att'], sp_def=args['sp_def'], speed=args['speed'], generation=args['generation'], legendary=args['legendary'])

        db.session.add(pokemon)
        db.session.commit()
        return pokemon, 201

    @marshal_with(resource_fields)
    def patch(self, id):
        args = poke_update_args.parse_args()
        result = PokeModel.query.filter_by(id=id).first()
        if not result:
            abort(404, message=f"Could not find Pokemon with id <{id}>")
        if args['name'] != None:
            result.name = args['name']
        if args['type1'] != None:
            result.type1 = args['type1']
        if args['type2'] != None:
            result.type2 = args['type2']
        if args['total'] != None:
            result.total = args['total']
        if args['hp'] != None:
            result.hp = args['hp']
        if args['attack'] != None:
            result.attack = args['attack']
        if args['defense'] != None:
            result.defense = args['defense']
        if args['sp_att'] != None:
            result.sp_att = args['sp_att']
        if args['sp_def'] != None:
            result.sp_def = args['sp_def']
        if args['speed'] != None:
            result.speed = args['speed']
        if args['generation'] != None:
            result.generation = args['generation']
        if args['legendary'] != None:
            result.legendary = args['legendary']

        db.session.commit()
        return result


# Register Resource
api.add_resource(Pokemon, "/pokemon/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
