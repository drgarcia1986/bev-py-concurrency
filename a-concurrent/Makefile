start-falcon:
	gunicorn server-sync:api -b :8080

start-aiohttp:
	python server.py

start-siege:
	siege -c 100 -r 100 -b http://localhost:8080/3/
