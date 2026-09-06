from DSA.Collections.Queue.Queue import Queue
from DSA.Node.LinearNode import LinearNode


"""
    An example of using a queue to encrypt a message using a simple Caesar cipher.

    It's a simple implementation of a queue to demonstrate how to use a queue to store and manipulate data.
    When shifting characters in the message, we wrap around the alphabet using modulo 26. 
    This means that if we shift a character beyond 'Z' or 'z', we start back at 'A' or 'a' respectively.
    Any non-alphabetic characters in the message are not encrypted and are added to the queues as-is.
"""
def main() -> None:

    # Create two queues. One for the de-crypted message and one for the encrypted message.
    decrypted_queue: Queue = Queue()
    encrypted_queue: Queue = Queue()

    # Define the message to be encrypted.
    message: str = "Musty Zebras!"

    # Define a constant to shift the characters in the message.
    shift: int = 3

    # Perform encryption by iterating through each character in the message.
    # Also stores decrypted characters in a separate queue for demonstration purposes.
    for char in message:

        # Only want to encrypt alphabetic characters. Non-alphabetic characters are added to the queues without encryption.
        if not char.isalpha():
            decrypted_queue.enqueue(LinearNode(char))
            encrypted_queue.enqueue(LinearNode(char))
            continue

        # Enqueue the character to the decrypted queue.
        decrypted_queue.enqueue(LinearNode(char))

        # Wrap within the current alphabet using modulo 26. Need to know if its uppercase or lowercase 
        # to determine the starting point of the alphabet.
        # Example: Z shifted by 2 becomes B, and z shifted by 2 becomes b.

        # Get the starting point of the alphabet based on the case of the character.
        alphabet_start: int = ord("A") if char.isupper() else ord("a")

        # Encrypt the character by shifting it and wrapping around the alphabet if necessary.
        encrypted_char: str = chr(
            alphabet_start + (ord(char) - alphabet_start + shift) % 26
        )
        encrypted_queue.enqueue(LinearNode(encrypted_char))


    # Print string outputs of both queues
    print(f"Decrypted Queue: {decrypted_queue.to_string()}")
    print(f"Encrypted Queue: {encrypted_queue.to_string()}")

    return


if __name__ == "__main__":
    main()