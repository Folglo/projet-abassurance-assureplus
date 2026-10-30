# Contribuer au projet

Ce document définit la convention de nommage des branches et les règles de travail.
Il s'appuie sur les bonnes pratiques Git et GitHub vues en formation.

## Branches principales
| Branche | Rôle | Règle |
|---|---|---|
| `main` | version stable, mise en production | contient uniquement du code testé et validé |
| `develop` | développement principal (appelée « dev » dans le cours) | reçoit les fonctionnalités terminées |

## Branches de travail
| Type | Créée depuis | Fusionnée dans | Usage | Exemple |
|---|---|---|---|---|
| `feature/` | `develop` | `develop` | nouvelle fonctionnalité | `feature/us-1-2-duplicate-matrix` |
| `bugfix/` | `develop` | `develop` | correction d'un bug non urgent | `bugfix/birth-date-format` |
| `release/` | `develop` | `main`, puis `develop` | préparation d'une version | `release/1.0.0` |
| `hotfix/` | `main` | `main` et `develop` | correction rapide d'un bug critique | `hotfix/total-clients-count` |

`bugfix/` est un ajout de l'équipe pour les bugs non urgents. Les autres types viennent du cours.

## Règles de nommage
- Format : `type/us-X-Y-short-description` ; `us-X-Y` renvoie à la User Story du tableau Trello.
- Noms explicites, en anglais, en minuscules, séparés par des tirets, sans accents ni espaces.
- Jamais de noms génériques comme `feature1` ou `test`.

## Commits
- Un commit = un seul changement (commit atomique).
- Message clair et concis, en anglais : `type: short description`.
- Types : `feat`, `fix`, `test`, `docs`, `refactor`.
- Exemple : `feat: add duplicate detection on customers`
- On évite les commits inutiles (espaces, renommages seuls) et les commits volumineux.

## Avant de fusionner
1. Les tests unitaires passent (`python -m pytest`) et Ruff ne signale rien (`ruff check .`).
2. Une pull request est ouverte vers `develop`, avec une description et un relecteur.
3. Elle est liée à son issue (`#numéro`).
4. `develop` n'est fusionnée dans `main` que lorsque la version est testée et validée.

## Issues
- Une issue par tâche ou par branche, avec un titre court et une description détaillée.
- Labels : `bug`, `feature`, `documentation`.
- Une personne assignée et, si besoin, un jalon (milestone).
