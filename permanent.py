import time
from itertools import takewhile
import operator
import pickle
from kademlia.storage import IStorage
from collections import OrderedDict
from abc import abstractmethod, ABC

class PermanentStorage(IStorage):
    def __init__(self, ttl=604800):
        """
        By default, max age is a week.
        """
        self.data = OrderedDict()
        self.ttl = ttl
        try : 
            """
			Saving in a file, on a line : time key value
			"""
            f = open("db", "rb")
            try:
                while True:
                    l = pickle.load(f)
                    self.data[l[1]] = (l[0], l[2])
            except:
                pass
            f.close()
            
            self.cull()
        except : 
            pass

    def __setitem__(self, key, value):
        
        if key in self.data:
            del self.data[key]
        t = time.monotonic()
        f = open("db", "ab")
        pickle.dump((t,key, value),f)
        f.close()
        self.data[key] = (t, value)
        self.cull()

    def cull(self):
        for _, _ in self.iter_older_than(self.ttl):
            self.data.popitem(last=False)

    def get(self, key, default=None):
        self.cull()
        if key in self.data:
            return self[key]
        return default

    def __getitem__(self, key):
        self.cull()
        return self.data[key][1]

    def __repr__(self):
        self.cull()
        return repr(self.data)

    def iter_older_than(self, seconds_old):
        min_birthday = time.monotonic() - seconds_old
        zipped = self._triple_iter()
        matches = takewhile(lambda r: min_birthday >= r[1], zipped)
        return list(map(operator.itemgetter(0, 2), matches))

    def _triple_iter(self):
        ikeys = self.data.keys()
        ibirthday = map(operator.itemgetter(0), self.data.values())
        ivalues = map(operator.itemgetter(1), self.data.values())
        return zip(ikeys, ibirthday, ivalues)

    def __iter__(self):
        self.cull()
        ikeys = self.data.keys()
        ivalues = map(operator.itemgetter(1), self.data.values())
        return zip(ikeys, ivalues)
