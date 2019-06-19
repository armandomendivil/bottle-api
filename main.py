from bottle import Bottle, get, post, put, delete, request
from bottle.ext.mongo import MongoPlugin

app = Bottle()

db_name = 'demo-api'
db_uri = ''
db_plugin = MongoPlugin(uri=db_uri, db=db_name)

app.install(db_plugin)

animals = [
	{ 'id': 0, 'name': 'Ellie', 'type': 'Elephant' },
	{ 'id': 1, 'name': 'Toby', 'type': 'Dog' },
	{ 'id': 2, 'name': 'Whiskas', 'type': 'Cat' }
]

def search(name):
	for animal in animals:
		if animal['name'] == name:
			return animal
	
	return None

@app.get('/')
def getAll(mongodb):
	print('here!!')
	mongodb['items'].insert({ 'key': 'value' })
	return { 'animals': animals }

@get('/animal/<name>')
def getOne(name):
	animal = search(name)
	return { 'animal': animal }

@post('/animal')
def addOne():
	name = request.json.get('name')
	type = request.json.get('type')

	new_animal = { 'name': name, 'type': type }
	animals.append(new_animal)

	return { 'animal': new_animal }

@put('/animal/<name>')
def updateOne():
	return None

@delete('/animal/<name>')
def removeOne(name):
	the_animal = [animal for animal in animals if animal.get('name') == name]
	animals.remove(the_animal[0])

	return { 'animals': the_animal }


app.run(debug=True, reloader=True)
