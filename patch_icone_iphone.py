from pathlib import Path

fichier = Path("index.html")

texte = fichier.read_text(encoding="utf-8")

ancien = """  <link
    rel="apple-touch-icon"
    href="./apple-touch-icon.png"
  >"""

nouveau = """  <link
    rel="apple-touch-icon"
    sizes="180x180"
    href="/cis-sermaize-pwa/apple-touch-icon.png"
  >"""

if ancien not in texte:
    print("ERREUR - Bloc apple-touch-icon introuvable.")
    raise SystemExit(1)

if texte.count(ancien) != 1:
    print(
        "ERREUR - Nombre de blocs trouves :",
        texte.count(ancien)
    )
    raise SystemExit(1)

sauvegarde = Path(
    "index_AVANT_CORRECTION_ICONE_IPHONE.html"
)

sauvegarde.write_text(
    texte,
    encoding="utf-8"
)

texte = texte.replace(
    ancien,
    nouveau,
    1
)

fichier.write_text(
    texte,
    encoding="utf-8"
)

print("OK - ICONE IPHONE CORRIGEE")
print("Taille declaree : 180x180")
print("Chemin : /cis-sermaize-pwa/apple-touch-icon.png")