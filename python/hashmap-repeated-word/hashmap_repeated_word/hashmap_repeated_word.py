# from linkedlist import LinkedList,Node

from collections import Counter
# class HashTable(object):
#     def __init__(self,size=200):
#         self.size= size
#         self.map = [None]*size

#     def custom_hash(self,key):
#         sum_of_asscci = 0
#         for ch in key:
#             ascci_of_ch = ord(ch)

#             sum_of_asscci += ascci_of_ch   
#         temp_value = sum_of_asscci * 19
#         hashed_key = temp_value %  self.size

#         return hashed_key


#     def add(self,key):
        
#         hashed_key = self.custom_hash(key)
#         if not self.map[hashed_key]:
#             self.map[hashed_key]  = key
#         else:

#             if isinstance(self.map[hashed_key],LinkedList):
               
#                 self.map[hashed_key].append(key)
#                 return
#             else:
                
#                 chain = LinkedList()
#                 existing_pair = self.map[hashed_key]
#                 new_pair = key
#                 self.map[hashed_key] = chain

#                 chain.append(existing_pair)
#                 chain.append(new_pair)
        
#     def get_value(self,key):
#         hashed_key = self.custom_hash(key)
#         return self.map[hashed_key]

#     def contains(self,key):
#         new_key = self.custom_hash(key)
        

#         if self.map[new_key] is None:
            
#             return False
#         else: 
#             return True

string  = "it was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."


# def hashmap_repeated_word(string):
#     arr = string.split(" ")
#     hash_table=HashTable()
#     # print(arr)
#     for word in arr :
#         hash_table.add(word)

#     print(hash_table.map)
#     for index,item in enumerate(hash_table.map):
#         if item:
#             print(index,item)

#     List = ''
#     for i in  hash_table.map: 
#         if isinstance(i,LinkedList):
        
#             List = i  
#             break
#     print(List.head.value)
#     return List.head.value
   # spliting the string
def hashmap_repeated_word(string): 
    lis = list(string.split(" "))
     
    # Calculating frequency of every word
    frequency = Counter(lis)
     
    # Traversing the list of words
    for i in lis:
       
        # checking if frequency is greater than 1
         
        if(frequency[i] > 1):
            # return the word
            return i






print(hashmap_repeated_word(string))
