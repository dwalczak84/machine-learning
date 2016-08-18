# https://www.hackerrank.com/challenges/document-classification

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier


# Load the training file from problem's directory
train_data = []
with open('trainingdata.txt') as f:
    for line in f:
        train_data.append(line)
del train_data[0]    

train_cat = []        
for i in train_data:
    train_cat.append(int(i[0]))

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
# Select linear support vector machine (SVM)
# Build a Pipeline class to make the transformation vectorizer => transformer => classifier easier to work with
text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-4, n_iter=5, random_state=None)), ])
_ = text_clf.fit(train_data, train_cat)

# Read real data and build one big list of documents as strings:
documents = []
n = int(raw_input())
for i in range(n):
    s = raw_input()
    documents.append(s)
    
# Makre a classification basedn on the prediction of the model on the documents. Print each category in new line
for i in text_clf.predict(documents):
    print i

