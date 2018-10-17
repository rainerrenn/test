#Katse editeerida Browserist

def most_unique(string):
    list = string.split()
    '''for i in range(len(list)):
        for j in list:
            if j not in list:
                list.append(j)'''
    for i in range(len(list)):
        sona_mida_analuusime = list[i]
        unikaalsed_tahed = []
        for j in range(len(sona_mida_analuusime)):
            if sona_mida_analuusime[j] not in unikaalsed_tahed:
                unikaalsed_tahed.append(sona_mida_analuusime[j])
        print(list)

        
        
        
        
'''   
    if (len(list[0])) > (len(list[1])) and (len(list[1])) > (len(list[2])):
        biggest = (list[0])
    elif (len(list[1])) > (len(list[0])) and (len(list[1])) > (len(list[2])):
        biggest = (list[1])
    else:
        biggest = (list[2])
    print(biggest)
'''
most_unique('expectation expect j')
