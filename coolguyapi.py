from flask import Flask, request
from flask_restful import reqparse, Resource, Api

app = Flask(__name__)
api = Api(app)

guys = {
  'cool_guys': ['Preston', 'Anthony'],
  'uncool_guys': ['Connor', 'Neil', 'Kevin'],
  'late_guys': ['John']
}

parser = reqparse.RequestParser()
parser.add_argument('cool_guys', action='append')
parser.add_argument('uncool_guys', action='append')
parser.add_argument('late_guys', action='append')

class Is_A_Cool_Guy(Resource):
  def get(self, name):
    if (name in guys['cool_guys']):
      return name + " is a cool guy!"
    elif (name in guys['uncool_guys']):
      return name + " is an uncool guy :("
    elif (name in guys['late_guys']):
      return name + " is a late guy and needs to get his life together. Not cool, guy..."
    else:
      return name + " might be a cool guy but isn't cool enough to get in my cool guy list"

class Update_Guys(Resource):
  def post(self):
    args = parser.parse_args()
    cool = args['cool_guys']
    uncool = args['uncool_guys']
    late = args['late_guys']
    
    for guy in cool:
      if (guy in guys['cool_guys']):
        guys['cool_guys'].remove(guy)
      else:
        guys['cool_guys'].append(guy)

    for guy in uncool:
      if (guy in guys['uncool_guys']):
        guys['uncool_guys'].remove(guy)
      else:
        guys['uncool_guys'].append(guy)

    for guy in late:
      if (guy in guys['late_guys']):
        guys['late_guys'].remove(guy)
      else:
        guys['late_guys'].append(guy)

    return guys
    
api.add_resource(Is_A_Cool_Guy, '/isacoolguy/<name>')
api.add_resource(Update_Guys, '/update')

if __name__ == '__main__':
  app.run(port='3010')