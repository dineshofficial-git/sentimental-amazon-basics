import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re
def process_review(review):

    #convert review into lowercase form
    review_lower = review.lower()
    
    #removes punctuations and numbers
    review_puncs_nums_removed = re.sub(r"[^a-z\s]", "", review_lower)

    #tokenize the review and coverts sentence to words
    review_tokens = word_tokenize(review_puncs_nums_removed)

    # remove the stop words
    stop_words = stopwords.words('English')
    review_tokens_stopwords_removed = [token for token in review_tokens if token not in stop_words]

    # lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token, pos='n') for token in review_tokens_stopwords_removed]

    return " ".join(lemmatized_tokens)

if __name__ == "__main__" :
    review = "the product was really nice"
    print(process_review(review))