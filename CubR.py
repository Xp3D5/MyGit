from tkinter import *
from math import sqrt


def evr():
    try:
        a = float(ent1.get())
        b = float(ent2.get())
        c = float(ent3.get())
        chan = int(ent4.get())
        if chan == 1:
            cub_fun(a, b, c)
        if chan == 2:
            bcub_fun(a, b, c)
        if chan != 1 and chan != 2:
            print("Erro!")
            lb1.configure(text="Такого режима нет!")
            lb2.configure(text="")

    except ValueError:
        lb1.configure(text="Введите числа,ТОЛЬКО ЧИСЛА!")
        lb2.configure(text="")

def cub_fun(a, b, c):  # Решение квадратного уравнения
    D = b ** 2 - 4 * a * c
    print("Дискриминант равен: " + str(D))
    if D < 0:
        print("Корней нет.")
        lb1.configure(text="Корней нет!")
        lb2.configure(text="")
    if D == 0:
        x = -b / (2 * a)
        print("Корень уравнения: " + str(x))
        lb1.configure(text="Первый корень К.уравнения:" + str(x))
        lb2.configure(text="")
        return x
    if D > 0:
        x = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        print("Первый корень квадратного уравнения: " + str(x))
        print("Второй корень квадратного уравнения: " + str(x2))
        m = [x, x2]
        lb1.configure(text="Первый корень К.уравнения:" + str(m[0]))
        lb2.configure(text="Второй корень К.уравнения:" + str(m[1]))
        return m


def bcub_fun(a, b, c):  # Решение биквадратного уравнения
    e = cub_fun(a, b, c)
    y = e[0]
    y2 = e[1]
    print("Первый корень биквадратного уравнения: " + str(sqrt(e[0])))
    print("Второй корень биквадратного уравнения: " + str(sqrt(e[1])))
    lb1.configure(text="Первый корень Бк.уравнения:"+str(sqrt(e[0])))
    lb2.configure(text="Второй корень Бк.уравнения:" + str(sqrt(e[1])))


def builder(root): #UI приложения
    lb1 = Label(root, text="Введите a:", font=("Ubuntu", 12),bg="black",fg="white")
    lb2 = Label(root, text="Введите b:", font=("Ubuntu", 12),bg="black",fg="white")
    lb3 = Label(root, text="Введите c:", font=("Ubuntu", 12),bg="black",fg="white")
    lb4 = Label(root, text="Режим:", font=("Ubuntu", 12),bg="black",fg="white")

    bt1 = Button(root, text="Вывести результат", font=("Ubuntu", 10), command=evr,bg="black",fg="white")

    lb1.grid(row=0, column=0, columnspan=2, sticky="wn")
    lb2.grid(row=1, column=0, columnspan=2, sticky="wn")
    lb3.grid(row=2, column=0, columnspan=2, sticky="wn")
    lb4.grid(row=3, column=0, columnspan=2, sticky="wn")

    ent1.grid(row=0, column=2, columnspan=2, sticky="wn")
    ent2.grid(row=1, column=2, columnspan=2, sticky="wn")
    ent3.grid(row=2, column=2, columnspan=2, sticky="wn")
    ent4.grid(row=3, column=2, columnspan=2, sticky="wn")

    bt1.grid(row=5, column=2, sticky="es", columnspan=1)


root = Tk()
root.title("Программа для решения квадратных ")
root.configure(bg="black")

ent1 = Entry(root, width=20, font=("Ubuntu", 10),bg="black",fg="white") #Вводим a
ent2 = Entry(root, width=20, font=("Ubuntu", 10),bg="black",fg="white") #Вводим b
ent3 = Entry(root, width=20, font=("Ubuntu", 10),bg="black",fg="white") #Вводим c
ent4 = Entry(root, width=20, font=("Ubuntu", 10),bg="black",fg="white") #Вводим режим

lb1 = Label(root, font=("Ubuntu", 12),bg="black",fg="white")
lb2 = Label(root, font=("Ubuntu", 12),bg="black",fg="white")

builder(root)

lb1.grid(row=4,column=0)
lb2.grid(row=4,column=1)
root.mainloop()
