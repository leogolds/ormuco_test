from gdlru.lru import LRUCache


def test_lru1():
    lru = LRUCache(2)
    assert lru.get(2) is -1
    assert lru.put(2, 6) is None
    assert lru.get(1) is -1
    assert lru.put(1, 5) is None
    assert lru.put(1, 2) is None
    assert lru.get(1) is 2
    assert lru.get(2) is 6


def test_lru2():
    lru = LRUCache(2)
    assert lru.put(1, 1) is None
    assert lru.put(2, 2) is None
    assert lru.get(1) is 1
    assert lru.put(3, 3) is None
    assert lru.get(2) is -1
    assert lru.put(4, 4) is None
    assert lru.get(1) is -1
    assert lru.get(3) is 3
    assert lru.get(4) is 4


