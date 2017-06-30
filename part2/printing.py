from pprint import pprint
import reports

file_name = "game_stat.txt"

# What is the title of the most played (top-seller) game?
print("\nThe most played game is: ")
pprint(reports.get_most_played(file_name))

# How many copies have been sold in total?
print("\nNumber of copies sold in total (M): ")
pprint(reports.sum_sold(file_name))

# How many games are sold on average?
print("\nThe average number of copies sold (M): ")
pprint(reports.get_selling_avg(file_name))

# How many characters long is the longest title?
print("\nLength of longest title: ")
pprint(reports.count_longest_title(file_name))

# What is the average of the release dates?
print("\nThe average of release dates is: ")
pprint(reports.get_date_avg(file_name))

# What details are there of the game?
title_input = input("\nWhich game are you interested in? ")
print("\nEverything about " + title_input + ": ")
if reports.get_game(file_name, title_input) is not None:
    pprint(reports.get_game(file_name, title_input))
else:
    print("There's no game with that title in the file!")

# bonus: How many games are there in the different genres?
print("\nThe following number of games are per genre: ")
pprint(reports.count_grouped_by_genre(file_name))

# bonus: What is the date ordered list of the games?
print("\nList of titles sorted by year of release: ")
pprint(reports.get_date_ordered(file_name))
