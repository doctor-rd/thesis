extract: dep main bib

dep: eqalg.tex
	sed -n 37,43p eqalg.tex > dep

main: eqalg.tex
	sed -n 46,207p eqalg.tex > main


bib: eqalg.tex
	sed -n 210,217p eqalg.tex > bib

clean:
	rm -f dep
	rm -f main
	rm -f bib
