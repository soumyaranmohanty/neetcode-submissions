# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1= list1
        head2 = list2
        dummy=ListNode(0)
        curr=dummy
        
        while (head1 and head2):
            print(head1.val, " ", head2.val)
            if head1.val<=head2.val:
                curr.next=head1
                head1=head1.next

            else:
                curr.next=head2
                head2=head2.next
            curr=curr.next
        # print(head1)
        # print(head2)
        # print(curr)
        # print(curr.val)
        if head1 is not None:
            curr.next=head1
        if head2 is not None:
            #print("Head 2 i not null")
            curr.next=head2

        return dummy.next
                



        