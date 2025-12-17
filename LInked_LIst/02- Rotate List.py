def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # Count length of list
        curr = head
        count = 1
        while curr.next:
            curr = curr.next
            count += 1
        
        # Handle if k >= count
        k = k % count
        if k == 0:
            return head
        
        # Move to (count - k - 1) position
        curr = head
        for _ in range(count - k - 1):
            curr = curr.next
        
        # new head will be curr.next
        newhead = curr.next
        curr.next = None
        
        # Find the end of new list and connect it to old head
        tail = newhead
        while tail.next:
            tail = tail.next
        
        tail.next = head
        head = newhead
        
        return head
