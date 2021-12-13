# from hashtable import hashtable

from linkedList import LinkedList,Node


class HashTable(object):
    def __init__(self,size=200):
        self.size= size
        self.map = [None]*size

    def custom_hash(self,key):
        sum_of_asscci = 0
        for ch in key:
            ascci_of_ch = ord(ch)

            sum_of_asscci += ascci_of_ch   
        temp_value = sum_of_asscci * 19
        hashed_key = temp_value %  self.size

        return hashed_key


    def add(self,key):
        
        hashed_key = self.custom_hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key]  = key
        else:

            if isinstance(self.map[hashed_key],LinkedList):
               
                self.map[hashed_key].append(key)
                return
            else:

                chain = LinkedList()
                existing_pair = self.map[hashed_key]
                new_pair = key
                self.map[hashed_key] = chain

                chain.append(existing_pair)
                chain.append(new_pair)
        
    def get_value(self,key):
        hashed_key = self.custom_hash(key)
        return self.map[hashed_key]

    def contains(self,key):
        new_key = self.custom_hash(key)
        

        if self.map[new_key] is None:
            
            return False
        else: 
            return True



# if __name__=="__main__":

#     hash_table=HashTable()
#     hash_table.add("ahmad")
#     hash_table.add("ali")
#     hash_table.add("hamad")


#     for index,item in enumerate(hash_table.map):
#         if item:
#             print(index,item)

#     print(hash_table.contains('hamad'))
#     print(hash_table.contains('kk'))
#     print(hash_table.contains('ahmad'))
#     print(hash_table.map)
