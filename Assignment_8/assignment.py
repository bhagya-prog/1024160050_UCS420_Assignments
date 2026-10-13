import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

#Q1 
text = """
I love reading books, my favourite being Harry Potter series.
I love exploring deep about AI-ML and also trying new technologies.
In food, I though love everything but my favourite is paneer.
in sports, I personally love cricket and badminton.
I also enjoy learning new languages and exploring different cultures.
And my favourite hobby is writing poems and short stories. 
"""

clean_text = re.sub(r'[^\w\s]', '', text.lower())
print("Cleaned Text:\n", clean_text)


words = word_tokenize(text.lower())
sentences = sent_tokenize(text)

print("\nWord Tokens:\n", words)
print("\nSentence Tokens:\n", sentences)


print("\nUsing split():")
print(text.lower().split())

print("\nUsing word_tokenize():")
print(word_tokenize(text.lower()))

stop_words = set(stopwords.words('english'))
filtered_words = [
    word for word in word_tokenize(clean_text)
    if word not in stop_words and word.isalpha()
]
print("\nWords after removing stopwords:\n", filtered_words)

frequency = FreqDist(filtered_words)
print("\nWord Frequency Distribution:")
print(frequency)
print("\nMost Common Words:")
print(frequency.most_common())

#Q2
words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
print("Extracted Words:\n", words)

stop_words = set(stopwords.words('english'))
filtered_words = [w for w in words if w not in stop_words]
print("\nAfter Stopword Removal:\n", filtered_words)

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(w) for w in filtered_words]
print("\nStemmed Words:\n", stemmed_words)

lemmatizer = WordNetLemmatizer()
lemmatized_words = [
    lemmatizer.lemmatize(w) for w in filtered_words
]
print("\nLemmatized Words:\n", lemmatized_words)

print("\nComparison:")
for original, stem, lemma in zip(
    filtered_words, stemmed_words, lemmatized_words
):
    print(original, "-> Stem:", stem, "| Lemma:", lemma)

#Q3
texts = [
    "Artificial intelligence improves healthcare and education",
    "Machine learning helps computers learn from data",
    "Natural language processing enables computers to understand human language",
]

count_vectorizer = CountVectorizer()
bow_matrix = count_vectorizer.fit_transform(texts)

print("Bag of Words Vocabulary:")
print(count_vectorizer.get_feature_names_out())

print("\nBag of Words Matrix:")
print(bow_matrix.toarray())


tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(texts)

feature_names = tfidf_vectorizer.get_feature_names_out()
print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())

print("\nTop 3 Keywords for Each Text:")

for i, row in enumerate(tfidf_matrix.toarray()):
    top_indices = row.argsort()[::-1][:3]
    top_words = [
        (feature_names[j], round(row[j], 3))
        for j in top_indices
    ]
    print(f"Text {i + 1}: {top_words}")

#Q4
text1 = """
Artificial intelligence enables computers to learn from data.
Machine learning helps systems make predictions.
AI automates tasks and improves decision making.
"""

text2 = """
Blockchain is a distributed digital ledger.
It stores transactions in connected blocks.
Blockchain improves transparency and data security.
"""
def preprocess(text):
    text = text.lower()
    words = re.findall(r'\b[a-z]+\b', text)
    return words

words1 = preprocess(text1)
words2 = preprocess(text2)

print("Tokens of Text 1:\n", words1)
print("\nTokens of Text 2:\n", words2)

set1 = set(words1)
set2 = set(words2)

intersection = set1.intersection(set2)
union = set1.union(set2)

jaccard = len(intersection) / len(union)

print("\nCommon Words:", intersection)
print("Jaccard Similarity:", round(jaccard, 4))

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([text1, text2])

cosine = cosine_similarity(
    tfidf_matrix[0:1],
    tfidf_matrix[1:2]
)[0][0]

print("Cosine Similarity:", round(cosine, 4))

print("\nAnalysis:")
print("Jaccard measures the overlap between unique words.")
print("Cosine measures similarity between TF-IDF vectors.")

if jaccard > cosine:
    print("Jaccard similarity is higher in this example.")
elif cosine > jaccard:
    print("Cosine similarity is higher in this example.")
else:
    print("Both similarity values are equal.")

#Q5
reviews = [
    "This product is amazing and works perfectly.",
    "I love the quality and excellent performance.",
    "The product is terrible and very disappointing.",
    "The service was slow and the product was damaged.",
    "The product is okay and works as expected.",
    "The quality is good and I am very happy with it."
]

positive_reviews = []

print("Sentiment Analysis Results:\n")

for review in reviews:
    analysis = TextBlob(review).sentiment
    polarity = analysis.polarity
    subjectivity = analysis.subjectivity

    if polarity > 0:
        sentiment = "Positive"
        positive_reviews.append(review)
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print("Review:", review)
    print("Polarity:", round(polarity, 3))
    print("Subjectivity:", round(subjectivity, 3))
    print("Sentiment:", sentiment)
    print("-" * 50)

if positive_reviews:
    positive_text = " ".join(positive_reviews)

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate(positive_text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Positive Reviews")
    plt.show()
else:
    print("No positive reviews available.")

#Q6
text = """
Artificial intelligence is changing the world.
Technology helps people solve difficult problems.
Machine learning allows computers to learn from data.
Deep learning is used in image recognition and language processing.
Students can use technology to improve their knowledge.
Learning programming develops logical thinking.
Python is a popular language for artificial intelligence.
Data helps computers identify patterns and make predictions.
Neural networks learn complex relationships from examples.
Artificial intelligence can support education, healthcare, and science.
Technology continues to develop every day.
Learning new skills helps people prepare for the future.
Computers can generate text using language models.
Machine learning improves when useful training data is available.
Artificial intelligence makes many tasks faster and easier.
"""


tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])

total_words = len(tokenizer.word_index) + 1
print("Total Unique Words:", total_words)

# 
input_sequences = []

for line in text.lower().split("."):
    line = line.strip()

    if not line:
        continue

    token_list = tokenizer.texts_to_sequences([line])[0]

    for i in range(1, len(token_list)):
        sequence = token_list[:i + 1]
        input_sequences.append(sequence)

max_sequence_len = max(len(seq) for seq in input_sequences)

input_sequences = pad_sequences(
    input_sequences,
    maxlen=max_sequence_len,
    padding="pre"
)

X = input_sequences[:, :-1]
y = input_sequences[:, -1]

model = Sequential([
    Embedding(
        input_dim=total_words,
        output_dim=32,
        input_length=max_sequence_len - 1
    ),
    LSTM(64),
    Dense(total_words, activation="softmax")
])

model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

model.summary()

model.fit(X, y, epochs=100, verbose=0)

print("\nModel Training Completed!")


def generate_text(seed_text, next_words=8):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences(
            [seed_text]
        )[0]

        token_list = pad_sequences(
            [token_list],
            maxlen=max_sequence_len - 1,
            padding="pre"
        )

        predictions = model.predict(token_list, verbose=0)
        predicted_id = int(np.argmax(predictions, axis=1)[0])

        output_word = None

        for word, index in tokenizer.word_index.items():
            if index == predicted_id:
                output_word = word
                break

        if output_word is None:
            break

        seed_text += " " + output_word

    return seed_text

seed = "artificial intelligence"

print("\nGenerated Text:")
for i in range(3):
    print(f"Line {i + 1}:", generate_text(seed, next_words=8))

    