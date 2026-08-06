# Check for Disjoint Arrays or Sets

def areDisjoint(a, b):
    st = set()

    for ele in a:
        st.add(ele)

    for ele in b:

        if ele in st:
            return False
    return True

a = [12, 34, 11, 9, 3]
b = [7, 2, 1, 5]

if areDisjoint(a, b):
    print("True")
else:
    print("False")