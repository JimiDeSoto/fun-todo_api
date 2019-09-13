1. Przygotowanie srodowiska

	apt-get install python3-venv
	python3 -m venv flask
	exitflask/bin/pip install flask
	flask/bin/pip install flask-httpauth


2. Użycie


a) GET
http://localhost:5000/todo/api/v1.0/tasks
http://localhost:5000/todo/api/v1.0/tasks/"id"


b) POST
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks


c) Update
curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/2

