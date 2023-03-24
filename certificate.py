# importing the random module
import random
from itertools import combinations
from itertools import permutations
import decimal

def generate_random_certificate(set_s, collection_c, value_k):

    length_c=len(collection_c)

    certificado=[]
    missing_ones=value_k
    for x in range(length_c):
        if missing_ones==0:
            certificado.append(str(0))
        elif (length_c-x)==missing_ones:
            certificado.append(str(1))
            missing_ones=missing_ones-1
        else:
            certificado.append(str(random.randint(0, 1)))
            if certificado[-1]=="1":
                missing_ones=missing_ones-1

    print("El certificado generado es: \n")
    print(certificado)
    print("\n")


    # Code to get the probability of getting a certificate that belongs to the problem language with the exemplar
    # Get all combinations of collections_c in k
    comb = combinations(collection_c, value_k)

    validate_certificates = verifica_pertenencia(set_s, comb)
    ####FAlTA HACER FILTER DE LOS TRUE Y DE LOS FALSE PARA SACAR LA PROBABILIDAD
    filtered_list = filter(is_True, validate_certificates)
    # print(filtered_list)
    len1 = decimal.Decimal(len(filtered_list))
    len2 = decimal.Decimal(len(validate_certificates))

    probabilidad = len1/len2

    # Prints the probability
    print("La probabilidad de generar un certificado tal que se verifica la pertenencia al lenguaje: " + str(probabilidad))


    return certificado



# Function that verifies if every cerificate of a list of certificates belongs to the problems language.
def verifica_pertenencia(set_s, combinations):

    pertenencia_list=[]

    #Itarate through the combinations
    for i in combinations:
        # print (i)
        union_of_combinations=[]
        for j in i:
            union_of_combinations=union_of_combinations+j.split(",")
            # print(j)
        # print(union_of_combinations)
        if compare_lists(union_of_combinations, set_s):
            pertenencia_list.append(True)
        else:
            pertenencia_list.append(False)
    # print(pertenencia_list)
    return pertenencia_list


# Function that compares lists as sets
def compare_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if set1 == set2:
        return True
    else:
        return False
    
def is_True(bool):
    if(bool):
        return True
    else: 
        return False