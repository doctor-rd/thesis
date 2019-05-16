extract: coll main

coll: paper.tex
	sed -n 57,87p paper.tex > coll

main: paper.tex
	sed -n 89,136p paper.tex > main

dummy:
	echo DUMMY paper1/coll > coll
	echo DUMMY paper1/main > main

clean:
	rm -f coll
	rm -f main
