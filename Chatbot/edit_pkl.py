import pickle


with open('stopwords.pkl', 'rb') as f:
    data = pickle.load(f)
    
# data.remove('name')
print(data)
# pickle.dump(data, open( "stopwords.pkl", "wb" ) )