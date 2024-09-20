class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

    def append(self, data):
        new_node = Node(data)  
        if self.head is None:  
            self.head = new_node
            return
        last_node = self.head 
        while last_node.next: 
            last_node = last_node.next
        last_node.next = new_node  

    def print_list(self):
        current_node = self.head  
        while current_node:  
            print(current_node.data, end=" -> ")  
            current_node = current_node.next  
            print("None")  

def count_nodes(linked_list):
    count = 0 
    current_node = linked_list.head  
    while current_node:  
        count += 1  
        current_node = current_node.next  
    return count  
# Exemplo de uso
if __name__ == "__main__":
    linked_list = LinkedList() 
    linked_list.append(10) 
    linked_list.append(20)
    linked_list.append(30)

    print("Lista encadeada:")
    linked_list.print_list() 

    # Contador de nós
    total_nodes = count_nodes(linked_list)
    print("Número de nós na lista encadeada:", total_nodes)  