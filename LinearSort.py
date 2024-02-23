
nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]


def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if anArray[i] == item:
            return i
    return -1

print(linearSearch(nums, 100))
print(linearSearch(nums, 75))
print(linearSearch(words, "fish"))
print(linearSearch(words, "at"))
print(linearSearch(unsorted, 70))