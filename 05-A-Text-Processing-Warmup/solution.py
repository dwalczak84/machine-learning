def a_text_processing_warmup(s):
    
    import re
    pattern_a = r'[^A-Za-z0-9]+a[^A-Za-z0-9]+|[^A-Za-z0-9]+A[^A-Za-z0-9]+'
    pattern_an = r'[^A-Za-z0-9]+an[^A-Za-z0-9]+|[^A-Za-z0-9]+An[^A-Za-z0-9]+'
    pattern_the = r'[^A-Za-z0-9]+the[^A-Za-z0-9]+|[^A-Za-z0-9]+The[^A-Za-z0-9]+|The'
    pattern_dates = r'[0-9]{1,} [A-Z]{1}[a-z]+ [0-9]{2,}|[0-9]{2}\/[0-9]{1,}\/[0-9]{2,}|[A-Z][a-z]+ [0-9]{1,}\, [0-9]{2,}\,|[0-9]{1,}th of [A-Z][a-z]+ [0-9]{2,}|[0-9]{1,}rd of [A-Z][a-z]+ [0-9]{2,}|[0-9]{1,}nd of [A-Z][a-z]+ [0-9]{2,}|[0-9]{1,}st of [A-Z][a-z]+ [0-9]{2,}'
    A = [len(re.findall(pattern_a , s))] + [len(re.findall(pattern_an , s))] + [len(re.findall(pattern_the , s))] + [len(re.findall(pattern_dates , s))]
    return A


T = int(raw_input())
for i in range(2 * T + 1):
    try:
        s = raw_input()
        if s == '':
            continue
        else:
            for i in a_text_processing_warmup(s): print i
    except EOFError:
        break
