from hashmap_left_join import __version__
from hashmap_left_join.hashmap_left_join import HashTable,left_join

def test_version():
    assert __version__ == '0.1.0'


def test_left_join():
    Synonem_hash_table=HashTable()
    Synonem_hash_table.add("fond","enamored")
    Synonem_hash_table.add("wrath","anger")
    Synonem_hash_table.add("diligent","employed")
    Synonem_hash_table.add("outift","garb")
    Synonem_hash_table.add("guide","usher")


    Antonym_hash_table=HashTable()
    Antonym_hash_table.add("fond","averse")
    Antonym_hash_table.add("wrath","delight")
    Antonym_hash_table.add("diligent","idle")
    Antonym_hash_table.add("guide","follow")
    Antonym_hash_table.add("flow","jam")

    actual = left_join(Synonem_hash_table,Antonym_hash_table)
    expected = [['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse'], ['outift', 'garb', 'NULL']]
    assert actual == expected