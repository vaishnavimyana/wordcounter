#sentence:This is a project to create a word counter which counts number of words in a given sentence
def count_words(text):
    words = text.split()
    return len(words)

def main():
    user_input = input("Enter a sentence to count the number of words: ").strip()
    if not user_input:
        print("Input cannot be empty. Please try again.")
    else:
        word_count = count_words(user_input)
        print(f"The number of words in the given text is: {word_count}")
if __name__ == "__main__":
    main()