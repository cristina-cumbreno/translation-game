import nltk
from nltk.corpus import wordnet as wn
import random
from nltk.wsd import lesk
from nltk.tokenize import sent_tokenize

print('Welcome to the word game!\n')

file = open(input('Please write the file name containing the text: '),'r')
raw_text = file.read()
file.close()

language = (input("""
***Choose the language you want to practice.*** 

Available choices: 
Albanian: als
Arabic: arb
Catalan: cat
Chinese: cmn
Danish: dan
English: eng
Basque: eus
Farsi: fas
Finnish: fin
French: fra
Galician: glg
Hebrew: heb
Indonesian: ind
Italian: ita
Japanese: jpn
Esperanto: nno
Norwegian: nob
Polish: pol
Portuguese: por
Spanish: spa
Thailandese: tha
Malaysian: zsm

Your choice: """)).lower()

word_type = (input("""
*** Choose the type of words you want to practice. ***
Available choices:
Nouns: n 
Verbs: v
Adjectives: j
Adverbs: r

Your choice: """)).upper()


sentences = sent_tokenize(raw_text)

def get_wordnet_pos(tag):
    if tag == ('J'):
        return wn.ADJ
    elif tag == ('V'):
        return wn.VERB
    elif tag == ('N'):
        return wn.NOUN
    elif tag == ('R'):
        return wn.ADV

wn_word_type = get_wordnet_pos(word_type)

def cleantext(text):
# Cleans the text from punctuation    
    text = "".join(text.split("\n"))
    text = "".join(text.split("."))
    text = "".join(text.split(","))
    text = "".join(text.split(":"))
    text = "".join(text.split(";"))
    text = "".join(text.split("("))
    text = " ".join(text.split("-"))
    text = "".join(text.split(")"))
    text = "".join(text.split("\""))
    text = "".join(text.split("\'"))
    text = "".join(text.split("!"))
    text = "".join(text.split("?"))
    text = text.lower()
    return text

dictionary = {}
   
for sent in sentences:
    clean_sent = cleantext(sent)
    if len(clean_sent) <2:
            continue
    else:
        tokenized = nltk.word_tokenize(clean_sent)
        tagged = nltk.pos_tag(tokenized)
        for element in tagged:
            if element[1].startswith(word_type) and len(element[0]) > 2 and lesk(sent, element[0], wn_word_type): 
                dictionary[element[0]] = [sent, lesk(sent, element[0], wn_word_type)]

wnl = nltk.WordNetLemmatizer()

for word in dictionary:
    dictionary[word].append(wnl.lemmatize(word, wn_word_type))

def extract_answers(word):
    answers = []
    synset = dictionary[word][1]
    trans_words = synset.lemma_names(language)
    if trans_words != []:
        for trans_word in trans_words: 
            trans_word = " ".join(trans_word.split("_"))
            answers.append(trans_word)
    return answers

game_dictionary = {}
game_words = []

for word in dictionary:
    lemma = dictionary[word][2]
    context = dictionary[word][0]
    definition = dictionary[word][1].definition()
    if extract_answers(word) != []:
        game_dictionary[lemma] = [extract_answers(word)],[context],[definition]
        game_words.append(lemma)
        
random.shuffle(game_words)

points = 0

limit = int(input("""
How many words do you want to practice? {} words available. """
.format(len(game_words))))

for word in game_words[0:limit]:
    print("""
    *** What is the translation for {0} ? ***
    
        The word in context: {1}
    """.format(word, game_dictionary[word][1][0]))
   
    first_response = input(""" >>>>> Your translation: """)

    if first_response in game_dictionary[word][0][0]:
        points += 1
        print("""
    Great!
    
    Points: {}
        """.format(points))
    
    else:
        print("""
    Wrong!
    
        Here's some help. The definition of this word is: {}
    
    Try again!
        """.format(game_dictionary[word][2][0]))
        
        second_response = input(""" >>>>> Your translation: """)
        if second_response in game_dictionary[word][0][0]:
            points += 1
            print("""
    Now you got it!
    
    Points: {}
            """.format(points))
        else: 
            print("""
    Wrong again!
    
    The possible right answers were: {0})
    
    Points: {1}
    """.format(game_dictionary[word][0][0],points))
        
print(""" 
>>> Final score: {0} /{1} <<< """
      .format(points,limit))

final_score = points/limit

if final_score == 1.0:
    print('*** Wow, you are amazing! ***')
if final_score < 1.0 and final_score >= 0.75 :
    print('*** That was great! ***')
if final_score < 0.75 and final_score >= 0.5:
    print('*** Well done ***')
if final_score < 0.5 and final_score >= 0.25:
    print('*** You need to practice more ***')
if final_score < 0.25:
    print('*** Oops, that was bad... ***')