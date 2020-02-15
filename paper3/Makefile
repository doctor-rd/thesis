extract: patchwork main1 quotmatching main2 main3

patchwork: equivariant.tex
	sed -n 53,56p equivariant.tex > patchwork

main1: equivariant.tex
	sed -n 67,89p equivariant.tex > main1

quotmatching: equivariant.tex quotmatching.patch
	sed -n 90,93p equivariant.tex > quotmatching
	patch quotmatching quotmatching.patch

main2: equivariant.tex
	sed -n 99,142p equivariant.tex > main2

main3: equivariant.tex main3.patch
	sed -n 144,248p equivariant.tex > main3
	patch main3 main3.patch

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
