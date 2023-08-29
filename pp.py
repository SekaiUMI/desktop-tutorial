"""
# Input 4 values on 1 line
x_1 , x_2 , y_1 , y_2 = input("Enter Euclidean Coordinate (x_1,y_1) , (x_2,y_2) that input by x_1 , x_2 , y_1 , y_2 : ").split()

for i in [x_1,x_2,y_1,y_2] :
    i = float(i)

# 1+2+3+...+10
j = 0
for i in range(10) : # 0-9
    j = j + i + 1
    
print("Summation from 1 to 10 :" , j) # j = 55

n = 0
while n < 5 :
    print(n)
    n = n + 1

N = "jogihaeoigoai;hgioreh"
print(N[3])
print(len(N))

N = [1,2,3,4]
print(N[3])
print(len(N))

N = []
for i in range(4) : # i = 0 , i = 1 , i = 2 , i = 3
    x = float(input("Enter Euclidean Coordinate : ")) # 4 x = 4 , 3 , x = 3
    N.append(x)

for i in range(len(N)) : # i = 0 ,1 ,2 , ..., k
    if i != len(N)-1 :
        print(N[i] , end = " , ")
    else :
        print(N[i])
"""

def f(x) : # f(x) = 2x
    return 2*x

def g(x) :
    return 3*x**4 + x**3 + 2*x**2 +10

def h(x,y,z) :
    return (z-x)**2 - x*y + y**2

def i(a,b,c,d) :
    return (a**2 + b**2 - c**2)/(d**2 - 2*a*d + 2*a)

def main() :
    a , b , c , d = [float(e) for e in input("Enter a,b,c,d : ").split()]
    # result_1 = f(f(a)) , result_2 = g(f(a-b)) , result_3 = h(f(a+b),f(a+c),g(f(d**2))) , result_4 = i(h(f(a+b),f(a-c),g(f(d**2))),g(f(a-b)),f(f(f(f(f(c))))),d**8)
    result_1 = f(f(a)) # 2*(2*a)
    result_2 = g(f(a-b)) # (2*(a-b)) -> 3*(2*(a-b))**4 + (2*(a-b))**3 + 2*(2*(a-b))**2 +10
    result_3 = h(f(a+b),f(a+c),g(f(d**2)))
    result_4 = i(h(f(a+b),f(a-c),g(f(d**2))),g(f(a-b)),f(f(f(f(f(c))))),d**8)
    print("f(f({:})) = {:}".format(a,result_1))
    print("g(f({:})) = {:}".format(a-b,result_2))
    print("h(f({:}),f({:}),g(f({:}))) = {:}".format(a+b,a+c,d**2,result_3))
    print("i(h(f({:}),f({:}),g(f({:}))),g(f({:})),f(f(f(f(f({:}))))),{:}) = {:}".format(a+b,a-c,d**2,a-b,c,d**8,result_4))

main()

# f(f(a)) = f(x) ; x = f(a)
x = f(4)
y = f(x)

print(y , f(f(4)))