# My Blog

## Aperçu du Projet

**My Blog** est une application web dynamique et riche en fonctionnalités, développée avec Django, qui permet de créer et de gérer des articles de blog, des événements, des cours et du contenu multimédia. L'application inclut des fonctionnalités telles que l'authentification des utilisateurs, un système de commentaires, la gestion des médias et le chargement dynamique de contenu avec pagination.

Le projet est structuré autour de plusieurs applications :

- **Elenizado** : Gère les publications, les commentaires, les événements, et plus encore.
- **About** : Fournit des informations sur le site, y compris la gestion des CV et des galeries.
- **Oeuvre** : Présente des poèmes, des vidéos et d'autres contenus multimédias.
- **Website** : Gère les paramètres globaux du site, comme le logo, les informations générales et les liens vers les réseaux sociaux.

## Fonctionnalités

- **Publications et Événements** : Permet aux utilisateurs de consulter, commenter et interagir avec les articles et événements.
- **Galerie et Multimédia** : Affiche des images et des vidéos sous forme de galerie.
- **Cours** : Liste des cours disponibles, avec prise en charge de la pagination.
- **Authentification des Utilisateurs** : Système d'authentification convivial pour commenter et soumettre des formulaires.
- **Intégration des Réseaux Sociaux** : Lien avec les profils sociaux et gestion des abonnements à la newsletter.

## Prérequis

Avant de lancer l'application, assurez-vous d'avoir installé les éléments suivants :

- Python 3.8+
- Django 5.1+
- PostgreSQL ou SQLite
- `pip` (pour installer les dépendances)

### Dépendances

Pour installer les dépendances nécessaires, exécutez la commande suivante :

```bash
pip install -r requirements.txt
```

## Installation

1. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

2. Appliquez les migrations :

   ```bash
   python manage.py migrate
   ```

3. Créez un superutilisateur (optionnel mais recommandé pour l'accès à l'administration) :

   ```bash
   python manage.py createsuperuser
   ```

4. Lancez le serveur :

   ```bash
   python manage.py runserver
   ```

5. Ouvrez votre navigateur et visitez `http://127.0.0.1:8000/` pour voir l'application.

## Utilisation

- **Panneau d'administration** : Accédez à `http://127.0.0.1:8000/admin/` avec les identifiants du superutilisateur.
- **Consulter le contenu** : Naviguez sur le blog pour voir les articles, événements, cours et contenus multimédias.
- **Ajouter/Modifier du contenu** : En tant qu'admin, créez, modifiez ou supprimez des publications, événements, cours, etc., depuis le panneau d'administration.

## Tests

Pour exécuter les tests de l'application, utilisez la commande suivante :

```bash
python manage.py test
```

## Vérification du Code

Ce projet utilise **flake8** pour l'analyse de la qualité du code Python. Pour lancer flake8, exécutez :

```bash
flake8 .
```

Si vous souhaitez ignorer certains avertissements, vous pouvez modifier le fichier de configuration `.flake8`.

## Contribution

Si vous souhaitez contribuer, vous pouvez forker le dépôt, créer une branche et soumettre une pull request avec vos modifications. Veillez à respecter les standards de codage et à écrire des tests pour les nouvelles fonctionnalités ou corrections de bogues.
