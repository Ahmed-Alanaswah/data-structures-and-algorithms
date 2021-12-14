# # from hashtable import hashtable

# from linkedlist import LinkedList,Node


# class HashTable(object):
#     def __init__(self,size=20):
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


#     def add(self,key,value):
        
#         hashed_key = self.custom_hash(key)
#         if not self.map[hashed_key]:
#             self.map[hashed_key]  = [key,value]
#         else:

#             if isinstance(self.map[hashed_key],LinkedList):
               
#                 self.map[hashed_key].append([key,value])
#                 return
#             else:

#                 chain = LinkedList()
#                 existing_pair = self.map[hashed_key]
#                 new_pair = [key,value]
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



# if __name__=="__main__":

#     Synonem_hash_table=HashTable()
#     Synonem_hash_table.add("fond","enamored")
#     Synonem_hash_table.add("wrath","anger")
#     Synonem_hash_table.add("diligent","employed")
#     Synonem_hash_table.add("outift","garb")
#     Synonem_hash_table.add("guide","usher")
    

#     Antonym_hash_table=HashTable()
#     Antonym_hash_table.add("fond","averse")
#     Antonym_hash_table.add("wrath","delight")
#     Antonym_hash_table.add("diligent","idle")
#     Antonym_hash_table.add("guide","follow")
#     Antonym_hash_table.add("flow","jam")
#     for index,item in enumerate(Synonem_hash_table.map):
#         if item:
#             print(index,item)
#     print('============')

#     newArr1=[]
#     newArr2 = []
#     newArr3 = []
#     for i in  range(len(Synonem_hash_table.map)):
#         if Synonem_hash_table.map[i] is not None :
#             newArr1.append(Synonem_hash_table.map[i])


#     for i in  range(len(Antonym_hash_table.map)):
#         if Antonym_hash_table.map[i] is not None :
#             newArr2.append(Antonym_hash_table.map[i])

#     for i in  range(len(newArr1)) :
#         for j in  range(len(newArr2)):
#             if newArr1[i][0] == newArr2[j][0]: 
#               newArr3  += [newArr1[i] + [newArr2[j][1]]]
            
#     for i  in newArr1 :
#         if Antonym_hash_table.contains(i[0])==False:
#             newArr3  += [i + ['NULL']]
            

#     print(newArr1)
#     print(newArr2)
#     print('======')
#     print(newArr3)
#     print('-----')

#     # print('============')
#     # print(Synonem_hash_table.map)
#     # print('============')
#     # print(Antonym_hash_table.map)
