# Scripts de tracé

Chaque script régénère une figure du recueil et l'écrit directement dans `figures/`
sous le nom correspondant. Les scripts sont indépendants les uns des autres.

## Environnement

Les dépendances (matplotlib, numpy) sont installées dans le venv du dossier de travail,
`/Users/matthieu/Colles/.venv`. Depuis ce dossier-ci :

    ../../../.venv/bin/python electronique_dephaseur_2.py

Pour recréer le venv depuis zéro :

    python3 -m venv /Users/matthieu/Colles/.venv
    /Users/matthieu/Colles/.venv/bin/pip install -r requirements.txt

## Convention

Le nom du script reprend celui de la figure produite, lui-même construit sur
`<thème>_<exercice>_<numéro>`. L'en-tête de chaque script rappelle à quel exercice
et à quelle question la figure se rattache, ainsi que les formules tracées.
