#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#importing some Python libraries
import csv
import math
documents = []
labels = []

#reading the data in a csv file
with open('/Users/josenunez/Downloads/search engine/collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
    if i > 0:  # skipping the header
      documents.append (row[0])
      labels.append(row[1])
print(labels)


#Conduct stopword removal.
#--> add your Python code here
stopWords = {'I', 'and', 'She', 'They', 'her', 'their'}

def remove_stopwords(document, stopwords):
    words = document.split()
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)
documents = [remove_stopwords(doc, stopWords) for doc in documents]
print(documents)

#Conduct stemming.
#--> add your Python code here
steeming = {
  "cats": "cat",
  "dogs": "dog",
  "loves": "love",
}

def stem_words(document, stemming_dict):
    words = document.split()
    stemmed_words = [stemming_dict.get(word, word) for word in words]
    return ' '.join(stemmed_words)

documents = [stem_words(doc, steeming) for doc in documents]
print("documents: ",documents)

#Identify the index terms.
#--> add your Python code here
terms = []


terms = [doc.split() for doc in documents]

print("terms",terms)

query = "cat and dogs"
query_terms = query.split()
query_terms = [remove_stopwords(doc, stopWords) for doc in query_terms]
query_terms = [stem_words(doc, steeming) for doc in query_terms]
print("query search",query_terms)

#Build the if-idf term weights matrix.
#--> add your Python code here
docMatrix = []
def calculate_tf_idf(term, document, terms):
    tf = document.count(term) / len(document.split())
    idf = math.log(len(terms) / (sum(1 for doc in terms if term in doc) + 1))
    return tf * idf

for doc in terms
    doc_weights = [calculate_tf_idf(term, ' '.join(doc), terms) for term in query_terms]
    docMatrix.append(doc_weights)
print("matrix",docMatrix)

    

#Calculate the document scores (ranking) using document weigths (tf-idf) calculated before and query weights (binary - have or not the term).
#--> add your Python code here
docScores = []
for doc_weights in docMatrix:
    doc_score = sum(doc_weights)
    docScores.append(doc_score)
print(docScores)
#Calculate the precision and recall of the model by considering that the search engine will return all documents with weights >= 0.1.
#--> add your Python code here




retrieved_documents = [i for i, score in enumerate(docScores) if score >= 4.7]
print(retrieved_documents)
# True labels 
relevant_documents = [i for i, label in enumerate(labels) if label == ' R']
print(relevant_documents)
# Calculate precision and recall
def calculate_precision_recall(retrieved, relevant):
    a = len(set(retrieved) & set(relevant))  # True positives (hits)
    b = len(set(retrieved) - set(relevant))  # False positives (noise)
    c = len(set(relevant) - set(retrieved))  # False negatives (misses)
    
    recall = (a / (a + c)) * 100.0
    precision = (a / (a + b)) * 100.0

    return precision, recall

precision, recall = calculate_precision_recall(retrieved_documents, relevant_documents)

# Output precision and recall
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")