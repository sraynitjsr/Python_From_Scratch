player1 = "Virat Kohli"
age1 = 35
formatted_string_1 = "Player: %s, Age: %d" % (player1, age1)
print(formatted_string_1)

player2 = "Rohit Sharma"
age2 = 37
formatted_string_2 = "Player: {}, Age: {}".format(player2, age2)
print(formatted_string_2)

player_info = {'name': 'Jasprit Bumrah', 'age': 28}
formatted_string_4 = "Player: {name}, Age: {age}".format(**player_info)
print(formatted_string_4)
