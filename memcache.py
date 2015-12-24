## Memcache

## set[key, value] ==> returns True
## get(key) ==> returns Value or None
## delete(key)
## flush()

MEMORY = {}

class Memcache:
    def __init__(self):
        global MEMORY
        self.CACHE = MEMORY

    def set(self, key, value):
        self.CACHE[key] = value
        # print(self.CACHE)
        return True

    def get(self, key):
        x = self.CACHE[key]
        return x

    def delete(self, key):
        if key in self.CACHE:
            del self.CACHE[key]

    def flush(self):
        self.CACHE.clear()

#
# def test_memcache():
#     m = Memcache()
#     print(m.set('a', '1'))
#     print(m.set('b', '2'))
#     print(m.CACHE)
#     print(m.get('b'))
#     m.delete('b')
#     print(m.CACHE)
#     m.flush()
#     print(m.CACHE)


# True
# True
# {'a':'1', 'b':'2'}
# 2
# {'a':'1'}
# {}

if __name__ == '__main__':
    test_memcache()