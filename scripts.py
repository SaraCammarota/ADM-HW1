#Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

#Python If-Else
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
if ( n > 100 | n < 1):
    print("Input must be in range [1,100]")   
    
if (n % 2) == 1 : 
    print("Weird")
else: 
   if (2 <= n <= 5):
      print("Not Weird")
   if (6 <= n <= 20):
      print("Weird")   
   if  (n > 20):
      print("Not Weird")
      
      
   

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    
  
if((1 <= a <= 10**10) & (1 <= b <= 10**10)):
  
    
    print(a+b)
    print(a-b)
    print(a*b)

else:
    print("Inputs a and b must be in range [1, 10^10]") 
    
    
    

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a//b)
print(a/b)    

#Loops
if __name__ == '__main__':
    n = int(input())
    
i=0      
if(1 <= n <= 20):
    while i < n:
        print(i**2)
        i+=1
else:
    
    print("Input must be in range [1,20]")
        

      

         



#Write a function
def is_leap(year):
    leap = False
    if(1900<= year<= 10**5):
        if (year%4)==0:
            leap = True
            if (year%100)==0:
                leap=False
                if(year%400)==0:
                    leap = True
                
    else:
        print("Input year must be in range [1900, 10^5]")
                
    
    return leap


#Print Function
if __name__ == '__main__':
    n = int(input())

    
if(1<=n<=150):
    for i in range(n):
        print(i+1, end="")
else:
    print("Input must be in range [1,150]")

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    
list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

print(list)


#Find the Runner-Up Score!  
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    

scores = list(arr)
scores.sort()
same=0    

for i in range(n):
    if (-100 <= scores[i] <= 100):
        check = True
    else:
        check = False
        
        
if ((2<= n <= 10) and (check == True)):
    
    
    for i in range(1, len(scores)): 
        if scores[n-1] == scores[n-1-i]:
          same += 1


        
    print(scores[n-2-same])        
 
else:
  print("Incorrect range") 

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
 

average = sum(student_marks[query_name])/3

average_float = "{:.2f}".format(average)
print(average_float)


#Lists
if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(0, N): 
        command = input()
        command_list = command.split()
        if (command_list[0] == 'insert'):
            list.insert(int(command_list[1]), int(command_list[2]))
        elif (command_list[0] == 'print'):
            print(list)
        elif (command_list[0] == 'remove'):
            list.remove(int(command_list[1]))
        elif(command_list[0] == 'append'):
            list.append(int(command_list[1]))    
        elif (command_list[0] == 'sort'): 
            list.sort()
        elif(command_list[0] == 'pop'):
            list.pop()
        elif(command_list[0] == 'reverse'):
            list.reverse()
            
            
            

#Tuples 
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
t = tuple(integer_list)    

print(hash(t))

#sWAP cASE
def swap_case(s):
    return s.swapcase()


#String Split and Join


def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


#Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[(position+1):]
    return(string)



#Find a string
def count_substring(string, sub_string):
    counter = 0
    
    
    for i in range (0, len(string)-len(sub_string)+1):
        if (string.find(sub_string, i, i+len(sub_string)) != -1):
            counter+=1
        i +=1    
        
    return(counter)


#String Validators
if __name__ == '__main__':
    s = input()
    
    
    
#looking for alphanumeric characters

count=0
for i in range(0,len(s)):
    if (s[i].isalnum() == True):
        count +=1
        
if count != 0 :
    print("True") 
else:
    print("False")    
    
count=0
for i in range(0,len(s)):
    if (s[i].isalpha() == True):
        count +=1
        
if count != 0 :
    print("True") 
else:
    print("False")  
    
count=0
for i in range(0,len(s)):
    if (s[i].isdigit() == True):
        count +=1
        
if count != 0 :
    print("True") 
else:
    print("False")      

count=0
for i in range(0,len(s)):
    if (s[i].islower() == True):
        count +=1
        
if count != 0 :
    print("True") 
else:
    print("False")   
    
count=0
for i in range(0,len(s)):
    if (s[i].isupper() == True):
        count +=1
        
if count != 0 :
    print("True") 
else:
    print("False")      
    
    

#Text Alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'


#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
    


#Text Wrap


def wrap(string, max_width):
    
    string = '\n'.join(textwrap.wrap(string, max_width))
    return(string)
    
    

#What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print('Hello ' + first + ' ' + last + '! You just delved into python.')



#Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    
    
    dim = input()
    x = dim.split()
    N = int(x[0])
    M = int(x[1])
    
    if (N%2 == 1) and (5<N<101) and (M == 3*N):
        
        c=1
        for i in range(1, N//2 + 1): #tra 1 e 3
            print('-'*(((M-(3*c))//2)) +  '.|.'*c  + '-'*((M-(3*c))//2))
            c= c+2
            
        print('-'*((M-7)//2) + 'WELCOME' + '-'*((M-7)//2))
        
        c = c-2
        for i in range(N//2 + 2 , N+1):
          print('-'*(((M-(3*c))//2)) +  '.|.'*c  + '-'*((M-(3*c))//2))
          c= c-2

#String Formatting
def print_formatted(number):
    # your code goes here
    
    p = len(bin(number)[2:])
    for i in range(1, number+1):
        o = oct(i)
        h = hex(i).upper()
        b = bin(i)
        print(str(i).rjust(p), o[2:].rjust(p), h[2:].rjust(p), b[2:].rjust(p))
        
      




#Capitalize!



# Complete the solve function below.
def solve(s):
    new_string= ''
    for i in range(0, len(s)):
        if (s[i] != ' ') and (97 <=ord(s[i]) <= 122):
            if (i==0) or (s[i-1] == ' '):
                new = ord(s[i]) - 32
                new_string += chr(new)
            else:
                new_string += s[i]  
        else:
            new_string += s[i] 
    return(new_string)        
            
      


   


#Introduction to Sets
def average(array):
    # your code goes here
    set(array)
    average = sum(set(array))/len(set(array))
    average = round(average, 3)
    return(average)


#Set .add() 
# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
s = set()

if (0<N<1000):
    
    for i in range(1, N+1):
        country = input()
        s.add(country)
            
    tot = len(s) 
    print(tot)   
            
        
        

#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(0, N): 
    command = input().split()
    if command[0] == 'pop':
        if len(s) != 0:
            s.pop()
            s
    if command[0] == 'remove':
        x = int(command[1])
        if (x in s) == True: 
            s.remove(x)
            s
    if command[0] == 'discard': 
        x = int(command[1])
        s.discard(x)        
        s
        
print(sum(s)) 



#Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))

if (0<len(english.union(french))<1000):
    
    print(len(english.union(french)))
    
else:
    print("total number of students must be in range (0,100)")    
    

#Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))

if (0<len(english.union(french))<1000):
    print(len(english.intersection(french)))
    
else:
    print("total number of students must be in range (0,100)")        

#Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))

if (0<len(english.union(french))<1000):
    print(len(english.difference(french)))
    
else:
    print("total number of students must be in range (0,100)")        

#Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))

if (0<len(english.union(french))<1000):
    print(len(english.symmetric_difference(french)))
    
else:
    print("total number of students must be in range (0,100)")        

#Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT


n_a = int(input())
a = set(map(int, input().split()))
n = int(input())
for i in range(0,n):
    command = list(input().split())
    otherset = set(map(int, input().split()))
    
    if command[0] == 'update':
        a.update(otherset)
    if command[0] == 'intersection_update':
        a.intersection_update(otherset)
    if command[0] == 'difference_update':
        a.difference_update(otherset)
    if command[0] == 'symmetric_difference_update':        
        a.symmetric_difference_update(otherset)
        
print(sum(a))        

#Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
for i in range(0,T):
    n_a = int(input())
    a = set(input().split())
    n_b = int(input())
    b = set(input().split())
    
    if a.intersection(b) == a:
        print(True)
    if a.intersection(b) != a:
        print(False)    






#Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT

a = set(input().split())
n = int(input()) #number of other sets

if (0<len(a)<501) and (0<n<21):
    result = 0 
    for i in range(0, n):
        other = set(input().split())
        if 0<len(other)<101: 
            if a.issuperset(other): 
                if len(a.difference(other)) >= 1: 
                    result += 1   
        else:        
            print("out of range")
            
            
    print(result == n) 
else:
    print("out of range")
                


    
                
            

#Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())
m_s = set(map(int, input().split()))
n = int(input())
n_s = set(map(int, input().split()))

new = m_s.symmetric_difference(n_s)
lista = list(new)

lista.sort()
for i in range(0, len(lista)):
    print(lista[i])




#No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
s = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))



happy = 0

for i in range(0, len(s)):
    if s[i] in a: 
        happy += 1
    if s[i] in b:
        happy = happy - 1
        
print(happy)        
        
        

#Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict
N = int(input())
ordered_dictionary = OrderedDict()
if (0<N<=100):
    for i in range(0,N):
        lista = list(input().split())
        item_name = ' '.join(lista[:-1])
        net_price = int(lista[-1])
        if item_name in ordered_dictionary: 
            ordered_dictionary[item_name] += net_price
        else: 
            ordered_dictionary[item_name] = net_price    
       
    for item in ordered_dictionary:
        print(item, ordered_dictionary[item])

#Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

N = int(input())
colonne = list(input().split())

s = namedtuple('s', ",".join(colonne))
i=0
mark=0
for i in range(0,N):
    stud = s(*(input().split()))
    mark += int(stud.MARKS)
    
average = mark/N

print(average)

#Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d=deque()
N = int(input())
for _ in range(N):
    command = list(input().split())
    if command[0] == "append":
        d.append(int(command[1]))
    if command[0] == "pop":
        d.pop()
    if command[0] == "popleft":
        d.popleft()
    if command[0] == "appendleft":
        d.appendleft(int(command[1]))
       
print(*d)
        

#collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = int(input()) #number of shoes
shoe_s = list(map(int, input().split())) #list of sizes in shop
n = int(input()) #number of costumers
earnings = 0

for i in range(0,n):
    size, price = map(int, input().split())
    if (size in Counter(shoe_s).keys()):
        earnings += price
        shoe_s.remove(size)
        
print(earnings)        
        
    
    

#DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict
n, m = map(int, input().split())
a = defaultdict(list)

if (1<=n<=10000) and (1<=m<=100):
    for i in range(0,n): 
        a[input()].append(i+1)
        
       
    for _ in range(0,m):     
        w = input()
        if w in a: 
            print(*a[w])  
        else:
            print(-1)    
    
    
else:   
    print("out of range")         

#Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar


month, day, year = input().split()
x = calendar.weekday(int(year), int(month), int(day))

if (2000<int(year)<3000): 
    if x == 0: 
     print("MONDAY")
    if x == 1: 
      print("TUESDAY")
    if x == 2: 
        print("WEDNESDAY")
    if x == 3: 
        print("THURSDAY")
    if x == 4: 
       print("FRIDAY")
    if x == 5: 
        print("SATURDAY")
    if x == 6: 
        print("SUNDAY")
    

#Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
for _ in range(t):
    a, b = input().split()
    try:
        print (int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)   
    except ValueError as e:
        print("Error Code:", e)   

#Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = map(int, input().split())
if (0<N<=100) and (0<X<=100):
    subject = []
    for _ in range(X):
        subject.append(list(map(float, input().split())))
        
        
    for i in zip(*subject):
        print(round((sum(i)/X), 1))
    

#ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = list(input())
lowercase = [i for i in s if i.islower()]
uppercase = [i for i in s if i.isupper()]
odd = [i for i in s if (i.isdigit() and int(i)%2 ==1 )]
even = [i for i in s if (i.isdigit() and int(i)%2 ==0 )]

lowercase = sorted(lowercase)
uppercase = sorted(uppercase)
odd = sorted(odd)
even= sorted(even)

print("".join(lowercase + uppercase + odd + even))

#Athlete Sort
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    arr.sort(key = lambda x : x[k])
    for i in range(n):
        print(*arr[i])
    
    



#Map and Lambda Function
cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    fibo = [0, 1]
    if n>1:
        for i in range(2, n): 
            fibo.append(fibo[i-2] + fibo[i-1]) 
        return(fibo) 
    elif n==1:  
        return(fibo[:1])
    elif n ==0:
        return([])
          
    
        
        


#Re.split()
regex_pattern = r",|\."	# Do not delete 'r'.


#Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
if 0<len(s)<100:
    m = re.search(r"([0-9a-zA-Z])\1+", s)
    if m :
      print(m.group(1))

    else: 
      print(-1)
    
    
# I looked for the "\1+" online because I didn't know

#Arrays


def arrays(arr):
    # complete this function
    # use numpy.array
    x = numpy.array(arr[::-1], float)
    return x


#Shape and Reshape
import numpy

arr = list(map(int, input().split()))
array = numpy.array(arr)
print(numpy.reshape(array, (3,3)))


#Transpose and Flatten
import numpy
n, m = map(int, input().split())
lista = []
for _ in range(n):
    lista.append(list(map(int, input().split())))
    
arr = numpy.array(lista)
print(numpy.transpose(arr))
print(arr.flatten())

#Concatenate
import numpy

n, m, p = map(int, input().split())
list1 = []
list2 = []
for _ in range(n):
    list1.append(list(map(int, input().split())))
for _ in range(m):
    list2.append(list(map(int, input().split())))
arr1 = numpy.array(list1)
arr2 = numpy.array(list2)
print(numpy.concatenate((arr1, arr2)))


#Zeros and Ones
import numpy

dim = list(map(int, input().split()))
print(numpy.zeros((dim), dtype=int))
print(numpy.ones((dim), dtype=int))

#Eye and Identity
import numpy
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
print(numpy.eye(n, m))

#Array Mathematics
import numpy

n, m = map(int, input().split())
a = numpy.zeros((n,m), int)
b = numpy.zeros((n,m), int)



for i in range(n):
    lista = list(map(int, input().split()))
    for j in range(m):
        a[i][j] = lista[j]

for i in range(n):
    lista = list(map(int, input().split()))
    for j in range(m):
        b[i][j] = lista[j]

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)

#Floor, Ceil and Rint
import numpy
numpy.set_printoptions(legacy='1.13')
a = numpy.array(input().split(), float)


print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


#Sum and Prod
import numpy

n, m = map(int, input().split())
my_array = [numpy.array(input().split(), int) for _ in range(n)]

print(numpy.prod(numpy.sum(my_array, axis=0)))

#Min and Max
import numpy
n, m = map(int, input().split())
array=[]
for _ in range(n):
    array.append(list(map(int, input().split())))
array= numpy.array(array)
print(numpy.max(numpy.min(array, axis = 1)))

    




#Mean, Var, and Std
import numpy
n, m = map(int, input().split())
array=[]
for _ in range(n):
    array.append(list(map(int, input().split())))
array= numpy.array(array)
print(numpy.mean(array, axis=1))
print(numpy.var(array, axis=0))
print(round(numpy.std(array),11))





#Dot and Cross
import numpy

n = int(input())
arr1=[]
arr2=[]
for _ in range(n):
    arr1.append(list(map(int, input().split())))
for _ in range(n):
    arr2.append(list(map(int, input().split())))
a = numpy.array(arr1, int)
b = numpy.array(arr2, int)    



product = numpy.empty([n,n], int)

for i in range(n):
    for j in range(n):
        product[i][j] = numpy.dot(a[i],b[:,j])
        
print(product)

#Inner and Outer
import numpy

a = numpy.array(list(map(int, input().split())))
b = numpy.array(list(map(int, input().split())))

print(numpy.inner(a,b), numpy.outer(a,b), sep='\n')


#Polynomials
import numpy as np

p = np.array(list(map(float, input().split())))
x = float(input())

print(np.polyval(p, x))



#Linear Algebra
import numpy as np

n = int(input())
a = []

for _ in range(n):
   a.append(list(map(float, input().split())))

print(round(np.linalg.det(np.array(a)), 2))



#Nested Lists
if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    students.sort(reverse=True, key=lambda x : x[1])   #sorting by score
      
    count = 0
    while count<len(students):
        if students[-1][1] == students[-2][1]:
            students.pop()       
        count +=1    
    students.pop()    
    
    new_list=[students[-1][0]]
    for i in range(len(students)-1):
        if students[i][1] == students[-1][1]:
            new_list.append(students[i][0])
   
    new_list.sort()
    for i in range(len(new_list)):
        print(new_list[i])

#Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    candles.sort()
    count=1
    for i in range(len(candles)-1):
        if candles[i] == candles[-1]:
            count +=1
    return count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


#Number Line Jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if v1 == v2 and x1 != x2 :
        return("NO")
    elif v1 == v2 and x1 == x2:
        return("YES")
    else:
        n = (x2-x1)/(v1-v2) 
        if n.is_integer() and n>=0:
            return("YES")
        else:
            return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    x = 5
    y = 2
    likes = 2
    if n>1:
        for _ in range(n-1):
            x = 3*y
            y = math.floor(x/2)
            likes += y
    return(likes)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    section = [int(d) for d in str(n)]
    somma = sum(section) * k 
    while somma >= 10: 
        section = [int(d) for d in str(somma)]
        somma = sum(section) 
    return(somma)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()




#Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    x = arr[-1]
    success = 0
    for i in reversed(range(0, n-1)):
        if (arr[i]>=x):
            arr[i+1]=arr[i]
            print(*arr)
        elif(arr[i]<x):
            arr[i+1] = x 
            print(*arr)
            success = 1
            break
    if success == 0: 
        arr[0] = x
        print(*arr)
        
    


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


#Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
    x = arr[-1]
    for i in reversed(range(0, n-1)):
        if (arr[i]>=x):
            arr[i+1]=arr[i]
            
        elif(arr[i]<x):
            arr[i+1] = x 
            
            break
    if arr[0] > x: 
        arr[0] = x
        
        
def insertionSort2(n, arr):
    new_array=[]
    new_array.append(arr[0])

    for i in range(1, len(arr)):
        new_array.append(arr[i])
        rest = arr[i+1:]
        x = new_array[-1]
        for i in reversed(range(0, len(new_array)-1)):
          if (new_array[i]>=x):
            new_array[i+1]=new_array[i]
            
          elif(new_array[i]<x):
            new_array[i+1] = x 
            break
        if new_array[0] > x: 
          new_array[0] = x

        print(*new_array + rest)
        
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

#Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

pattern = re.compile(r'^[\+\-]?\d*\.\d+$')
t = int(input())
for _ in range(t):
    
    match = re.search(pattern, input())
    
      
    if match:
        print(True)
    else:
        print(False)


#Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
stringa = input()

pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAEIOU]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'


if len(re.findall(pattern,stringa)) == 0:
  print(-1)

else:
  for x in re.findall(pattern,stringa):
    print(x)


#Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

s = input()
k = input()
pattern = re.compile(k)
m = pattern.search(s)

if m == None: 
    print('(-1, -1)')
while m:
    print((m.start(), m.end()-1))
    m = pattern.search(s, m.start()+1)






#Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
for _ in range(N):
    s = str(input())
    pattern = re.compile(r'^(7|8|9)\d{9}$')
    m = pattern.search(s)
    if m:
      print('YES')
    else:
      print('NO')

#Validating and Parsing Email Addresses
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())
pattern = re.compile(r'^<([a-zA-Z0-9])[a-zA-Z0-9-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>$')
for _ in range(N):
    emails = list(map(str, input().split()))
    m = pattern.search(emails[1])
    if m: 
        print(*emails)


#XML 1 - Find the Score


def get_attr_number(node):
    number =  0
    for i in node.iter():
        number += len(i.keys())
    return number



#Alphabet Rangoli
def print_rangoli(size):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size-1, -1, -1): 
        char = alphabet[size-1:i:-1] + alphabet[i:size]
        char = '-'.join(char)
        print(char.center(4*size -3 , '-'))
      
    for i in range(1, size):
        char = alphabet[size-1:i:-1] + alphabet[i:size]
        char = '-'.join(char)
        print(char.center(4*size -3 , '-'))
        
        



#The Captain's Room 
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
from collections import Counter

k = int(input())

rooms = list(input().split(' '))

counter = Counter(rooms)

for i in counter.keys():
    if counter[i]==1:
        print(i)
        break


