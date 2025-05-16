# Restrict unpickling to safe classes 
import pickle 
 
class RestrictedUnpickler(pickle.Unpickler): 
    def find_class(self, module, name): 
        if module == "numpy" and name == "ndarray": 
            return getattr(numpy, name) 
        raise pickle.UnpicklingError(f"Unsafe {module}.{name}") 
 
RestrictedUnpickler(open("safe.pkl", "rb")).load()