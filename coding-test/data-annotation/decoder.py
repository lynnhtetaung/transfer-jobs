def decoder(message_file):
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

    # Extract words at the end of each pyramid line
    decoded_message = ' '.join(pyramid[level][-1] for level in sorted(pyramid.keys()))

    # Print the end of each line with their corresponding numbers and words
    for level, words in sorted(pyramid.items()):
        print(f"Line {level}: {level * (level + 1) // 2} {words[-1]}")

    return decoded_message

# Test the combined function with the input file
decoded_message = decoder('encode_message.txt')
print("\nDecoded Message:", decoded_message)

