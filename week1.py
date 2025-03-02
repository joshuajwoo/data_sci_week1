def fibo(n):
    first = 1
    second = 1
    count = 0
    while count < n:
        print(first)
        first, second = second, first + second
        count += 1
def odd_indices(lst):
    for elem in range(1, len(lst), 2):
        print(lst[elem])
def count_words(words):
    ht = {}
    lst_words = words.split()
    for i in lst_words:
        if i not in ht:
            ht[i] = None
    return len(ht)
def count_vowels(word):
    count = 0
    for let in word:
        if let in "aeiou":
            count += 1
    return count
def caps_animals(lst):
    for elem in lst:
        print(elem.upper())
def one_to_twnety():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
def sum_of_integers(a, b):
    return a + b
def main():
    fibo(10)
    odd_indices([1, 2, 3, 4, 5])
    print(count_words("I have provided this text to provide "
                "tips on creating interesting paragraphs. "
                "First, start with a clear topic sentence "
                "that introduces the main idea. Then, support"
                " the topic sentence with specific details, "
                "examples, and evidence. Vary the sentence length "
                "and structure to keep the reader engaged. "
                "Finally, end with a strong concluding sentence "
                "that summarizes the main points. Remember, "
                "practice makes perfect!"))
    print(count_vowels("data science"))
    caps_animals(['tiger', 'elephant', 'monkey', 'zebra', 'panther'])
    one_to_twnety()
    print(sum_of_integers(1, 2))
main()