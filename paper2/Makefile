extract: clmap main

clmap: paper.tex
	sed -n 54,61p paper.tex > clmap

main: paper.tex
	sed -n 66,226p paper.tex | sed "s/\\\\section/\\\\subsection/" > main

dummy:
	echo DUMMY paper2/clmap > clmap
	echo DUMMY paper2/main > main

clean:
	rm -f clmap
	rm -f main
