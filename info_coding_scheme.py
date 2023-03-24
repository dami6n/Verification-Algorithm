import os


def print_coding_scheme_info(set_s, collection_c, value_k, certificate):



    print("EJERCICIO 2")
    print("----------------------------------")


    # Prints the first and last 5 elements of the set "S"
    # if len(set_s) < 10:
    # print("Numero de elemetos de nuestro universo S: " + len(set_s))
    # print("----------------------------------")


    # Prints number of subsets of collection "C"

    print("Numero de miembros de C: ")
    print(len(collection_c))
    print("----------------------------------")

    #Prints value of "k"
    print("Valor de k: ")
    print(value_k)
    print("----------------------------------")

    #Prints coding scheme of first element of "C"
    print("El ejemplar, con el certificado dado, satisface la condicion de pertenencia al lenguaje correspondiente")
    union=[]
    for x in range(len(certificate)):
        if certificate[x]=='1':
            union = union + collection_c[x].split(",")

    if compare_lists(union, set_s):
        print("Satisface la condicion de pertenencia")
    else:
        print("NO satisface la condicion de pertenencia")

    # print(union)



def compare_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if set1 == set2:
        return True
    else:
        return False




