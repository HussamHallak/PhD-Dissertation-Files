from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

documents = []

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

k = 2
model = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print

print("\n")
print("Prediction")

new_documents = ["", ""]

Y = vectorizer.transform(new_documents[0])
prediction = model.predict(Y)
print(prediction)

Y = vectorizer.transform(new_documents[0])
prediction = model.predict(Y)
print(prediction)
