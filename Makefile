local:
	./build.py

serve: local
	cd htdocs && python3 -m SimpleHTTPServer
