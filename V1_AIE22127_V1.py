# Q1)
def find_pairs(input_list):
    pairs = []

    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] + input_list[j] == 10:
                pairs.append((input_list[i], input_list[j]))

            for k in range(j + 1, len(input_list)):
                if input_list[i] + input_list[j] + input_list[k] == 10:
                    pairs.append((input_list[i], input_list[j], input_list[k]))

    return pairs

user_List = [2,7,4,1,3,6]

result_pairs = find_pairs(user_List)

print(f"Q1) The pairs in the list {user_List} that form a sum of 10 are as follows:\n{result_pairs}")

# Q2)
def findingRange(input_list):
    if len(input_list) < 3:
        print("ERROR: Range determination not possible.")
        return

    min_value = input_list[0]
    max_value = input_list[0]

    for value in input_list:
        if value < min_value:
            min_value = value
        elif value > max_value:
            max_value = value

    final_Range = max_value - min_value
    print(f"Q2) The range of the list is {final_Range}")

user_list = []
n = int(input("Enter the size of the list: "))
print("Enter the values inside the list:")
for a in range(n):
    value = float(input(f"Enter the {a + 1}th element of the list: "))
    user_list.append(value)

print(f"Q2) The current list includes elements: {user_list}")
findingRange(user_list)

# Q3)
def matrix_mult(A, B):
    result = []
    for i in range(len(A)):
        rows = []
        for j in range(len(B[0])):
            sum_value = 0
            for k in range(len(B)):
                sum_value += A[i][k] * B[k][j]
            rows.append(sum_value)
        result.append(rows)
    return result

def power_mult(A, m):
    result = [row[:] for row in A]
    for _ in range(m - 1):
        result = matrix_mult(result, A)
    return result

def create_matrix(rows, columns):
    matrix = []
    print("Enter the values inside the matrix:")
    
    for _ in range(rows):
        row = []
        for _ in range(columns):
            value = int(input())
            row.append(value)
        matrix.append(row)
    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def Matrix():
    rows = int(input("Enter the rows of the matrix: "))
    columns = int(input("Enter the columns of the matrix: "))
    
    A = create_matrix(rows, columns)

    print("Matrix A:")
    print_matrix(A)

    m = int(input("Enter the power to be applied to the matrix: "))

    output = power_mult(A, m)

    print("Q3) Resulting matrix after power multiplication:")
    print_matrix(output)

Matrix()

# Q4)
def MostOccuringLetter(input_word):
    highest_occurence = 0
    most_occurred_letter = ''

    for i in range(len(input_word)):
        count = 1

        for j in range(i + 1, len(input_word)):
            if input_word[i] == input_word[j]:
                count += 1

                if count > highest_occurence:
                    highest_occurence = count
                    most_occurred_letter = input_word[i]

    return most_occurred_letter, highest_occurence

user_input_word = input("Enter a word of your choice: ")

result_letter, result_count = MostOccuringLetter(user_input_word)

print(f"Q4) The most occurring letter is: {result_letter}")
print(f"Q4) {result_letter} occurred {result_count} times")
