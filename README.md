# translation-game
A simple word game I developed as a project for university. In a nutshell, the game allows the player to practice vocabulary in a language of choice. 

First, the game asks for four things:
- a txt file, from where it will extract the words
- the language we want to practice
- the grammatical category of the words we want to practice (verbs, adjectives, nouns, adverbs)
- the number of rounds we want to play

Next, the game itself will begin. In each round the player will be asked to translate a word from English into the language of choice. The game will also provide context, aka the sentence from the source text where the word appears. Each correct answer will be rewarded with a point. If the player guesses wrong, they will have a second chance, and the game will provide a hint: the definition of the word. At the end of all rounds, an encouraging message will be displayed according to the percentage of correct answers.

## Requirements:
- Python 3
- The NLTK package "wordnet"
- The NLTK package "wsd" (Word Sense Disambiguation) and, within it, the Lesk algorithm
- The NLTK package "tokenize" and, within it, the function "sent_tokenize"
- Random
