import sys


def open_file(file_name):  # To help open the file used by other functions in the required form.
    with open(file_name, "r") as read_file:
        try:
            game_list = [row.split("\t") for row in read_file]
        except FileNotFoundError:
            sys.exit("File not found!")
        return game_list


def count_games(file_name):  # How many games are in the file?
    game_list = open_file(file_name)
    return len(game_list)


def decide(file_name, year):  # Is there a game from a given year?
    game_list = open_file(file_name)
    year_in_file = False
    for row in game_list:
        if row[2] == str(year):
            year_in_file = True
    return year_in_file


def get_latest(file_name):  # Which is the latest game?
    game_list = open_file(file_name)
    year_of_release = []
    for row in game_list:
        year_of_release.append(row[2])
    latest_release = max(year_of_release)
    for row in game_list:
        if row[2] == latest_release:
            return row[0]


def count_by_genre(file_name, genre):  # How many games do we have by genre?
    game_list = open_file(file_name)
    games_in_genre = 0
    for row in game_list:
        if row[3] == genre:
            games_in_genre += 1
    return games_in_genre


def get_line_number_by_title(file_name, title):  # What is the line number of the given title?
    game_list = open_file(file_name)
    for game_nr, row in enumerate(game_list):
        if row[0] == title:
            return game_nr + 1
    raise ValueError("Game not found!")


def create_sorted_list(list, nr):  # To help create a sorted list from the "nr"th elements of the parameter list.
    list_to_sort = []
    for row in list:
        if row[nr] not in list_to_sort:
            list_to_sort.append(row[nr])
    return sorted(list_to_sort, key=str.title)


def get_genres(file_name):  # bonus: What are the genres?
    game_list = open_file(file_name)
    return create_sorted_list(game_list, 3)


def sort_abc(file_name):  # bonus: What is the abc ordered list of titles?
    game_list = open_file(file_name)
    return create_sorted_list(game_list, 0)


def when_was_top_sold_fps(file_name):  # bonus: What is the release date of top sold fps shooter game?
    game_list = open_file(file_name)
    sell_nums = []
    for row in game_list:
        if row[3] == "First-person shooter":
            sell_nums.append(float(row[1]))
    for row in game_list:
        if float(row[1]) == max(sell_nums):
            return float(row[2])
