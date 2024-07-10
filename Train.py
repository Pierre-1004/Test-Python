
def reverse_int(nb):
    sign = nb // abs(nb)
    print(sign)

    return int(str(abs(nb))[::-1])*sign

#nombre = int(input())
#print(reverse_int(nombre))

#maliste = [1,2,3,4,5,6,7,8,9]
#print("maliste[::]", maliste[::])
#print("maliste[::-1]", maliste[::-1])
#print("maliste[:-1]", maliste[:-1])
#print("maliste[-1::]", maliste[-1::])
#print("maliste[-1:]", maliste[-1:])
#print("maliste[-3:]", maliste[-3:])
#print("maliste[-3::]", maliste[-3::])
#print("maliste[:-2]", maliste[:-2])
#print("maliste[::-2]", maliste[::-2])


liste = [0,3,6,1,2,4,5]

def triplet_abc(liste_triplet):
    result =[]
    liste_triplet.remove(0)
    for i in range(len(liste_triplet)):
        for j in range(len(liste_triplet)):
            for k in range(len(liste_triplet)):
                if liste_triplet[i]*liste_triplet[i] + liste_triplet[j]*liste_triplet[j] == liste_triplet[k]*liste_triplet[k] :
                    result.append([liste_triplet[i],liste_triplet[j],liste_triplet[k]])

    return result

#print(triplet_abc(liste))




##################"
#Longueur moyenne des mots

phrase = "Même les phrases avec des caractères de la langue française peuvent être utilisées."

def average_word (input):

    for ponctuation in ",.?;/:!'":
        input = input.replace(ponctuation, ' ')
    words = input.split(" ")
    return round(sum(len(word) for word in words)/len(words),2)

#print(average_word(phrase))


################################################
#Suite de fibonacci

def search_fibbo(min,max):
    liste= []
    scope = max-min +1
    for i in range(scope):
        liste.append(min+i)


    return liste

print(search_fibbo(5,15))
