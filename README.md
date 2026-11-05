# Devlish Claude Kit 😈

Un petit kit pour que Claude Code travaille proprement dès la première minute.
Par [Devlish](https://www.instagram.com/devlish_team/), une équipe de jeunes devs.

## Ce que vous obtenez

| Fichier | Rôle |
|---|---|
| `CLAUDE.md` | Les règles de votre projet, à compléter |
| `/review` | Cherche les vrais bugs avant un commit |
| `/commit` | Écrit des commits propres |
| `/bug-hunt` | Trouve la cause d'un bug, étape par étape |
| `/tests` | Écrit des tests utiles |
| Protection `.env` | Empêche Claude de lire vos secrets |

## Installation

Il faut [Claude Code](https://claude.com/claude-code), Git et Python 3.

```bash
git clone https://github.com/Mohamed-EDDAHMANI/devlish-claude-kit.git
cd devlish-claude-kit
./install.sh /chemin/vers/votre/projet
```

Le script n'écrase aucun fichier existant. Ensuite :

1. Complétez `CLAUDE.md` dans votre projet.
2. Lancez `claude` dans le dossier du projet.
3. Essayez `/review`.

## La protection `.env`

Elle bloque les outils de Claude quand ils visent un fichier `.env`. Les fichiers comme `.env.example` restent accessibles.

C'est un filet de sécurité, pas une garantie : un script peut toujours lire ce fichier. Gardez vos secrets hors de Git.

## Pour aller plus loin

- [obra/superpowers](https://github.com/obra/superpowers) : une méthode complète de travail pour les agents.
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) : une grande liste de ressources.

Ces projets appartiennent à leurs auteurs. Ils ne font pas partie de ce kit.

## Licence

[MIT](LICENSE). Une idée ou un bug ? Ouvrez une issue.
