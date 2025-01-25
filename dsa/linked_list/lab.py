from dsa.linked_list.singly_linked_list import SinglyLinkedList

# LAB
words = SinglyLinkedList()
words.append("hello")
words.append("ham")
words.append("spam")
current = words.tail

for w in words.iter():
    print(w)

print('delete hello')
words.delete('hello')
# words.delete('ham')

for w in words.iter():
    print(w)

