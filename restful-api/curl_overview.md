# Découverte de `curl`

## Introduction

`curl` (**Client URL**) est un outil en ligne de commande permettant de transférer des données entre un client et un serveur. Il prend en charge de nombreux protocoles, notamment :

* HTTP
* HTTPS
* FTP
* SMTP
* LDAP

Il est couramment utilisé pour :

* Tester des API REST.
* Déboguer des requêtes HTTP.
* Inspecter les réponses d'un serveur.
* Automatiser des échanges de données.

---

# Vérification de l'installation

Une fois `curl` installé, il est possible de vérifier son installation avec :

```bash
curl --version
```

### Résultat attendu

Cette commande affiche :

* La version de curl installée.
* Les protocoles pris en charge.
* Les fonctionnalités disponibles.

Exemple :

```text
curl 8.x.x
Protocols: dict file ftp ftps http https ...
Features: SSL IPv6 HSTS ...
```

---

# Récupérer le contenu d'une page web

La commande suivante permet de télécharger le contenu HTML d'une page :

```bash
curl http://example.com
```

### Résultat attendu

Le terminal affiche le code HTML de la page.

Exemple :

```html
<!doctype html>
<html>
<head>
<title>Example Domain</title>
...
</head>
</html>
```

---

# Récupérer des données depuis une API

Le site JSONPlaceholder fournit une API publique destinée aux tests.

Pour récupérer tous les articles :

```bash
curl https://jsonplaceholder.typicode.com/posts
```

### Résultat attendu

La réponse est un tableau JSON contenant plusieurs objets :

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "...",
    "body": "..."
  },
  {
    "userId": 1,
    "id": 2,
    "title": "...",
    "body": "..."
  }
]
```

Chaque article possède :

* `userId` : identifiant de l'utilisateur.
* `id` : identifiant de l'article.
* `title` : titre de l'article.
* `body` : contenu de l'article.

---

# Afficher uniquement les en-têtes HTTP

L'option `-I` permet d'obtenir uniquement les en-têtes de la réponse :

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

### Résultat attendu

```text
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: ...
Date: ...
Cache-Control: ...
```

### Utilité

Cette commande permet de :

* Vérifier le code de statut HTTP.
* Connaître le type de contenu renvoyé.
* Observer les informations de cache.
* Diagnostiquer certains problèmes réseau.

---

# Effectuer une requête POST

L'option `-X` permet de spécifier la méthode HTTP utilisée.

L'option `-d` permet d'envoyer des données au serveur.

Exemple :

```bash
curl -X POST \
-d "title=foo&body=bar&userId=1" \
https://jsonplaceholder.typicode.com/posts
```

### Résultat attendu

```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

L'API JSONPlaceholder ne sauvegarde pas réellement les données ; elle simule simplement la création d'une nouvelle ressource et renvoie un identifiant (`id`) égal à `101`.

---

# Principales options de curl

| Option      | Description                                          |
| ----------- | ---------------------------------------------------- |
| `-I`        | Affiche uniquement les en-têtes HTTP                 |
| `-X`        | Spécifie la méthode HTTP (GET, POST, PUT, DELETE...) |
| `-d`        | Envoie des données dans la requête                   |
| `--version` | Affiche les informations sur curl                    |
| `-H`        | Ajoute un en-tête personnalisé                       |

Exemple :

```bash
curl -H "Content-Type: application/json" URL
```

---

# Formater le JSON avec jq

Les réponses JSON peuvent être difficiles à lire. Il est possible de les formater avec l'outil `jq` :

```bash
curl https://jsonplaceholder.typicode.com/posts | jq
```

### Résultat attendu

Le JSON est affiché de manière plus lisible, avec une indentation et une coloration syntaxique.

---

# Conclusion

`curl` est un outil essentiel pour interagir avec les API et tester les communications HTTP.

Il permet notamment :

* De récupérer des ressources avec une requête GET.
* D'envoyer des données avec une requête POST.
* D'inspecter les en-têtes HTTP.
* De déboguer des serveurs et des API.
* D'automatiser des échanges réseau directement depuis le terminal.
