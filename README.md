
<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h2 >verification_gvd</h3>
   <a href="https://github.com/ReseauOGF/verification_gvd/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#objectif">Objectif</a>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>


## Objectif
Avoir un fichier regroupement les différences entre un import et un export GVD

## Getting Started
### prerequisites
- python3 .
- Extraction GVD format '.csv'
- Fichier a comparer format '.csv'

### installation
1. Clone the repo
> git clone https://github.com/ReseauOGF/verification_gvd.git

## usage

- Placer l'extraction GVD dans le dossier ./projet/data/input
  - Renommer le ficher en : export.csv
- Placer le fichier a comparer dans le dossier ./projet/data/input
  - Renommer le ficher en : import.csv
- Activer l'environement virtuel
> env\Scripts\activate
- Lancement du script
> py .\projet\script\verification_gvd.py

### résultats

Le fichier "result.xlsx" regroupe les différences entres les fichiers GVD import et export.
Les informations affichiées sont celles du fichier import.