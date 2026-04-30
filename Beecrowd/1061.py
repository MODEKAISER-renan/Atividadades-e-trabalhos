#data: 22.04.2026
#data final: 23.04.2026

lixo,dia = input().split("Dia ")
dia = int(dia)
horas,minutos,segundos = input().split(' : ')
horas,minutos,segundos = int(horas),int(minutos),int(segundos)
lixo,dia2 = input().split("Dia ")
dia2 = int(dia2)
horas2,minutos2,segundos2 = input().split(' : ')
horas2,minutos2,segundos2 = int(horas2),int(minutos2),int(segundos2)
total = (dia*86400)+(horas*3600)+(minutos*60)+segundos
total2 = (dia2*86400)+(horas2*3600)+(minutos2*60)+segundos2
totalReal = total2-total
dia = totalReal // 86400
totalReal = totalReal % 86400
horas = totalReal // 3600
totalReal = totalReal % 3600
minutos = totalReal // 60
segundos = totalReal % 60
print(f"{dia} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")

