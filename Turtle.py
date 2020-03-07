from turtle import *
color('green', 'blue')
begin_fill()
while True:
    forward(120)
    left(125)
    if abs(pos()) < 1:
        break
end_fill()
done()