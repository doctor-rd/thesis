extract: coll main cnt1 cnt2

coll: paper.tex
	sed -n 57,87p paper.tex > coll

main: paper.tex
	sed -n 89,136p paper.tex > main

cnt1: paper.tex
	sed -n 139,143p paper.tex > cnt1

cnt2: paper.tex
	sed -n 145,148p paper.tex > cnt2

dummy:
	echo DUMMY paper1/coll > coll
	echo DUMMY paper1/main > main
	echo DUMMY paper1/cnt1 > cnt1
	echo DUMMY paper1/cnt2 > cnt2

clean:
	rm -f coll
	rm -f main
	rm -f cnt1
	rm -f cnt2
