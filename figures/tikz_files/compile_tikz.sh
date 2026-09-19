#!/bin/bash
# Compile un schema TikZ autonome et le recadre sur son contenu.
# Usage : ./compile_tikz.sh magnetostatique1_1
# Le PDF recadre est ecrit dans ../ sous le meme nom.
set -e
nom="${1%.tex}"
tmp=$(mktemp -d)
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$tmp" "$nom.tex" >/dev/null
bbox=$(gs -q -dBATCH -dNOPAUSE -sDEVICE=bbox "$tmp/$nom.pdf" 2>&1 | grep "^%%BoundingBox" | head -1)
read -r _ x0 y0 x1 y1 <<< "$bbox"
m=2
w=$(( x1 - x0 + 2*m )); h=$(( y1 - y0 + 2*m ))
gs -q -o "../$nom.pdf" -sDEVICE=pdfwrite -dDEVICEWIDTHPOINTS=$w -dDEVICEHEIGHTPOINTS=$h -dFIXEDMEDIA \
   -c "<</PageOffset [$(( m - x0 )) $(( m - y0 ))]>> setpagedevice" -f "$tmp/$nom.pdf"
rm -rf "$tmp"
echo "../$nom.pdf  (${w}x${h} pt)"
