# Problem description:
# https://www.hackerrank.com/challenges/language-detection
import sys

def language_detection(s):
    
    s = ''.join(s.split('—'))
    s = s.split(' ')
    EN_count = 0
    FR_count = 0
    DE_count = 0
    ES_count = 0
    
    DE = ['der', 'die', 'und', 'den', 'von', 'zu', 'das', 'mit', 'sich', 'auf','f\xfcr', 'ist', 'im', 'dem', 'nicht', 'ein',  'Die', 
    'eine', 'als', 'auch', 'werden', 'aus', 'er', 'hat', 'da\xdf', 'sie', 'nach', 'wird', 'bei', 'einer', 'Der', 'um', 'am', 'sind', 
    'noch', 'wie', 'einem', '\xfcber', 'einen', 'Das', 'Sie', 'zum', 'war', 'haben', 'nur', 'oder', 'aber', 'vor', 'zur', 'bis', 
    'mehr', 'durch', 'man', 'sein', 'wurde', 'sei', 'In', 'Prozent', 'hatte', 'kann', 'gegen', 'vom', 'k\xf6nnen', 'schon', 'wenn', 
    'habe', 'seine', 'Mark', 'ihre', 'dann', 'unter', 'wir', 'soll', 'ich', 'eines', 'Es', 'Jahr', 'zwei', 'Jahren', 'diese', 
    'dieser', 'wieder', 'keine', 'Uhr', 'seiner', 'worden', 'Und', 'will', 'zwischen', 'Im', 'immer', 'Millionen', 'Ein', 'sagte']
    FR = ['de', 'le', 'et', 'les', 'une', 'est', 'pour', 'qui', 'dans', 'par', 'plus', 'pas', 'au', 'sur', 'ne', 'ce', 'il', 'sont', 
    'ou', 'avec', 'Il', 'aux', "d'unn", 'cette', "d'une", 'ont', 'ses', 'mais', 'comme', 'tout', 'nous', 'sa', 'Mais', 'fait', 
    '\xe9t\xe9', 'aussi', 'leur', 'bien', 'peut', 'ces', 'deux', 'A', 'ans', 'l', 'encore', "n'est", 'march\xe9', 'Pour', 'donc', 
    'cours', "qu'il", 'moins', 'sans', "C'est", 'Et', 'entre', 'Ce', 'faire', 'elle', "c'est", 'peu', 'vous', 'prix', 'On', 'dont', 
    'lui', '\xe9galement', 'Dans', 'effet', 'pays', 'cas', 'millions', 'Belgique', 'BEF', 'mois', 'leurs', 'taux', 'ann\xe9es', 
    'temps', 'groupe']
    EN = ['the', 'of', 'to', 'and', 'for', 'is', 'that', 'on', 'said', 'with', 'be', 'by', 'as', 'are', 'at', 'from', 'it', 'has',  
    'have', 'will', 'or', 'its', 'not', 'were', 'which', 'this', 'but', 'can', 'more', 'his', 'been', 'would', 'about', 'their', 
    'also', 'they', 'million', 'had', 'than', 'up', 'who', 'In', 'one', 'you', 'new', 'I', 'other', 'year', 'all', 'two', 'S', 
    'But', 'It', 'company', 'into', 'U', 'Mr.', 'system', 'some', 'when', 'out', 'last', 'only', 'after', 'first', 'time', 'says', 
    'years', 'market', 'no', 'over', 'we', 'could', 'if', 'people', 'percent', 'such', 'This', 'most', 'use', 'because', 'any', 
    'data', 'there', 'them', 'government', 'may', 'software', 'New', 'now', 'many']
    ES = ['y', 'el', 'los', 'no', 'las', 'del', 'por', 'con', 'una', 'lo', 'para', 'su', 'al', 'como', 'más', 'o', 'pero', 'me', 
    'ha', 'sus', 'si', 'yo', 'ya', 'este', 'porque', 'muy', 'todo', 'cuando', 'que', 'sin', 'sobre', 'está', 'también', 'esta', 
    'hay', 'sí', 'entre', 'ser', 'era', 'mi', 'dos', 'había', 'nos', 'años', 'tiene', 'hasta', 'desde', 'te', 'eso', 'fue', 
    'todos', 'puede', 'han', 'pues', 'así', 'bien', 'vez', 'ni', 'solo', 'él', 'ahora', 'uno', 'parte', 'ese', 'vida', 'tiempo', 
    'mismo', 'otro', 'día', 'cada', 'siempre', 'hacer', 'donde', 'esa', 'nada', 'hace', 'tan', 'entonces', 'decir', 'bueno', 
    'otra', 'esto', 'después', 'ella', 'mundo', 'tanto', 'otros', 'que']

    for i in s:
        if i in EN:
            EN_count += 1
        elif i in DE:
            DE_count += 1
        elif i in FR:
            FR_count += 1
        elif i in ES:
            ES_count += 1
        else:
            continue

    A = [EN_count, FR_count, DE_count, ES_count]
    B = ['English', 'French', 'German', 'Spanish']
        
    return B[A.index(max(A))]
    
# read input
text = []
while True:
    input_ = sys.stdin.readline()
    text.append(input_)
    if input_ == '':
        break

text = ' '.join(list(text[:-1]))
print language_detection(text)
