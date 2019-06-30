sent = input('Your sentence: ').lower()
def count_dict(sent):
    afb = {}

    for i in sent: 
        afb[i] = sent.count(i)
    for j in sorted(afb):
        print (j,': ',str(afb[j]))


count_dict(sent)