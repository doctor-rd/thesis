extract: clmap main

clmap: paper.tex
	sed -n 54,61p paper.tex > clmap

main: paper.tex main.patch
	sed -n 66,229p paper.tex > main
	patch main main.patch

dummy:
	echo DUMMY paper2/clmap > clmap
	echo DUMMY paper2/main > main

clean:
	rm -f clmap
	rm -f main
