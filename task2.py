import turtle
import math


def pythagoras_tree(t, branch_len, level):
    """
    Функція рекурсивно малює 'дерево Піфагора'.
    t          : об'єкт Turtle
    branch_len : довжина поточної гілки
    level      : рівень рекурсії, що залишився
    """
    if level == 0:
        return

    # Намалювати "стовбур" (поточну гілку)
    t.forward(branch_len)

    # Ліва гілка
    t.left(45)
    pythagoras_tree(t, branch_len / math.sqrt(2), level - 1)

    # Перехід до правої гілки
    t.right(90)
    pythagoras_tree(t, branch_len / math.sqrt(2), level - 1)

    # Повернутися в початковий нахил
    t.left(45)

    # Повернутися "вниз" по стовбуру
    t.backward(branch_len)


def main():
    # Зчитуємо від користувача бажаний рівень рекурсії
    level = int(input("Вкажіть рівень рекурсії: "))

    # Ініціалізація вікна та 'черепашки'
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    t = turtle.Turtle()

    # Повертаємо черепашку стовбуром догори
    t.left(90)

    # Зсунемося трохи вниз, щоб дерево повністю влізло у вікно
    t.penup()
    t.backward(200)
    t.pendown()

    # Швидкість малювання (0 – найшвидша)
    t.speed(0)

    # Викликаємо рекурсивну функцію
    pythagoras_tree(t, 100, level)

    # Залишаємо вікно відкритим
    turtle.done()


if __name__ == "__main__":
    main()
