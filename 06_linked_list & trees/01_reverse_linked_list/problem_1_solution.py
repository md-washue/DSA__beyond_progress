
def reverse_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


class LinkList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = LinkList(1)
head.next = LinkList(2)
head.next.next = LinkList(3)

new_head = reverse_list(head)

current = new_head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next

print("None")
