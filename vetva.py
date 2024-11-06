def vetva(t,pocet):
    if pocet == 0:
        return
    t.pensize(pocet*2)
    t.forward(50)
    t.left(30)
    vetva(t, pocet - 1)
    t.right(60)
    vetva(t, pocet-1)
    if pocet == 1:
        t.dot(20, 'blue')
    else:
        t.dot(30,'green')
    t.left(30)
    t.penup()
    t.backward(50)
    t.pendown()

if __name__ == '__main__': #toto sa vykona len ked
    print("test")