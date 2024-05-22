import nltk
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk import ngrams
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import brown
from nltk import pos_tag
from nltk.tag import pos_tag, map_tag
# Task 3
# Q1 
nlp = spacy.load('en_core_web_sm')
def sentence_tokens(text) :
    doc = nlp(text)
    sentences = [sentence.text for sentence in doc.sents]
    return sentences
input_text = input("Enter input in duetch :")
sentences = sentence_tokens(input_text)
print("Tokenized Sentence is : ")
for sentence in sentences :
    print(sentence)
#--------------------------------------------------------------------------------------
# Q2 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')

def tag_with_universal_tagset(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words) 
    universal_tags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in pos_tags]
    return universal_tags

def tag_with_penn_treebank_tagset(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    return pos_tags

input_text = input("Please enter the text you want to tag: ")

penn_tags = tag_with_penn_treebank_tagset(input_text)
universal_tags = tag_with_universal_tagset(input_text)

print("\nPart-of-Speech Tags using Penn Treebank Tagset:")
print(penn_tags)

print("\nPart-of-Speech Tags using Universal Tagset:")
print(universal_tags)


print("\nComparison of Penn Treebank and Universal Tagsets:")
for penn, universal in zip(penn_tags, universal_tags):
    print(f"{penn[0]}: {penn[1]} (Penn) vs {universal[1]} (Universal)")
#--------------------------------------------------------------------------------------
# Q3 
nltk.download('stopwords')
def get_stop_words(language) :
    try :
        stop_words = set(stopwords.words(language))
    except OSError :
        return f"\n there is no stop words in {language}"
languges = ['english', 'germen', 'spanish', 'italian', 'french']
for language in languges :
    print(f"\n stop words in {language.capitalize()} : ")
    print(get_stop_words(language))