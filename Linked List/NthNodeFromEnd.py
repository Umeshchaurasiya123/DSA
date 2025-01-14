# remove the nth node from the end. 

from LinkedList import LinkedList 
from LinkedList import node

my_linked_list=LinkedList()

my_linked_list.append(11)
my_linked_list.append(22)
my_linked_list.append(33)
my_linked_list.append(44)
my_linked_list.append(55)


def removeNthFromEnd(head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        Dummy=node()
        Dummy.next=head

        left=Dummy
        right=head

        while n>0 and right is not None:
            n-=1
            right=right.next

        while right:
            right=right.next
            left=left.next
        
        left.next=left.next.next
        return Dummy.next


new_head=removeNthFromEnd(my_linked_list.head,3)

# my_linked=LinkedList()
# my_linked.head=my_linked_list.head
# my_linked.display()

my_linked_list.display()

