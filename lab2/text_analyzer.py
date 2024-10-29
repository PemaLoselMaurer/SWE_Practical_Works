import collections
# Open and Read txt file
def read_file(filename):
    with open("./sample.txt", 'r', encoding="utf-8") as file:
        return file.read()
content = read_file('sample.txt')
print(content) 

# Counting Number of lines
def count_lines(content):
    return len(content.split('\n'))
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

# Counting Words
def count_words(content):
    return len(content.split())
num_words = count_words(content)
print(f"Number of words: {num_words}")

# Average Word Length
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

# Most Common Word
def most_common_word(content):
    words = content.lower().split() 
    word_counts = collections.Counter(words) 
    common_word, count = word_counts.most_common(1)[0] 
    return common_word, count

# Combine all to main
def analyze_text(filename):
    content = read_file(filename)
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
analyze_text('sample.txt')

# Count Number of Unique words in texts
def count_unique_words(text):
    words = text.split()
    unique_words = set(words) 
    return len(unique_words)
text = "This is a sample text for testing. Modify the program to count the number of unique words in the text."
unique_word_count = count_unique_words(text)
print(f"Number of unique words: {unique_word_count}")

# Longest word in text
def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)  
longest_word = find_longest_word(text)
print(f"Longest word: {longest_word}")

# the Occurance of specific word
def count_word_occurrences(text, specific_word):
    words = text.lower().split() 
    specific_word = specific_word.lower()
    return words.count(specific_word)
occurrences = count_word_occurrences(text, 'the')
print(f"Occurrences of 'the': {occurrences}")

# % of Words Longer than Average Length
def percentage_words_longer_than_average(text):
    words = text.split()
    word_lengths = [len(word) for word in words]
    average_length = sum(word_lengths) / len(word_lengths)  # Calculate the average word length
    longer_than_average = [word for word in words if len(word) > average_length]
    percentage = (len(longer_than_average) / len(words)) * 100  # Calculate the percentage
    return percentage
percentage_longer_than_average = percentage_words_longer_than_average(text)
print(f"Percentage of words longer than the average length: {percentage_longer_than_average:.2f}%")