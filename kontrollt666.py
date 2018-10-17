
# VARIANT 3


#Ülesanne 1

def synad(sisend):    
    return (sisend.append("tere"))

sisend
    a,b,c,d =["ahha", "see", "oli", "tema"]
    a1 = a[::-1]
    if a1==a:
    synad.append(1)
    a=synad
    b1 = b[::-1]
    if b1==b:
    synad.append(2)
    c1 = c[::-1]
    if c1==c:
     synad.append(3)
    d1 = d[::-1]
    if d1==d:
    synad.append(4)
s6nad()

'''
print(synad(["ahha", "see", "oli", "tema"]))
'''
# Ülesanne 2

var = input("Meeste arv linnas: ")
x = int(var)
meeste_arv = x
naiste_arv = meeste_arv * x
laste_arv = naiste_arv * x
rahvastik = meeste_arv + naiste_arv + laste_arv
print(str("Rahvaarv kokku linnas: ") + str(rahvastik))


# Ülesanne 3

def most_unique(string):
    list = string.split()
    lists=[]
    for i in range(len(list)):
       sona_mida_analuusime = list[i]
       unikaalsed_tahed = []
       lists.append(unikaalsed_tahed)
       for j in range(len(sona_mida_analuusime)):
           if sona_mida_analuusime[j] not in unikaalsed_tahed:
               unikaalsed_tahed.append(sona_mida_analuusime[j])
    
    ssss = set(lists[0]+lists[1])
    return ssss

print(most_unique('expectation expect'))






