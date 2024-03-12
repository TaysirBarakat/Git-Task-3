# Initialise the loop
while True:

    # Prompt the user to enter a sentence or end the program
    sentence = input("Please enter a sentence to be printed, or type \"End\" \
to end the program.")

    # Check if the loop should be exited
    if sentence == "End":
        break

    # Prints the sentence
    else:
        print(sentence)
