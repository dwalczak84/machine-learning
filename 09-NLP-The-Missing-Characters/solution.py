import urllib2

corpus_url = 'http://hr-testcases.s3.amazonaws.com/1307/assets/corpus.txt'

A = []
resp = urllib2.urlopen(corpus_url).read()
resp = resp.split('\n')

# read the corpus data
for line in resp:
    A.append(line)

# preprocess the data
B = [''.join([i for i in j if ord(i) in [32] + range(65, 123)]).strip('\r') for j in A]
C = []
for i in B:
    if i:
        C.extend(i.split())

D = list(set(C))

max_length = max(map(len, D))

# create dict with keys as unique lengths of strings from preprocessed corpus
# data
E = {i: [] for i in range(1, max_length + 1)}

for i in D:
    E[len(i)].append(i)
    
# find the missing character in string s based on corpus data
def the_missing_characters(s):
    l = len(s)
    idx = s.index('#')
    tmp = []
    for i in E[l]:
        tmp.append(i)
        
    F = map(list, tmp)
    G = []

    for i in F:
        i[idx] = '#'
        G.append(''.join(i))   

    for i, j in enumerate(G):
        if j == s:
            print E[l][i][idx], j
        

T = raw_input()

for i in T.split():
    if '#' in i:
        the_missing_characters(i)
