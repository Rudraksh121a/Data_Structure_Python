#  Singly Linked List

# Create a Node    
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SLL:
    def __init__(self,start=None):
        self.start=start

# Check list is empty or not
    def is_empty(self):
        return self.start==None
    
# insert at first note
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n

# insert at last node
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():              # if list is not empty
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n    
        else:                                # if list is empty
            self.start=n
            
# Search a specified value in node
    def search(self,data):
        temp=self.start
        while temp.next is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
        
#insert after the specified value
    def insert_after(self,temp,data):   #assume search is already occure and get temp
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n

# print all the nodes
    def printlist(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
           
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next

    def delete_last(self):
        if self.start is None:
            pass                    #0 Node

        elif self.start.next is None :
            self.start=None     #1 Node

        else:
            temp=self.start             #More then one node
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

# delete specific value
    def delete_item(self,data):
        if self.start is None:
            pass                    #0 Node

        elif self.start.next is None and self.start.item ==data:
            self.start=None     #1 Node

        else:
            temp=self.start             
            if temp.item==data:         #More then one node and 1st variable is deleted
                self.start=temp.next
            else:
                while temp.next is not None :   #more then 1 nodes
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    def  __iter__(self):  #make iterable linklist
        return SLLIterator(self.start) # start is  node first reference
           

# Make datatype iterable
class SLLIterator:  #This is iterator class
    def __init__(self,start)            :
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data



    
# driver Code
mylist=SLL()
# mylist.is_empty()
mylist.insert_at_start(20)  #20
mylist.insert_at_start(10)  #10 20
mylist.insert_at_last(30)  #10 20 30
mylist.insert_after(mylist.search(20),25)  # 10 20 25 30
mylist.is_empty()
mylist.search(25)
mylist.delete_first()       # 20 25 30
mylist.delete_last()       # 20 25 
mylist.delete_item(20)      #20
mylist.printlist()
print()
print("using loop")
for i in mylist:   #25
    print(i)

