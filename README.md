# Patrimoine Clair

Suivez votre patrimoine en un coup d'œil, **sans connecter vos comptes bancaires** et sans créer de compte.

## Pourquoi cet outil

- **Aucune connexion bancaire.** Vous saisissez vos lignes vous-même.
- **Vos données restent chez vous.** Elles sont stockées dans votre navigateur, rien n'est envoyé à un serveur. Une politique de sécurité (CSP) bloque les connexions sortantes de la page, hormis la lecture des cours publiés sur le même site.
- **Protection par mot de passe.** Chiffrement AES-GCM des données stockées, et export chiffré `.enc`.
- **Un outil léger.** Pas d'abonnement, pas de publicité.

## Ce qu'il fait

- **Total du patrimoine**, capital versé, plus-value et revenu annuel estimé
- **Classement par enveloppe** : PEA, PEA-PME, assurance vie, CTO, PER, Livret A, LDDS, LEP, compte courant, crypto, immobilier, avec total et part de chacune
- **Fusion automatique des lignes** : un nouvel achat sur un actif existant s'ajoute à la ligne, avec un prix de revient moyen recalculé
- **Cible par ligne** (en % de l'enveloppe) et montant approximatif à ajouter pour l'atteindre
- **Rendement estimé par ligne** et rendement sur coût (YoC)
- **Historique des versements** pour distinguer le capital versé de la plus-value
- **Évolution dans le temps** : un instantané par mois, courbe du patrimoine et courbe en pointillés du capital versé
- **Recherche et filtre** par enveloppe
- **Bouton œil** : floute les montants pour partager une capture d'écran
- **Thème clair / sombre** manuel
- **Installable sur téléphone** (PWA) et utilisable hors-ligne
- **Cours automatiques** chaque soir de semaine (voir plus bas)

## Utilisation

1. Ajoutez une ligne : nom, code, enveloppe, quantité, prix de revient, cours.
2. Pour un livret ou un compte, indiquez simplement le solde dans « Quantité ».
3. Saisissez vos versements pour suivre le capital versé.
4. Cliquez sur « Enregistrer un instantané » une fois par mois pour alimenter la courbe.
5. Activez le mot de passe dans « Protection des données » si vous le souhaitez.
6. **Exportez régulièrement vos données** : vider les données du navigateur les efface.

## Sécurité et confidentialité

- Sans mot de passe, les données sont stockées en clair dans le navigateur (IndexedDB).
- Avec mot de passe, elles sont chiffrées (clé dérivée par PBKDF2, puis AES-GCM). **Un mot de passe perdu ne peut pas être récupéré** : gardez un export.
- Le chiffrement protège contre la lecture des données stockées. Il ne protège pas un appareil déjà compromis, car les données sont lisibles en mémoire une fois déverrouillé.
- L'export chiffré (`.enc`) utilise un mot de passe propre au fichier.

## Installer sur téléphone

- **iPhone / iPad (Safari)** : Partager → Sur l'écran d'accueil
- **Android (Chrome)** : menu ⋮ → Installer l'application

L'application installée peut avoir un stockage séparé de celui du navigateur : transférez vos données par export / import.

## Installer votre propre copie

1. Créez un dépôt public sur GitHub et envoyez-y : `index.html`, `manifest.json`, `sw.js`, `icon-192.png`, `icon-512.png`, `apple-touch-icon.png`, `update_prices.py`, `tickers.json`, `prices.json`, `LICENSE`, `README.md`.
2. Créez le fichier `.github/workflows/prices.yml` (contenu fourni avec l'outil).
3. **Settings → Pages** : branche `main`, dossier `/ (root)`.
4. **Settings → Actions → General → Workflow permissions** : *Read and write permissions*.
5. Dans `tickers.json`, associez chaque code utilisé dans l'outil à son symbole Yahoo Finance :

   ```json
   {
     "TTE": "TTE.PA",
     "WPEA": "WPEA.PA"
   }
   ```

   Vérifiez chaque symbole sur finance.yahoo.com (par ISIN) et que le prix est en euros.
6. Onglet **Actions → Mise à jour des cours → Run workflow** pour un premier test.
7. Optionnel : renseignez `NEWSLETTER_URL` en haut du script de `index.html` pour activer l'inscription par e-mail.

## Limites à connaître

- Les cours viennent de l'API non officielle de Yahoo Finance : elle peut changer ou se bloquer sans préavis. L'outil reste utilisable en saisie manuelle.
- Les cours sont mis à jour après la clôture, pas en temps réel.
- Le capital investi affiché sans versements saisis est estimé à partir des prix de revient. Avec des versements, c'est leur somme qui est utilisée.
- La courbe d'évolution ne mesure pas une performance : elle suit le montant du patrimoine, versements compris.
- Les montants « à ajouter » pour atteindre une cible sont des ordres de grandeur, calculés sur la valeur actuelle de l'enveloppe.
- Les données sont locales à chaque navigateur et à chaque appareil : utilisez l'export et l'import pour les transférer.
- L'outil n'a pas de synchronisation bancaire, de cours en temps réel ni d'application sur les stores.

## Licence

Ce projet est distribué sous licence [PolyForm Noncommercial 1.0.0](LICENSE).

- **Autorisé :** utiliser l'outil pour gérer votre propre patrimoine, l'étudier, le modifier et le partager à des fins non commerciales.
- **Non autorisé sans accord de l'auteur :** le revendre, l'intégrer à un produit ou un service payant, ou en tirer un revenu.

Pour un usage commercial, contactez l'auteur.

## Avertissement

Cet outil est un support de suivi à but informatif. Il ne constitue pas un conseil en investissement. Les performances passées ne préjugent pas des performances futures.
