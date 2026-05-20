# from turtle import Turtle,Screen
# my_screen = Screen()

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.fd(100)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon",["Pikachu","Raichu","Bulbasaur","Squirtle","Charmander"]) 
table.add_column("Type",["Electric","Electric","Grass","Water","Fire"])
table.align = "l"

print(table)