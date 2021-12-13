import pickle

model = None
with open('model.pkl', 'rb') as pickle_file:
   model = pickle.load(pickle_file)
   
print(y_pred)