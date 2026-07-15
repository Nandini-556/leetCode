class Solution(object):
    def findLucky(self, arr):
       

        frequency = {}

        for number in arr:
            frequency[number] = frequency.get(number, 0) + 1

        lucky_number = -1

        for number in frequency:
            if number == frequency[number]:
                lucky_number = max(lucky_number, number)

        return lucky_number