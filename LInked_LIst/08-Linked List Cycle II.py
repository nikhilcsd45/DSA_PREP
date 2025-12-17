def detectCycle(self, head):
    slow=head
    fast=head

    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next

        if slow== fast:
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow