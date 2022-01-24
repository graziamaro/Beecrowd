a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)

tri = (a*c)/2
circ = c*c*3.14159
trap = ((a+b)*c)/2
quad = b*b
ret = a*b

print ("TRIANGULO: {:.3f}" .format(tri))
print ("CIRCULO: {:.3f}" .format(circ))
print ("TRAPEZIO: {:.3f}" .format(trap))
print ("QUADRADO: {:.3f}" .format(quad))
print ("RETANGULO: {:.3f}" .format(ret))
