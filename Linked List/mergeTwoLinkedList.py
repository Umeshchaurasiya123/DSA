from LinkedList import LinkedList 
from LinkedList import node

my_linked_list1=LinkedList()
my_linked_list2= LinkedList()

# Append elements to the linked list
my_linked_list1.append(10)
my_linked_list1.append(20)
my_linked_list1.append(30)
my_linked_list1.append(40)
my_linked_list1.append(50)

my_linked_list2.append(12)
my_linked_list2.append(15)
my_linked_list2.append(17)
my_linked_list2.append(19)
my_linked_list2.append(30)
my_linked_list2.append(32)
my_linked_list2.append(35)
my_linked_list2.append(45)
my_linked_list2.append(99)
my_linked_list2.append(199)



# Display the linked list
# my_linked_list.display()
# [10, 20, 30, 40]
# # Print the length of the linked list
# print("Length of the linked list:", my_linked_list.length())
# 4

def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # create an dummy node and  create a pointer which point to the currnet node. 

        Dummy=node()
        current=Dummy
       
        
        #  here [1,3,4] is basically means there is linked list of 3 element. 
        # list1 is kind a head which point to the first node and so on. 
        # None is treated as false. 
        # [] means there is no node. 
        # only head is avaialve with values stored as None. 
        # [0] means their  is  only one node head point to first element only. 
        
        while list1 is not None and list2 is not None:

            if(list1.data<=list2.data):
                current.next=list1
                current=list1
                list1=list1.next
            else:
                current.next=list2
                current=list2
                list2=list2.next
            

        if list1 is None :
            current.next=list2
        else:
            current.next=list1
            
        return Dummy.next


ans=mergeTwoLists(my_linked_list1.head,my_linked_list2.head)

mergeLinkedList=LinkedList()
mergeLinkedList.head=ans
mergeLinkedList.display()




