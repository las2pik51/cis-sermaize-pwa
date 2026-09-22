from pathlib import Path
import shutil

fichier = Path("index.html")
sauvegarde = Path(
    "index_AVANT_CORRECTION_CORS.html"
)

if not fichier.exists():
    raise SystemExit(
        "ERREUR - index.html introuvable"
    )

contenu = fichier.read_text(
    encoding="utf-8"
)

debut = """            fetch(
              'https://script.google.com/macros/s/AKfycbzClJ-siED0JMrCguhbt8VZs-zuBIQb19f_KeYSwee-bWweA8BAI47d92W5eLGZ96dvkA/exec',
              {
                method: 'POST',
                body: JSON.stringify({
                  action:
                    'desactiverNotification',
                  token: token
                })
              }
            )
            .then(function(reponse) {
              return reponse.json();
            })
            .then(function(resultat) {

              if (
                resultat &&
                resultat.success
              ) {

                etat.innerHTML =
                  'Notifications desactivees.<br><br>' +
                  '<button id="ouvrirCIS">' +
                  'Ouvrir CIS SERMAIZE Connect' +
                  '</button>';

                document
                  .getElementById(
                    'ouvrirCIS'
                  )
                  .addEventListener(
                    'click',
                    function() {

                      window.location.href =
                        'https://script.google.com/macros/s/AKfycbzClJ-siED0JMrCguhbt8VZs-zuBIQb19f_KeYSwee-bWweA8BAI47d92W5eLGZ96dvkA/exec';
                    }
                  );

              } else {

                etat.textContent =
                  resultat &&
                  resultat.message
                    ? resultat.message
                    : 'Impossible de desactiver.';
              }
            })
            .catch(function(erreur) {

              console.error(
                'Erreur desactivation:',
                erreur
              );

              etat.textContent =
                'Erreur pendant desactivation.';
            });"""

nouveau = """            fetch(
              'https://script.google.com/macros/s/AKfycbzClJ-siED0JMrCguhbt8VZs-zuBIQb19f_KeYSwee-bWweA8BAI47d92W5eLGZ96dvkA/exec',
              {
                method: 'POST',
                mode: 'no-cors',
                body: JSON.stringify({
                  action:
                    'desactiverNotification',
                  token: token
                })
              }
            )
            .then(function() {

              etat.innerHTML =
                'Demande de desactivation envoyee.<br><br>' +
                '<button id="ouvrirCIS">' +
                'Ouvrir CIS SERMAIZE Connect' +
                '</button>';

              document
                .getElementById(
                  'ouvrirCIS'
                )
                .addEventListener(
                  'click',
                  function() {

                    window.location.href =
                      'https://script.google.com/macros/s/AKfycbzClJ-siED0JMrCguhbt8VZs-zuBIQb19f_KeYSwee-bWweA8BAI47d92W5eLGZ96dvkA/exec';
                  }
                );
            })
            .catch(function(erreur) {

              console.error(
                'Erreur envoi desactivation:',
                erreur
              );

              etat.textContent =
                'Erreur pendant envoi.';
            });"""

nombre = contenu.count(debut)

if nombre != 1:
    raise SystemExit(
        f"ERREUR - bloc CORS trouve "
        f"{nombre} fois. "
        "Aucune modification effectuee."
    )

shutil.copy2(
    fichier,
    sauvegarde
)

contenu = contenu.replace(
    debut,
    nouveau,
    1
)

fichier.write_text(
    contenu,
    encoding="utf-8"
)

print(
    "OK - CORRECTION CORS APPLIQUEE"
)
print(
    "Sauvegarde :",
    sauvegarde
)