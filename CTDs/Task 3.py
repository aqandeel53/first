import turtle  
t = turtle.Turtle()  
t.color("red")
x=30
while True:
    
    t.forward(x)
    t.left(72)
    if abs(t.pos()) < 1:
        x+=5
        t.left(30)
end_fill()
done()