import _pickle as pickle
from dataclasses import dataclass, field

@dataclass(order=True)
class Target:
    # Defines the required values for this object
    name: str = field(compare=False)
    value: str

def save_object(self, filename):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(self, outp, -1)

def pickle_loader(filename) -> Target:
    # Deserialize a file of pickled objects.
    with open(filename, 'rb') as inp:
        return pickle.load(inp)

