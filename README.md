# Get Tweets

Ce code a pour but de récupérer des tweets contenant du contenu potentiellement ofenssant à partir d'une liste de stopwords.

Le code principal est contenu dans le fichier `get_tweets.py`, un compte développeur twitter est nécéssaire pour l'utiliser.

Un output d'un run du fichier est obtenu dans `potential_tweets.csv`.

Quand les tweets obtenus éatient insuffisant, les fichiers `potentiel_tweets_xxx.csv` ont été générés. 

La liste des stopwords est contenue dans `stopwords.csv`
La liste des tweets selectionné comme étant dangereux est incluse dans `selected_tweets.csv`, certains proviennent de [MLMA hate speech](https://github.com/HKUST-KnowComp/MLMA_hate_speech.git).
