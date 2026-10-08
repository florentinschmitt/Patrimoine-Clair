# Patrimoine-Clair
Votre patrimoine en un coup d'œil. Aucune connexion bancaire.
# Patrimoine Clair

Suivez votre patrimoine en un coup d'œil, **sans connecter vos comptes bancaires**.

## Pourquoi cet outil

- **Aucune connexion bancaire.** Vous saisissez vos lignes vous-même.
- **Vos données restent chez vous.** Elles sont stockées dans votre navigateur, rien n'est envoyé à un serveur.
- **Un seul fichier.** Pas de compte à créer, pas d'abonnement.

## Ce qu'il fait

- Total du patrimoine et écart par rapport au prix de revient
- **Classement par enveloppe** : PEA, PEA-PME, assurance vie, CTO, PER, Livret A, LDDS, LEP, compte courant, crypto, immobilier
- Total et part de chaque enveloppe, en haut de page
- Répartition en barre, par ligne ou par enveloppe
- **Cible par ligne** (en % de l'enveloppe) et montant approximatif à ajouter pour l'atteindre
- **Évolution dans le temps** : un instantané par mois, courbe avec dates et montants
- Cours mis à jour automatiquement chaque soir de semaine (voir plus bas)
- Export et import de vos données, avec rappel si la dernière sauvegarde date

## Utilisation

1. Ajoutez une ligne : nom, code, enveloppe, quantité, prix de revient, cours.
2. Pour un livret ou un compte, indiquez simplement le solde dans « Quantité ».
3. Cliquez sur « Enregistrer un instantané » une fois par mois pour alimenter la courbe.
4. **Exportez régulièrement vos données** : vider le cache du navigateur les efface.

## Installer votre propre copie

1. Créez un dépôt public sur GitHub et envoyez-y `index.html`, `update_prices.py`, `tickers.json` et `prices.json`.
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
- La courbe d'évolution inclut vos versements : elle ne mesure pas une performance.
- Les montants « à ajouter » pour atteindre une cible sont des ordres de grandeur, calculés sur la valeur actuelle de l'enveloppe.
- Vos données étant locales à chaque navigateur, un autre appareil repart de zéro : utilisez l'export et l'import pour les transférer.

## Licence

Ce projet est distribué sous licence [PolyForm Noncommercial 1.0.0](LICENSE).

- **Autorisé :** utiliser l'outil pour gérer votre propre patrimoine, l'étudier, le modifier et le partager à des fins non commerciales.
- **Non autorisé sans accord de l'auteur :** le revendre, l'intégrer à un produit ou un service payant, ou en tirer un revenu.

Pour un usage commercial, contactez l'auteur.

## Avertissement

Cet outil est un support de suivi à but informatif. Il ne constitue pas un conseil en investissement. Les performances passées ne préjugent pas des performances futures.
