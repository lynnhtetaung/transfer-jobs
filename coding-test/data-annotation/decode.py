def decode(message_file):
    # Dictionary to store words in the pyramid structure
    pyramid = {}

    # Open the input file
    with open(message_file, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line into number and word
            num, word = line.split()
            # Convert the number to integer
            num = int(num)
            # Append the word to the corresponding level in the pyramid
            pyramid.setdefault(num, []).append(word)

    # Extract words at the end of each pyramid line (1, 3, 6 in this case)
    decoded_message = ' '.join(pyramid[i][-1] for i in [1, 3, 6] if i in pyramid)
    return decoded_message

# Test the decode function with the input file
decoded_message = decode('message.txt')
print("Decoded Message:", decoded_message)
