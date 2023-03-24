import os

# Minimum Cover Algorith but only for k=2
def min_cover_alg(set_s, collection_c,value_k):


    print("EJERCICIO 3")
    print("----------------------------------")

    found_s=False
    solution_set_one=[]
    solution_set_two=[]
    for x in range(len(collection_c)):
        if found_s: break
        for y in range(len(collection_c)):
            if found_s: break
            if compare_lists((collection_c[x].split(",") + collection_c[y].split(",")), set_s):
                found_s=True
                solution_set_one=collection_c[x].split(",")
                solution_set_two=collection_c[y].split(",")

    if found_s:
        print("SI")
        print(set_s)
        print(solution_set_one)
        print(solution_set_two)
    else : print("NO")


def compare_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if set1 == set2:
        return True
    else:
        return False


# def remove_duplicates(lst):
#     return list(set(lst))
