import pickle

pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)
print(example_dict)
