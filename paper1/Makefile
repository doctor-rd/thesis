extract: coll main count

coll: paper.tex coll.patch
	sed -n 54,87p paper.tex > coll
	patch coll coll.patch

main: paper.tex
	sed -n 89,136p paper.tex > main

count: paper.tex count.patch
	sed -n 139,148p paper.tex > count
	patch count count.patch

dummy:
	echo DUMMY paper1/coll > coll
	echo DUMMY paper1/main > main
	echo DUMMY paper1/count > count

clean:
	rm -f coll
	rm -f main
	rm -f count
