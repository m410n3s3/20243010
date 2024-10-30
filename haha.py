pi = 3.14159
valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

triangulo = (A*C)/(2)
circulo = (C*C) * pi
trapezio = (A+B)*(C)/(2)
quadrado = B*B
retangulo = A*B

print ("TRIANGULO = {:.3f}".format(triangulo))
print ("CIRCULO = {:.3f}".format(circulo))
print ("TRAPEZIO = {:.3f}".format(trapezio))
print ("QUADRADO = {:.3f}".format(quadrado))
print ("RETANGULO = {:.3f}".format(retangulo))