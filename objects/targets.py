import os
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


def init_test_target_values():
    if not os.path.exists('data'):
        os.makedirs('data')
        os.makedirs('data/objects')
        os.mknod('data/objects/target_data.pkl')

        target_list = [
            Target('ananke', '192.168.2.2'),
            Target('echo', '192.168.2.20'),
            Target('consus', '192.168.2.21')
        ]

        save_object(target_list, 'data/objects/target_data.pkl')
