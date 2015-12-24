import fake_database
from memcache import Memcache


def printName():
    print(str(__name__))

qlist = []
cache = Memcache()

def lastMultipliedHandler(quanswer, value):
    """keep appending qlist until you have 5, then delete the 1st element and append the latest one at the end, in order
    to display a top five list."""
    qlist.append(quanswer)
    if len(qlist) <= 4:
        print("Last result:", value)
        return qlist
    elif len(qlist) == 5:
        print("Last result:", value)
        r = "Last five: {}".format(qlist)
        return r
    elif len(qlist) > 5:
        qlist.reverse()
        qlist.pop()
        qlist.reverse()
        print("Last result:", value)
        r = "Last five: {}".format(qlist)
        return r


def multiplyHandler(a, b):
    value = fake_database.russian(a, b)
    key = (a,b)
    if key in cache.CACHE:
        print("Used Cache")
        quanswer = ("{0}x{1} = {2}".format(a, b, value))
        return lastMultipliedHandler(quanswer, value)
    else:
        cache.set(key,value)
    quanswer = ("{0}x{1} = {2}".format(a, b, value))
    return lastMultipliedHandler(quanswer, value)


if __name__ == "__main__":
    print()
    multiplyHandler(33, 77)
    print()
    multiplyHandler(21, 12)
    print()
    multiplyHandler(216, 18)
    print()
    multiplyHandler(8, 64)
    print()
    multiplyHandler(64, 444)
    print()
    multiplyHandler(9, 999)
    print()
    multiplyHandler(88, 6)
    print()
    multiplyHandler(55, 10)
    print()
    multiplyHandler(21, 12)
    print()
    multiplyHandler(33, 77)
