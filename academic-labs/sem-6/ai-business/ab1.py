import nltk
from nltk.util import ngrams
from collections import defaultdict, Counter

nltk.download('punkt')
nltk.download('punkt_tab')

# Sample email dataset
emails = [
    "thank you for your email",
    "please let me know if you have any questions",
    "looking forward to your response",
    "thank you for your time and consideration",
    "please find the attached document",
    "let me know if you need any help"
]

# Tokenize Sentences
tokens = []
for email in emails:
    words = nltk.word_tokenize(email.lower())
    tokens.extend(words)

# Create trigram model
model = defaultdict(Counter)
for w1, w2, w3 in ngrams(tokens, 3):
    model[(w1, w2)][w3] += 1

# Function to predict next word
def predict_next_word(text):
    words = nltk.word_tokenize(text.lower())
    if len(words) < 2:
        return "Type more words..."
    
    last_two = (words[-2], words[-1])
    if last_two in model:
        next_word = model[last_two].most_common(1)[0][0]
        return next_word
    else:
        return "No prediction available"

# Test
input_text = "thank you"
prediction = predict_next_word(input_text)
print("Input:", input_text)
print("Predicted next word:", prediction)
