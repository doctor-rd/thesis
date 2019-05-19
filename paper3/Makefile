extract: patchwork main1 quotmatching main2 main3

patchwork: equivariant.tex
	sed -n 53,56p equivariant.tex > patchwork

main1: equivariant.tex
	sed -n 67,89p equivariant.tex > main1

quotmatching: equivariant.tex
	sed -n 90,93p equivariant.tex > quotmatching

main2: equivariant.tex
	sed -n 99,142p equivariant.tex > main2

main3: equivariant.tex
	sed -n 144,247p equivariant.tex | sed "s/\\\\section/\\\\subsection/" > main3

dummy:
	echo DUMMY paper3/patchwork > patchwork
	echo DUMMY paper3/main1 > main1
	echo DUMMY paper3/quotmatching > quotmatching
	echo DUMMY paper3/main2 > main2
	echo DUMMY paper3/main3 > main3

clean:
	rm -f patchwork
	rm -f main1
	rm -f quotmatching
	rm -f main2
	rm -f main3
