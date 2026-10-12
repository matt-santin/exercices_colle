import pymupdf
src = "annales/Mines-Ponts/2015/Mines_PSI_2015_Physique-2.pdf"
out = "exercices_colle/figures/thermo_compression_etagee.pdf"
orig = pymupdf.open(src)          # copie intacte, pour reprendre la lettre D et une flèche
doc = pymupdf.open(src)
doc.select([1])
p = doc[0]
# Mélangeur (M), légendes Dm et D', flèche D', trait vertical
p.add_redact_annot(pymupdf.Rect(80, 55, 125, 135))
p.apply_redactions(images=0, graphics=2, text=0)
# Flèche et légende D de sortie : on ne retire que ce qui est entièrement dans la zone
p.add_redact_annot(pymupdf.Rect(486, 100, 506, 135))
p.apply_redactions(images=0, graphics=1, text=0)
# Descente verticale de sortie (même tracé que le reste du circuit) : masquée
p.draw_rect(pymupdf.Rect(503, 87.5, 520, 135), color=None, fill=(1, 1, 1))
w = 1.9925
p.draw_line((100, 87.13), (141.73, 87.13), width=w)    # entrée
p.draw_line((501.7, 87.13), (530, 87.13), width=w)     # sortie horizontale
fleche = pymupdf.Rect(84.5, 76.3, 99.7, 80.8)           # flèche de Dm dans l'original
lettre = pymupdf.Rect(486.5, 108, 497, 121)             # lettre D dans l'original
for x in (106, 513):                                     # entrée, sortie
    p.show_pdf_page(pymupdf.Rect(x, 76.3, x + fleche.width, 80.8), orig, 1, clip=fleche)
    xc = x + fleche.width / 2 - lettre.width / 2
    p.show_pdf_page(pymupdf.Rect(xc, 64, xc + lettre.width, 64 + lettre.height), orig, 1, clip=lettre)
clip = pymupdf.Rect(95, 54, 532, 133)
res = pymupdf.open()
res.new_page(width=clip.width, height=clip.height).show_pdf_page(
    pymupdf.Rect(0, 0, clip.width, clip.height), doc, 0, clip=clip)
res.save(out, garbage=4, deflate=True)
