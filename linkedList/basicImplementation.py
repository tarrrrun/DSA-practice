class Node:
    def __init__(self,k):
        self.key = k
        self.next=None

class NewNode:
    def __init__(self,k):
        self.key=k
        self.next = None
    
def countNodes(head):
    count = 0
    curr = head
    while curr:
        count+=1
        curr = curr.next
    return count

def addAtBeginning(head,x):
    if head==None:
        return Node(x)
    temp = Node(x)
    temp.next = head
    return temp
def traverseLL(head):
    l=[]
    if head == None:
        l.append(None)
        return l
    if head.next==None:
        l.append(head.key)
        return l
    while head.next!=None:
        l.append(head.key)
        head=head.next
    return l

def insertAtPosition(head,pos,k):
    temp=Node(k)
    if head==None:
        return temp
    curr=head
    for i in range (pos-1):
        curr=curr.next
        if curr==None:
            return head
    temp.next=curr.next
    curr.next=temp
    return head

def deleteFirstNode(head):
    if head==None:
        return None
    temp = head.next
    head = temp
    return head


def deleteAtPosition(head,pos):
    if head==None:
        return None
    if head.next == None:
        return head
    curr = head
    while pos>2:
        curr = curr.next
        if curr == None:
            return head
        pos-=1
    
    curr.next = curr.next.next
    return head


def sortedInsertion(head,x):
    if head == None:
        return None
    if head.key>x:
        temp = Node(x)
        temp.next=head
        return temp
    curr = head
    
    while curr!= None and curr.key<x:
        curr=curr.next
    temp = Node(x)
    if curr.next.next==None:
        temp.next = curr.next
        curr.next=temp
    else:
        temp.next=curr.next.next
        curr.next=temp
        return head

def reversLLUsingStack(head):
    stack=[]
    curr = head
    while curr is not None:
        stack.append(curr.key)
        curr=curr.next
    curr=head
    while curr is not None:
        curr.key = stack.pop()
        curr=curr.next
    return head

def reverseLLUsingRecursion(curr,prev=None):
    if curr ==None:
        return prev
    next= curr.next
    curr.next = prev
    return reverseLLUsingRecursion(next,curr)

def reverseLLUsingTraversal(head):
    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next=prev
        prev = curr
        curr = next
    return prev
    


if __name__ == '__main__':
    head=Node(None)
    head=addAtBeginning(head,6)
    head=addAtBeginning(head,12)
    head=addAtBeginning(head,18)
    head=addAtBeginning(head,24)
    head=addAtBeginning(head,30)
    print(head.key)
    print(*traverseLL(head))
    insertAtPosition(head,4,11)
    print(*traverseLL(head))
    head=deleteFirstNode(head)
    head=deleteFirstNode(head)
    print(*traverseLL(head))
    head=addAtBeginning(head,24)
    head=addAtBeginning(head,30)
    print(*traverseLL(head))
    deleteAtPosition(head,4)
    print(*traverseLL(head),"    Deleted at pos = 4")
    # print(*traverseLL(head))
    revv = (reversLLUsingStack(head))
    print(*traverseLL(revv))
    head = reverseLLUsingTraversal(head)
    print(*traverseLL(head))