'''
data inivial: 12.05.2026
data final: 12.05.2026
'''

I = 0

for i in range(11):
    print(f"I={"0" if I == 0 else f"{I:.1f}"} J=1{f".{(I*10):.0f}" if I != 0 else ""}")
    print(f"I={"0" if I == 0 else f"{I:.1f}"} J=2{f".{(I*10):.0f}" if I != 0 else ""}")
    print(f"I={"0" if I == 0 else f"{I:.1f}"} J=3{f".{(I*10):.0f}" if I != 0 else ""}")
    I += 0.2