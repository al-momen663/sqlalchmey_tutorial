import pickle

data = {'model': 'RandomForest', 'score': 0.91}
with open('model.pkl', 'wb') as file:
    pickle.dump(data, file)

# Load later
with open('model.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
