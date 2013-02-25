'''
Write code that will print ten astrisks (*) like the following:
* * * * * * * * * *
'''
print("first");
for i in range (10):
    print ("*", end = " ");

'''
Write code that will print the following:
* * * * * * * * * *
* * * * *
* * * * * * * * * * * * * * * * * * * *
'''
print("");
print("second");
for i in range (10):
    print ("*", end = " ");
print("");
for i in range (5):
    print ("*", end = " ");
print("");
for i in range (20):
    print ("*", end = " ");

'''
Use two for loops, one of them nested, to print the following 10x10 rectangle:
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
'''
print("");
print("third");
for i in range (10):
    for j in range (10):
        print("*", end = " ");
    print("");

'''
Use two for loops, one of them nested, to print the following 5x10 rectangle:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
print("");
print("fourth");
for i in range (10):
    for j in range (5):
        print("*", end = " ");
    print("");

'''
Use two for, one of them nested, to print the following 20x5 rectangle:
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
'''
print("");
print("fifth");
for i in range (5):
    for j in range (20):
        print("*", end = " ");
    print("");

'''
Write code that will print the following:
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
'''
print("");
print("sixth");
for i in range (10):
    for j in range (10):
        print(j, end = " ");
    print("");

'''
Adjust the prior program to print:
0 0 0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 1 1 
2 2 2 2 2 2 2 2 2 2 
3 3 3 3 3 3 3 3 3 3 
4 4 4 4 4 4 4 4 4 4 
5 5 5 5 5 5 5 5 5 5 
6 6 6 6 6 6 6 6 6 6 
7 7 7 7 7 7 7 7 7 7 
8 8 8 8 8 8 8 8 8 8 
9 9 9 9 9 9 9 9 9 9
'''
print("");
print("seventh");
for i in range (10):
    for j in range (10):
        print(i, end = " ");
    print("");

'''
Write code that will print the following:
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
0 1 2 3 4 5
0 1 2 3 4 5 6
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8 9
'''
print("");
print("eight");
j = 0;
for i in range (10):
    while j <= i:
        print(j, end = " ");
        j += 1;
    print("");
    j = 0;

'''
Write code that will print the following:
0 1 2 3 4 5 6 7 8 9
  0 1 2 3 4 5 6 7 8
    0 1 2 3 4 5 6 7
      0 1 2 3 4 5 6
        0 1 2 3 4 5
          0 1 2 3 4
            0 1 2 3
              0 1 2
                0 1
                  0
'''
print("");
print("ninth");
j = 0;
max_range = 10;
k = 0;
for i in range (10):
    while k < i:
        print("  ", end = "");
        k +=1;
    k = 0;
    while j < max_range:
        print(j, end = " ");
        j = j+ 1;
    print("");
    max_range -=1;
    j = 0;

'''
Write code that will print the following (Getting the alignment is hard, at least get the numbers):
  1   2   3   4   5   6   7   8   9 
  2   4   6   8  10  12  14  16  18 
  3   6   9  12  15  18  21  24  27 
  4   8  12  16  20  24  28  32  36 
  5  10  15  20  25  30  35  40  45 
  6  12  18  24  30  36  42  48  54 
  7  14  21  28  35  42  49  56  63 
  8  16  24  32  40  48  56  64  72 
  9  18  27  36  45  54  63  72  81
'''
print ("tenth");
for i in range (1, 10, 1):
    for j in range (1, 10, 1):
        if j*i < 10:
            print("", end = " ");
        print(j * i, end = " ");
    print("");

'''
Write code that will print the following:
                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
'''
print("eleventh");
for i in range(1,10,1):
    for z in range (10-i):
        print(" ", end = " ");
    for j in range(1,i,1):
        print(j, end = " ");
    for i in range (i, 0, -1):
        print (i, end = " ");
    print ("");

'''
Write code that will print the following:
                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8
      1 2 3 4 5 6 7
        1 2 3 4 5 6
          1 2 3 4 5
            1 2 3 4
              1 2 3
                1 2
                  1
'''

print("12th");
for i in range(1,10,1):
    for z in range (10-i):
        print(" ", end = " ");
    for j in range(1,i,1):
        print(j, end = " ");
    for i in range (i, 0, -1):
        print (i, end = " ");
    print ("");
j = 1;
max_range = 9;
k = 1;
for i in range (1,9):
    while k < i:
        print("  ", end = "");
        k +=1;
    k = 1;
    while j < max_range:
        print(j, end = " ");
        j = j+ 1;
    print("");
    max_range -=1;
    j = 1;

'''
Write code that will print the following:
                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
          1 2 3 4 5 4 3 2 1
            1 2 3 4 3 2 1
              1 2 3 2 1
                1 2 1
                  1
'''
print("13th");
for i in range(1,10,1):
    for z in range (10-i):
        print(" ", end = " ");
    for j in range(1,i,1):
        print(j, end = " ");
    for i in range (i, 0, -1):
        print (i, end = " ");
    print ("");
max_range = 9;
max_range2 = 7;
for i in range(1,10,1):
    for z in range (i+1):
        print(" ", end = " ");
    for j in range(1,max_range, 1):
        print(j, end = " ");
    max_range -= 1;
    for i in range (max_range2 ,0 , -1):
        print (i, end = " ");
    max_range2 -= 1;
    print ("");




    
