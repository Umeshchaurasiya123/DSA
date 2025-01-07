

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class LinkedList:

    def __init__(self):
        self.head=node()   
       

    
    def append(self,data):

        new_node=node(data)
        cur=self.head

        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total
        
    def display(self):
        elements=[]
        cur=self.head
        while cur.next!=None:
            cur=cur.next
            elements.append(cur.data)
        print(elements)




myLinked_List=LinkedList()

myLinked_List.append(10)
myLinked_List.append(20)
myLinked_List.append(30)
myLinked_List.append(40)
myLinked_List.append(50)

myLinked_List.display()

print(myLinked_List.length())







        
