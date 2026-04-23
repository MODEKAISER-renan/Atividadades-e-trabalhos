A = 0 
B = 0
C = 0
ax = 0

A,B,C = map(float,input().split())

if A < B:
    au = A
    A = B
    B = au
if B < C:
    au = B
    B = C
    C = au
if A < B:
    au = A
    A = B
    B = au

if A < (B+C):
    print("Perimetro = %0.1f"%(A+B+C))
else:
    print("Area = %0.1f"%(0.5*C*(A+B)))
   