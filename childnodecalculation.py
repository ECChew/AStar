import numpy as np
"""
Stratégie utilisée : De haut en bas, de gauche à droite
Par Julien Huynh 24/04/2020
"""
choice = 1 # 1 for Manhattan(4 directions), 2 for Euclidian (8 diagonals authorized)

yg = 2
xg = 4


ypos = 2
xpos = 3

cpos = 11#Cost at actual position


c = 1 #Cost from a node to another


xchild = []
ychild = []
hchild = []
gchild = []

if choice == 1:
    def h(x, y):
        return c * (np.abs(yg - y) + np.abs(xg - x))
# Première case, celle du haut
    gchild.append(cpos + c)
    xchild.append(xpos + 0)
    ychild.append(ypos - 1)
    hchild.append(h(xchild[0], ychild[0]))
#Deuxième case, celle à la même hauteur, à gauche
    gchild.append(cpos + c)
    xchild.append(xpos - 1)
    ychild.append(ypos + 0)
    hchild.append(h(xchild[1], ychild[1]))
#Troisième case, celle à la même hauteur, à droite
    gchild.append(cpos + c)
    xchild.append(xpos + 1)
    ychild.append(ypos + 0)
    hchild.append(h(xchild[2], ychild[2]))
#Quatrième case, celle en dessous
    gchild.append(cpos + c)
    xchild.append(xpos + 0)
    ychild.append(ypos + 1)
    hchild.append(h(xchild[3], ychild[3]))
elif choice == 2:
    def h(x, y):
        return c * np.sqrt((yg - y) ** 2 + (xg - x) ** 2)
#Première case, celle en haut à gauche
    gchild.append(cpos + c)
    xchild.append(xpos - 1)
    ychild.append(ypos - 1)
    hchild.append(h(xchild[0], ychild[0]))
#Deuxième case, celle en haut
    gchild.append(cpos + c)
    xchild.append(xpos + 0)
    ychild.append(ypos - 1)
    hchild.append(h(xchild[1], ychild[1]))
#Troisième case, celle en haut, à droite
    gchild.append(cpos + c)
    xchild.append(xpos + 1)
    ychild.append(ypos - 1)
    hchild.append(h(xchild[2], ychild[2]))
#Quatrième case, celle à gauche
    gchild.append(cpos + c)
    xchild.append(xpos - 1)
    ychild.append(ypos + 0)
    hchild.append(h(xchild[3], ychild[3]))
#Cinquième case, celle à droite
    gchild.append(cpos + c)
    xchild.append(xpos + 1)
    ychild.append(ypos + 0)
    hchild.append(h(xchild[4], ychild[4]))
#Sixième case, celle en bas à gauche
    gchild.append(cpos + c)
    xchild.append(xpos - 1)
    ychild.append(ypos + 1)
    hchild.append(h(xchild[5], ychild[5]))
#Septième case, celle en bas
    gchild.append(cpos + c)
    xchild.append(xpos + 0)
    ychild.append(ypos + 1)
    hchild.append(h(xchild[6], ychild[6]))
#Huitième case, celle en bas à droite
    gchild.append(cpos + c)
    xchild.append(xpos + 1)
    ychild.append(ypos + 1)
    hchild.append(h(xchild[7], ychild[7]))


cchild = np.zeros(len(xchild))
print("Node actuelle : (", ypos, ", ", xpos, "), g = ", cpos, "h = ", h(xpos, ypos))
for i in range(len(xchild)) :
    cchild[i] = gchild[i] + hchild[i]  # Total cost for children nodes
    print("(", ychild[i], ", ", xchild[i], "), g = ", gchild[i], ", h = ", hchild[i], ", total cost = ", cchild[i])
