extract: main bib

main: eqalg.tex
	sed -n 46,207p eqalg.tex > main

bib: eqalg.tex
	sed -n 210,217p eqalg.tex > bib

dummy:
	echo DUMMY paper4/main > main

clean:
	rm -f main
	rm -f bib
