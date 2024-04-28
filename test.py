def count_words(text):
    # Split the text into words
    words = text.split()
    
    # Count the number of words
    num_words = len(words)
    
    return num_words

def main():
    # Get input text from the user
    text = input("Enter some text: ")
    
    # Call the count_words function
    num_words = count_words(text)
    
    # Display the result
    print("Number of words:", num_words)

if __name__ == "__main__":
    main()
