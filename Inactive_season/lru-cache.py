# https://leetcode.com/problems/lru-cache/



class Node:
    def __init__(self, key, value):
        self.prev = None
        self.key = key
        self.value = value
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_val = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        

    def get(self, key: int) -> int:
        # print(self.key_val.keys())
        # check if the key exists
        if key in self.key_val:
            self.put(key, self.key_val[key].value)
            temp_curr = self.key_val[key]
            return temp_curr.value
        
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        # print(self.key_val.keys())

        if key in self.key_val:
            
            # insert the value at the beginning
            to_be_removed = self.key_val[key]
            prev = to_be_removed.prev
            nex = to_be_removed.next
            prev.next = nex
            nex.prev = prev
            # print("to be deleted: ", key)
            del self.key_val[key]
            # self.key_val.pop(to_be_removed.key, -1)
            
        if len(self.key_val) >= self.capacity:
            to_be_removed = self.tail.prev
            self.tail.prev = self.tail.prev.prev
            prev = to_be_removed.prev
            prev.next = self.tail
            del self.key_val[to_be_removed.key]

            
        temp_next = self.head.next
        new_node = Node(key, value)
        
        # adding the new_node to the cache
        self.key_val[key] = new_node
    
        # creating the connection b/n new node and head
        self.head.next = new_node
        new_node.prev = self.head
        
        # creating the connection b/n new node and the one that comes next
        temp_next.prev = new_node
        new_node.next = temp_next
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
