class LinkedList:
    def __init__(self, nodes=None) -> None:
        self.head = None
        if nodes != None:
            node = Node(str(nodes.pop(0)))
            self.head = node
            for elem in nodes:
                node.next = Node(data=str(elem))
                node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node != None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")        
        return " -> ".join(nodes)

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None
    def __repr__(self) -> str:
        return self.data
    
example = [1,2,3,4]
llist = LinkedList(example)
print(llist)