'''Pattern #1: Simple Number Triangle Pattern
Pattern:
1  
2 2  
3 3 3  
4 4 4 4  
Solution: 
'''
n = 4
for i in range(n+1):
    for j in range(1, i+1):
        print(i, end=' ')
    print()

'''
Pattern #2: Inverted Pyramid of Numbers
Pattern:
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
Solution:
'''
rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')

'''
Pattern #3: Half Pyramid Pattern of Numbers
Pattern:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
Solution:
'''
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

'''Pattern #4: Inverted Pyramid of Descending Numbers
Pattern:
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
Solution:
'''

rows = 5
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")


'''Pattern #5: Inverted Pyramid of the Same Digit
Pattern:
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
Solution:
'''
rows = 5
num = rows
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

''' 
Pattern #6: Reverse Pyramid of Numbers
Pattern:
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
Solution:
'''
rows = 6
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")


'''
Pattern #7: Inverted Half Pyramid Number Pattern
Pattern:
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
Solution:
'''
rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")


'''
Pattern #8: Pyramid of Natural Numbers Less Than 10
Pattern:
1 
2 3 4 
5 6 7 8 9
Solution:
''' 

currentNumber = 1

stop = 2

rows = 3 
for i in range(rows):

    for column in range(1, stop):

        print(currentNumber, end='')

        currentNumber += 1

    print("")

    stop += 2


'''   
Pattern #9: Reverse Pattern of Digits from 10 
Pattern:
1
3 2
6 5 4
10 9 8 7
Solution:
'''
start = 1
stop = 2
current_num = stop
for row in range(2, 6):
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    start = stop
    stop += row
    current_num = stop
 
 
'''
Pattern #10: Unique Pyramid Pattern of Digits
Pattern:
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1
Solution:
'''
rows = 6
for i in range(1, rows + 1):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()


'''
Pattern #11: Even Number Pyramid Pattern
Pattern:
10 
10 8 
10 8 6 
10 8 6 4 
10 8 6 4 2
Solution:
'''
rows = 5
last_num = 2 * rows
even_num = last_num
for i in range(1, rows + 1):
    even_num = last_num
    for j in range(i):
        print(even_num, end=' ')
        even_num -= 2
    print("\r")

  
'''
Pattern #12: Pyramid of Horizontal Tables
Pattern:
0  
0 1  
0 2 4  
0 3 6 9  
0 4 8 12 16  
0 5 10 15 20 25  
0 6 12 18 24 30 36
Solution:
'''
rows = 6
for i in range(0, rows):
    for j in range(0, i + 1):
        print(i * j, end='  ')
    print()

'''
Pattern #13: Pyramid Pattern of Alternate Numbers
Pattern:
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
Solution:
'''
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')


'''
Pattern #14: Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers
Pattern:
         1 
       1 2 
     1 2 3 
   1 2 3 4 
 1 2 3 4 5
Solution:
'''
rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")



'''
Pattern #15: Equilateral Triangle with Stars (Asterisk Symbol)
Pattern:
            *   
           * *   
          * * *   
         * * * *   
        * * * * *   
       * * * * * *   
      * * * * * * *
 Solution:
'''
size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")


'''  
Pattern #16: Downward Triangle Pattern of Stars
Pattern:
        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * 
Solution:
'''
rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")

 
 
'''
 Pattern #17: Pyramid Pattern of Stars
Pattern:
* 
* * 
* * * 
* * * * 
* * * * *
Solution:
'''
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

print(" ")