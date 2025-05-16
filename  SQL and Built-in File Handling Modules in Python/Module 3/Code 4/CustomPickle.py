#Custom Pickle protocols

import pickle 
 
class CustomModel: 
    def __reduce__(self): 
        return (self.__class__, (self.important_param,)) 
 
# Use protocol 5 (Python 3.8+) for out-of-band data 
with open("model.pkl", "wb") as f: 
    pickle.dump(model, f, protocol=5, buffer_callback=...) 
