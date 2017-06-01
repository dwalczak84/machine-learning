# list of 5000 common words:
url = 'https://s3.amazonaws.com/hr-testcases/479/assets/words.txt'

# list for 5000 common words:
words = []

with open('words.txt', 'r') as t_in:
    for line in t_in:
        words.append(line.strip('\n'))

words.sort(lambda y, x: cmp(len(x), len(y)))

# number of test cases:
T = int(raw_input())

# list for the input data:
S = []

for _ in range(T):
    s = raw_input()
    S.append(s)

# preprocess the input data:

# cut the suffixes:
A = []
for i in S:
    tmp = []
    for j in i:
        if ord(j) in range(65, 123) + [46]:
            tmp.append(j)
    A.append(''.join(tmp))

# cut the webpage suffixe parts
C = []
for i in A:
    C.append(i.split('.')[0])

def deterministic_Url_and_hashTag_segmentation(s):
    
    ss = s
    output = []
    indexes = []
    result = []

    for i in words:
        if i in s:
            idx = s.index(i)
            output.append(i)
            s = s[:idx] + s[idx + len(i):]

    if not s:
        if not output:
            return s
        for i in output:
            indexes.append(ss.index(i))
        
        B = zip(output, indexes)
        B.sort(key = lambda x: x[1])
    
        for i in B: 
            result.append(i[0])
        
        return result
    
    else:
        for i in output:
            indexes.append(ss.index(i))
        
        try:
            indexes.append(ss.index(s))
            B = zip(output + [s], indexes)
            B.sort(key = lambda x: x[1])
        except:
            B = zip(output, indexes)
            B.sort(key = lambda x: x[1])
        
        for i in B: 
            result.append(i[0])
        
        return result

for s in C:
    print deterministic_Url_and_hashTag_segmentation(s)
    
