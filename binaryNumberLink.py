class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def getNumber(binary):
    # Initialize an empty string to store the binary representation
    binary_str = ""

    # Traverse the linked list and build the binary string
    while binary is not None:
        binary_str += str(binary.data)
        binary = binary.next

    # Convert the binary string to a decimal number
    decimal_number = int(binary_str, 2)

    return decimal_number

# Example usage:
# Create a linked list representing a binary number, e.g., 1010
head = SinglyLinkedListNode(1)
head.next = SinglyLinkedListNode(0)
head.next.next = SinglyLinkedListNode(1)
head.next.next.next = SinglyLinkedListNode(0)

result = getNumber(head)
print(result)  # Output should be 10 (the decimal representation of 1010)
