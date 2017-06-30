import sys


def open_file(file_name):  # To help open the file used by other functions in the required form.
    with open(file_name, "r") as read_file:
        try:
            game_list = [row.split("\t") for row in read_file]
        except FileNotFoundError:
            sys.exit("File not found!")
        return game_list


def get_most_played(file_name):  # What is the title of the most played (top-seller) game?
    game_list = open_file(file_name)
    sell_nums = []
    for row in game_list:
        sell_nums.append(float(row[1]))
    for row in game_list:
        if float(row[1]) == max(sell_nums):
            return row[0]


def sum_sold(file_name):  # How many copies have been sold in total?
    game_list = open_file(file_name)
    copies_sold = 0
    for row in game_list:
        copies_sold += float(row[1])
    return copies_sold


def get_selling_avg(file_name):  # How many games are sold on average?
    game_list = open_file(file_name)
    sell_nums = []
    for row in game_list:
        sell_nums.append(float(row[1]))
    avg_sell = sum(sell_nums) / len(sell_nums)
    return avg_sell


def count_longest_title(file_name):  # How many characters long is the longest title?
    game_list = open_file(file_name)
    titles = []
    for row in game_list:
        titles.append(row[0])
    return len(max(titles, key=len))


def get_date_avg(file_name):  # What is the average of the release dates?
    game_list = open_file(file_name)
    years_of_release = []
    for row in game_list:
        years_of_release.append(float(row[2]))
    avg_release = sum(years_of_release) / len(years_of_release)
    return round(avg_release)


def input_title():
    user_input = input("Which game are you interested in? ")
    return user_input


def get_game(file_name):  # What details are there of the game?
    title = input_title()
    game_list = open_file(file_name)
    for row in game_list:
        if title == row[0]:
            row[1] = float(row[1])
            row[2] = round(float(row[2]))
            row[4] = row[4].strip("\n")
            return row
    raise ValueError


def count_grouped_by_genre(file_name):  # bonus: How many games are there in the different genres?
    game_list = open_file(file_name)
    genres = []
    games_in_genres = {}
    for row in game_list:
        genres.append(row[3])
    for count in range(len(genres)):
        games_in_genres.setdefault(genres[count], 0)
        games_in_genres[genres[count]] += 1
    return games_in_genres


def get_date_ordered(file_name):  # bonus: What is the date ordered list of the games?
    game_list = open_file(file_name)
    sorted_by_year = sorted(sorted(game_list), key=lambda data: data[2], reverse=True)
    sorted_titles = []
    for row in sorted_by_year:
        sorted_titles.append(row[0])
    return sorted_titles
