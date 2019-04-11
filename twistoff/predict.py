import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import *
from .twitter import *

def predict(user1_name, user2_name, s):
    user1 = User.query.filter(User.name == user1_name).one()
    user2 = User.query.filter(User.name == user2_name).one()
    user1_embeddings = np.array([tweet.embedding for tweet in user1.tweets])
    user2_embeddings = np.array([tweet.embedding for tweet in user2.tweets])
    user1_labels = np.ones(len(user1.tweets))
    user2_labels = np.zeros(len(user2.tweets))
    embeddings = np.vstack([user1_embeddings, user2_embeddings])
    labels = np.concatenate([user1_labels, user2_labels])
    log_reg = LogisticRegression(solver='lbfgs', max_iter=1000)
    log_reg.fit(embeddings, labels)

    tweet_text = s
    tweet_embedding = BASILICA.embed_sentence(tweet_text, model='twitter')
    log_reg.predict(np.array(tweet_embedding).reshape(1, -1))

    return log_reg.predict(np.array(tweet_embedding).reshape(1, -1))[0]