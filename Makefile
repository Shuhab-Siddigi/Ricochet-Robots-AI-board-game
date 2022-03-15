
run:
	python3 .

graph:
	pyreverse .
	dot -Tpng classes.dot -o uml-graph.png
	rm classes.dot
	rm packages.dot