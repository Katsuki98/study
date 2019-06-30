def get_even_list(l):
    l_new = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l_new.append(l[i])
    return l_new

l_new = get_even_list([1,4,5,-1,10])
print(l_new)