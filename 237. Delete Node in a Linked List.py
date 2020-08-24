ListNode = self.head

if ListNode and ListNode.val == node:
    self.head = ListNode.next
    ListNode = None
    return

prev = None
while ListNode and ListNode.val != node:
    prev = ListNode
    ListNode = ListNode.next
if ListNode == None:
    return
prev.next = ListNode.next
ListNode = None