sample.pdf: a.out
	python graph.py
a.out: sample.dat
	cc sample.c