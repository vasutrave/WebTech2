import numpy as np 
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
import re
def get_sentiment(review):

	data = pd.read_csv('Sentiment.csv')
	data = data[['text','sentiment']]

	data = data[data.sentiment != "Neutral"]
	data['text'] = data['text'].apply(lambda x: x.lower())
	data['text'] = data['text'].apply((lambda x: re.sub('[^a-zA-z0-9\s]','',x)))

	

	for idx,row in data.iterrows():
	    row[0] = row[0].replace('rt',' ')
	    
	max_fatures = 2000
	tokenizer = Tokenizer(num_words=max_fatures, split=' ')
	tokenizer.fit_on_texts(data['text'].values)
	X = tokenizer.texts_to_sequences(data['text'].values)
	X = pad_sequences(X)

	model = load_model("senti.h5")

	twt = [review]
	
	twt = tokenizer.texts_to_sequences(twt)
	
	twt = pad_sequences(twt, maxlen=28, dtype='int32', value=0)
	
	sentiment = model.predict(twt,batch_size=1,verbose = 2)[0]

	if np.argmax(sentiment) == 0:
	    return "Negative"

	elif np.argmax(sentiment) == 1:
	    return "Positive"

if __name__ == '__main__':
	
	review = "Food is amazing so is the excellent service"

	print(get_sentiment(review))