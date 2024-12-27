# Name: 류동우
# Date: 2022-05-15

def add(x, A):
    	# Set A 에 x 를 추가하는 함수
	# 단, 아무것도 리턴하지 않는다
	if x in A:
		return
	else:
		A.append(x)
	return
		

def remove(x, A):
	# Set A 에서 x 를 제거하는 함수
	# 단, 아무것도 리턴하지 않는다
	if x in A:
		A.remove(x)
	return

def make_set(A):
    B = []
    # List A를 받아 중복된 원소를 제거하여 List B 를 리턴하는 함수
    # 즉, 이 함수의 리턴값은 A를 Set으로 만든 것이 된다
    for x in A:
        if x in B:
            continue
        else:
            B.append(x)
    return B

def union(A, B):
    return make_set(A+B)

def intersection(A, B):
    C = []
    for x in A:
        if x in B:
            C.append(x) 
    return C

def difference(A, B):
    C = list(A)
    for x in B:
        if x in C:
            C.remove(x)
    return C
    
def is_subset(A, B):
    if len(difference(A, B)) == 0:
        return True
    return False

def find(x, A):
    C = []
    for y in A:
        if x in y:
            C.append(y)
    return C

def get_subsets(A):
    C = []
    a = len(A)
    '''
    모든 부분집합을 구한다는 것은 각 요소가 포함(1), 미포함(0)되는 모든 경우를 따진다는 것.
    A에게 3개의 요소가 있다면 8개의 부분집합이 나오게 된다.
    3개의 요소 중 어느 요소가 포함되느냐 미포함되느냐를 표현하기 위해
    000부터 111까지 즉, 0부터 7까지를 2진수로 표현하고, 각 자리의 수(0 또는 1)를 각 요소의 포함 여부와 결부시킨다.
    예로 000은 공집합, 111은 A자체를 나타내는 것.
    '''
    for x in range(2**a):
        D = []
        for y in range(a):
            if format(x, 'b').zfill(a)[y] == '1':
                D.append(A[y])
        C.append(D)
    return C

def equals(A, B):
    if (len(difference(A, B))==0) & (len(difference(B, A))==0):
        return True
    return False
            
def is_disjoint(A, B):
    if len(intersection(A, B)) == 0:
        return True
    return False

def cartesian_product(A, B):
    C = []
    for x in A:
        for y in B:
            C.append((x, y))
    return C

def symmetric_difference(A, B):
    return difference(A, B) + difference(B, A)

def intersection3(A, B, C):
    return intersection(intersection(A, B), C)

def union3(A, B, C):
    return union(union(A, B), C)

def symmetric_difference3(A, B, C):
    return symmetric_difference(symmetric_difference(A, B), C)


def format_set(A):
	# Set 출력 포맷으로 만들어서 리턴하는 함수
	# 이미 완성되어 있으므로 수정하지 않는다
	B = []
	for x in A:
		B.append('"' + x + '"')
	return "{" + ", ".join(B) + "}"

def run(A, B):
	# 1) 부터 15) 까지 출력하는 함수
	print('=' * 20)
	print("A = " + format_set(A))
	print("B = " + format_set(B))
	print("Union of A and B = " + format_set(union(A, B)))
	print("Intersection of A and B = " + format_set(intersection(A, B)))
	print("A - B = " + format_set(difference(A, B)))
	print("B - A = " + format_set(difference(B, A)))
	print("Symmetric difference of A and B = ", format_set(symmetric_difference(A, B)))
 
	print("List of cartesian product of A and B:")
	for elem in cartesian_product(A, B):
		print(format_set(elem), end=' ')
	print()
 
	print("List of cartesian product of B and A:")
	for elem in cartesian_product(B, A):
		print(format_set(elem), end=' ')
	print()
 
	if is_subset(A, B):
		print("A is a subset of B")
	else:
		print("A is not a subset of B")
	if is_subset(B, A):
		print("B is a subset of A")
	else:
		print("B is not a subset of A")

	print("Find \"c\" in A = " + format_set(find("c", A)))
 
	print("List of get_subsets of A:")
	for subset in get_subsets(A):
		print(format_set(subset), end = ' ')
	print()


	if equals(A, B):
		print("A == B")
	else:
		print("A != B")
	if is_disjoint(A, B):
		print("A and B are disjoint")
	else:
		print("A and B are not disjoint")
	print('=' * 20)

def run3(A, B, C):
    # 1) 부터 8) 까지 출력하는 함수
	print('=' * 20)
	print("A = " + format_set(A))
	print("B = " + format_set(B))
	print("C = " + format_set(C))
	print("Union of A, B and C = " + format_set(union3(A, B, C)))
	print("Intersection of A, B and C = " + format_set(intersection3(A, B, C)))
	print("Symmetric difference of A, B and C = ", format_set(symmetric_difference3(A, B, C)))
 
	if is_subset(A, union(B, C)):
		print("A is a subset of union of B and C")
	else:
		print("A is not a subset of union of B and C")
  
	if is_subset(intersection(B, C), A):
		print("Intersection B and C is a subset of A")
	else:
		print("Intersection B and C is not a subset of A")
	print('=' * 20)
 

A = make_set(input("Input your set A elements:\n").split())
B = make_set(input("Input your set B elements:\n").split())
C = make_set(input("Input your set C elements:\n").split())

run(A, B)
add("computer", A)
remove("python", B)
run(A, B)

run3(A, B, C)
add("computer", C)
remove("c", B)
run3(A, B, C)