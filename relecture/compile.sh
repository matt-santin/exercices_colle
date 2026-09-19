#!/bin/bash
cd "$(dirname "$0")"
mkdir -p build
pdflatex -interaction=nonstopmode -output-directory=build relecture.tex >/dev/null
pdflatex -interaction=nonstopmode -output-directory=build relecture.tex >/dev/null
cp build/relecture.pdf relecture.pdf
echo "relecture.pdf"
