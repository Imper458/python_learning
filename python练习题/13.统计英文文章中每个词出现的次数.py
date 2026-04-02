import re
def summerize_words():
    lines = []
    words = []
    times = {}
    with open('./English_paper.txt', 'r') as f:
        for line in f.readlines():
            line = line[:-1]
            lines.append(line)
            split_words = re.split(r'[ .]+', lines[-1])
            for word in split_words:
                words.append(word)
        # print(f'words:{words}')

        for word in words:
            if word in times:
                times[word] += 1
            else:
                times[word] = 1
        return times

print(summerize_words())
result = sorted(
    summerize_words().items(),
    key=lambda x: x[1],
    reverse=True
)

print(result)


