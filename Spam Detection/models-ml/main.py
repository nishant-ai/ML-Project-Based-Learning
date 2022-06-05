import sklearn, string, nltk, pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

# Preprocessing Function
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

trans_text = transform_text(input("Enter any text: ")) # transform text
vector_input = vectorizer.transform([trans_text]) # vectorize
result = model.predict(vector_input)[0] # predict


print("----------------------------")
print("Transformed Text - ")
print(trans_text)
print("----------------------------")
print("Vector Input: ")
print(vector_input)
print("----------------------------")



if result == 1: print("Spam Category")
else: print("Not Spam")