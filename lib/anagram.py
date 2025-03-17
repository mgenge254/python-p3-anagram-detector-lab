# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        sorted_word = sorted(self.word)
        return [word for word in word_list if sorted(word.lower()) == sorted_word and word.lower() != self.word]

# Example usage:
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))  # Output: ['inlets']
