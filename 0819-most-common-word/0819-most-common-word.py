class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned_words = set(banned)
        frequency = {}

        cleaned = ""

        for character in paragraph:
            if character.isalpha():
                cleaned += character.lower()
            else:
                cleaned += " "

        for word in cleaned.split():
            if word not in banned_words:
                frequency[word] = frequency.get(word, 0) + 1

        most_common = ""
        highest_frequency = 0

        for word in frequency:
            if frequency[word] > highest_frequency:
                highest_frequency = frequency[word]
                most_common = word

        return most_common