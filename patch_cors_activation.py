from pathlib import Path

fichier = Path("index.html")

texte = fichier.read_text(encoding="utf-8")

ancien = """fetch('https://script.google.com/macros/s/AKfycbzClJ-siED0JMrCguhbt8VZs-zuBIQb19f_KeYSwee-bWweA8BAI47d92W5eLGZ96dvkA/exec', {
  method: 'POST',
  body: JSON.stringify({
    action: 'enregistrerNotification',
"""

nouveau = """fetch('https://script.google.com/macros/s/AKfycbzClJ-siED0JMrCguhbt8VZs-zuBIQb19f_KeYSwee-bWweA8BAI47d92W5eLGZ96dvkA/exec', {
  method: 'POST',
  mode: 'no-cors',
  body: JSON.stringify({
    action: 'enregistrerNotification',
"""

if ancien not in texte:
    print("ERREUR - Bloc activation introuvable.")
    raise SystemExit(1)

if texte.count(ancien) != 1:
    print(
        "ERREUR - Plusieurs blocs correspondants trouves :",
        texte.count(ancien)
    )
    raise SystemExit(1)

sauvegarde = Path(
    "index_AVANT_CORRECTION_CORS_ACTIVATION.html"
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

print("OK - CORRECTION CORS ACTIVATION APPLIQUEE")
print("Sauvegarde :", sauvegarde)