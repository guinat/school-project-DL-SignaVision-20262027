# Build the report in build/ and copy the PDF next to this Makefile
all:
	latexmk -pdf -interaction=nonstopmode -outdir=build main.tex
	cp build/main.pdf report.pdf

clean:
	latexmk -C -outdir=build
	rm -rf build
