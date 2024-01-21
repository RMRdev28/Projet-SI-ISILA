Projet: Conception et réalisation d’un système d’information favorisant la gestion de stock commercial d’une entreprise agricole. 

Fonctionnalités Proncipales:

 Notre application permet la gestion de stock pour une entreprise agricole, elle fonctionne comme suit:
 
 On a une Sidebar qui contient des sous-menus, ces derniers contiennent les fonctionnalités de gestion des produits(Ajout/Suppression/modification), des achats, des ventes, des utilisateurs et des centres.
 
 Tel que:
 Lorsque l'utilisateur clique sur "Produits" dans le sidebar, un sous-menu apparaît avec les options de 'consulter la liste des produits' et 'ajouter un nouveau produit'.
 
 Lorsque l'utilisateur clique sur "Achats" dans le sidebar, un sous-menu apparaît avec les options de 'consulter  liste des achats' et 'ajouter un nouveau achats'.
 
 Lorsque l'utilisateur clique sur "Ventes" dans le sidebar, un sous-menu apparaît avec les options de 'consulter la liste des ventes' et 'ajouter un nouvelle vente'.
 
 Lorsque l'utilisateur clique sur "Utilisateurs" dans le sidebar, un sous-menu apparaît avec les options de 'consulter la liste des utilisateurs' et 'ajouter un nouveau utilisateur'.
 
tel que consulter utilisateur permet d afficher la liste des utilisateurs

et ajouter un nouveau utilisateur permet d afficher un formulaire qu'on rempli  pour ajouter un nouveau utilisateur (comme décrit dans l interface d ajout d un utilisateur)

Le fonctionnement de systéme avec github:

1-pour la branche frontend:
 * git init
 * git remote add origin https://github.com/RMRdev28/Si-Project.git
 * git pull origin frontEnd
   
2-pour la branche backend:
 * git init
 * git remote add origin https://github.com/RMRdev28/Si-Project.git](https://github.com/RMRdev28/Si-Project.git
 * git pull origin backEnd

1-pour la branche gestion:
dans le répertoire backend
 *cd gestion
 * git init
 * git remote add origin https://github.com/RMRdev28/Si-Project.git](https://github.com/RMRdev28/Si-Project.git
 * git pull origin gestion


Quelques Captures d'écrans de notre projet

Interface liste des produits
![prod](https://github.com/RMRdev28/Si-Project/assets/148289298/d3b4c7e4-4482-4dbe-8e3f-9a9104c3f93f)

Interface Utilisateurs
![user](https://github.com/RMRdev28/Si-Project/assets/148289298/1b62d61a-ee07-4048-a516-55917774825b)

Interface Achats
![achat](https://github.com/RMRdev28/Si-Project/assets/148289298/e7d34457-669d-4967-a01b-57ed0159ae2c)

Interface d'ajout(exemple d ajout d un utilisateur)
![add](https://github.com/RMRdev28/Si-Project/assets/148289298/ee874ce8-6914-4e28-8ca3-ba5a64a3cd85)

Interface qui affiche notification d'ajout avec succées
![notif](https://github.com/RMRdev28/Si-Project/assets/148289298/39280556-df8f-44b7-a010-7b7ecd8e8ff2)

Interface Dasboard
![418811058_265632046370789_8427276525566251767_n](https://github.com/RMRdev28/Si-Project/assets/148289298/f8ca9e08-f649-4ed0-896f-87fdb791ce95)![420798187_393077979748244_4639267403698799006_n](https://github.com/RMRdev28/Si-Project/assets/148289298/79cb8f81-9e33-4302-831a-888c5252f1cd)
![421124909_1393471457939407_5427309601572955855_n](https://github.com/RMRdev28/Si-Project/assets/148289298/4b5f8459-f765-4f81-b3c9-cad5497d6521)


#Dépendances React

react-bootstrap (v2.9.2) : React Bootstrap est une bibliothèque qui intègre Bootstrap avec React en fournissant des composants React réutilisables basés sur les composants de Bootstrap.

Utilisation : Permet l'utilisation de composants Bootstrap dans des applications React sans avoir à manipuler directement le DOM.


react-dom (v18.2.0) : React DOM est le package spécifique à React qui offre des méthodes pour interagir avec le DOM (Document Object Model). Il est essentiel pour le rendu des composants React dans le DOM.

Utilisation : Il est utilisé pour le rendu des composants React dans le navigateur.


react-router-dom (v6.21.1) : React Router est une bibliothèque de routage pour les applications React. Elle permet la gestion de la navigation entre différentes vues ou pages dans une application React.

Utilisation : Elle est Essentiel pour la mise en place de la navigation et des routes dans une application React.


axios (v1.6.5) : Axios est une bibliothèque HTTP basée sur les promesses qui facilite les requêtes HTTP, que ce soit pour effectuer des requêtes GET, POST,  DELETE,...

Utilisation :Elle permet  d’effectuer des appels API et  de récupérer des données.



#dépendances Django

Django.contrib.admin : Cette application fournit l'interface d'administration Django, une interface web permettant la gestion des modèles de base de données de l'application.

Utilisation : Elle est utile pour effectuer des opérations d'administration, notamment la gestion des utilisateurs, des groupes, des modèles de données,...


django.contrib.auth :Permet de gèrer l'authentification des utilisateurs dans l'application Django. Elle fournit des modèles et des vues pour gérer les comptes utilisateur.

Utilisation : Elle est essentielle pour la gestion des utilisateurs, de l'authentification, et des autorisations.


django.contrib.contenttypes :Elle permet le suivi des types de contenus dans votre application. Elle est utilisée par l'application d'administration pour gérer les relations entre les modèles.

Utilisation : Elle est essentielle pour la gestion des relations entre les modèles.


django.contrib.sessions :Elle gère les sessions utilisateur. Elle permet de stocker et de récupérer des données de session pour chaque utilisateur.

Utilisation : Elle est nécessaire pour gérer les sessions utilisateur dans l'application.


django.contrib.messages :Elle fournit une infrastructure pour stocker et récupérer des messages utilisateur temporaires, tels que des messages de succès ou d'erreur.

Utilisation : Utile pour afficher des messages temporaires aux utilisateurs après certaines actions.


django.contrib.staticfiles :Elle gère la gestion des fichiers statiques tels que les fichiers CSS, JavaScript et les images.

Utilisation : Elle est nécessaire pour la gestion des fichiers statiques dans l'application.


rest_framework :Django Rest Framework est une bibliothèque qui facilite la création d'API Web RESTful pour l'application Django.

Utilisation : Ell est essentielle pour développer une API Web RESTful dans l'application.


corsheaders :Elle permet de gèrer les en-têtes CORS (Cross-Origin Resource Sharing) pour permettre les requêtes depuis des domaines différents.

Utilisation : Elle est utile lorsque l'application doit autoriser les requêtes depuis des domaines différents, souvent Elle est nécessaire lors du développement d'une API utilisée par des applications front-end distinctes.




