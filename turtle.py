import turtle

# 创建画布和画笔
window = turtle.Screen()
pen = turtle.Turtle()

# 设置画笔的形状为海龟
pen.shape("turtle")

# 绘制海龟的身体
pen.circle(50)

# 绘制海龟的头部
pen.circle(20)

# 绘制海龟的眼睛
pen.penup()
pen.goto(-10, 60)
pen.pendown()
pen.circle(5)
pen.penup()
pen.goto(10, 60)
pen.pendown()
pen.circle(5)

# 绘制海龟的四肢
pen.penup()
pen.goto(-50, 0)
pen.pendown()
pen.left(45)
pen.forward(30)
pen.backward(30)
pen.right(90)
pen.forward(30)
pen.backward(30)

pen.penup()
pen.goto(50, 0)
pen.pendown()
pen.left(135)
pen.forward(30)
pen.backward(30)
pen.right(90)
pen.forward(30)
pen.backward(30)

# 绘制海龟的尾巴
pen.penup()
pen.goto(70, -40)
pen.pendown()
pen.left(30)
pen.forward(20)
pen.backward(20)

# 隐藏海龟
pen.penup()
pen.hideturtle()

# 关闭窗口
turtle.done()
