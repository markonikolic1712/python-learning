# from turtle import Turtle, Screen
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("yellow")
# timmy.forward(100)
# timmy.color("red")
# timmy.right(45)
# timmy.forward(100)
# timmy.color("blue2")
# timmy.right(45)
# timmy.forward(100)
# timmy.color("coral")
# timmy.right(45)
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
imena = ["Pera", "Mika", "Zika"]
adrese = ["Perina ulica", "Mikina ulica", "Zikina ulica"]
table.add_column("ime osobe", imena)
table.add_column("adresa na kojoj stanuje", adrese)
# table.align["ime osobe"] = "l"
# table.align["adresa na kojoj stanuje"] = "r"
# sve kolone se ravnaju levo
table.align = "l"

print(table)





