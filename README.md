1. Przygotowanie srodowiska

	apt-get install python3-venv
	python3 -m venv flask
	exitflask/bin/pip install flask
2. Użycie
a) GET
http://localhost:5000/todo/api/v1.0/tasks
http://localhost:5000/todo/api/v1.0/tasks/"id"
b) POST
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks

