import sys
import json
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB

# training data
train_file = 'training.json'

# Read and preprocess the training data
train_data = []
with open(train_file) as f:
    for line in f:
        train_data.append(json.loads(line))

del train_data[0]

# Continue preprocessing. Extract the train data to the lists for training a model
train_question = []
train_topic = []
train_excerpt = []
for i in train_data:
    train_question.append(i['question'].replace('\n', '').replace('\r', '').strip('  '))
    train_excerpt.append(i['excerpt'].replace('\n', '').replace('\r', '').strip('  '))
    train_topic.append(i['topic'].replace('\n', '').replace('\r', '').strip('  '))

# Combine train_question words with train_excerpt words together
train_list_global = []
for i in range(len(train_data)):
    train_list_global.extend([train_question[i] + ' ' + train_excerpt[i]])
    
train_data = []
for i in train_list_global:
    train_data.append(str(''.join([j if ord(j) < 128 else ' ' for j in i])))
  
# Convert unicode to str    
train_category = map(str, train_topic)

# Transform train_data to feature vectors
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(train_data)
count_vect.vocabulary_.get(u'algorithm')

# Compute tf (Term Frequencies) and td-idf (Term Frequency times Inverse Document Frequency).
# Use fit() method to fit estimator (train_cat) to data (train_data).
# Use transform() method to transform count-matrix to a tf-idf representation
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)

# Faster approach by skipping redun. processing. Use fit_transform() method
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

# Training a classifier
# Select Naive Bayes classifier for multinomial models
# Select This estimator implements regularized linear models with stochastic gradient descent (SGD) learning
# Build a Pipeline class to make the transformation vectorizer => transformer => classifier easier to work with

# Pipeline for Naive Bayes Model
# text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB()), ])

# Pipeline for Linear Model with Stochastic Gradient Descent
text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-4, n_iter=5, random_state=None)), ])

# Train the chosen model using the following approach: question + excerpt words against category word
_ = text_clf.fit(train_data, train_category)
    
# Read the test data for predictions
N = int(raw_input())
test_data = []
for _ in range(N):
    s = raw_input()
    test_data.append(json.loads(s))

# Preprocess the test data for running predictions with the model
test_question = []
test_excerpt = []
for i in test_data:
    test_question.append(i['question'].replace('\n', '').replace('\r', '').strip('  '))
    test_excerpt.append(i['excerpt'].replace('\n', '').replace('\r', '').strip('  '))
    
test_list_global = []
for i in range(len(test_data)):
    test_list_global.extend([test_question[i] + ' ' + test_excerpt[i]])
    
test_data = []
for i in test_list_global:
    test_data.append(str(''.join([j if ord(j) < 128 else ' ' for j in i])))

# Print each predicted outcome on trained Linear Model with SGD:
for i in text_clf.predict(test_data):
    print i