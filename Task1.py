# Task 1
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

def tokenize_words(text):
    return nltk.word_tokenize(text)

def tokenize_sentences(text):
    return nltk.sent_tokenize(text)

def main():
    user_text = input("Enter some text: ")

    print("Choose an option:")
    print("1. Print tokenized words")
    print("2. Print tokenized sentences")
    print("3. Print output using split function")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        tokenized_words = tokenize_words(user_text)
        print("Tokenized words:", tokenized_words)
    elif choice == 2:
        tokenized_sentences = tokenize_sentences(user_text)
        print("Tokenized sentences:", tokenized_sentences)
    elif choice == 3:
        # Using split() function to split by spaces
        split_words = user_text.split()
        print("Output using split function:", split_words)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
#--------------------------------------------------------------------------------------
print(PorterStemmer().stem("Computation"))
lists = ["Apples", "Dogs", "Books", "Running"]
pp = [PorterStemmer().stem(listi) for listi in lists]
print('|'.join(pp))
#--------------------------------------------------------------------------------------
language = SnowballStemmer(language = "english")
lists = ["Apples", "Dogs", "Books", "Running"]
pp = [language.stem(listi) for listi in lists]
print('|'.join(pp))#--------------------------------------------------------------------------------------
sentence = input("Enter Sentence : ")
Value_n = int(input("Enter the value of n :"))
n_grams = ngrams(sentence.split(), Value_n)
for ngrams in n_grams :
    print(ngrams)
#--------------------------------------------------------------------------------------
nlp = spacy.load("en_core_web_sm")
text = "Spacy is a good library jsdhkjfhdsbf dhfkjdsgfdgfjd dkfjgeiuwyfidnckjd dfjhdjvudyfowihfkwj"
doc_text =  nlp(text)
print(doc_text)
text_sent = [sentence.text for sentence in doc_text.sents]
print(text_sent)
text_token = [token.text for token in doc_text]
print(text_token)
#--------------------------------------------------------------------------------------

nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
text = "This is a sample text with some common stop words. Stop words are usually filtered out before processing natural language data. Despite their commonness, they carry very little meaningful information about the content of the text."
tokenized_text = word_tokenize(text)
filtered_text = [word for word in tokenized_text if not word.lower() in stop_words]
print(filtered_text)
#--------------------------------------------------------------------------------------
nltk.download("brown")
print(brown.tagged_words()[:40])
nltk.download('avareged_preceptron_tagger')
nltk.download('universal_tagset')
text = " Call me later"
tokens = word_tokenize(text)
print(pos_tag(tokens, tagset='universal'))
#--------------------------------------------------------------------------------------
nlp = spacy.load("en_core_web_sm")
words = nlp("I ate banana")
print(words[2].vector) 

