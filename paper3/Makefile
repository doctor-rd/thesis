extract: main1 main2 main3

main1: equivariant.tex
	sed -n 67,89p equivariant.tex > main1

main2: equivariant.tex
	sed -n 105,141p equivariant.tex > main2

main3: equivariant.tex
	sed -n 143,246p equivariant.tex | sed "s/\\\\section/\\\\subsection/" > main3

clean:
	rm -f main1
	rm -f main2
	rm -f main3
