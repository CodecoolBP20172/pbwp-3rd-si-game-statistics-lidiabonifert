import reports

with open("report.txt", "w") as export_data:
    # How many games are in the file?
    export_data.write("Number of games in the file: " + str(reports.count_games("game_stat.txt")) + "\n")

    # bonus: What is the abc ordered list of titles?
    export_data.write("ABC ordered list of titles:" + str(reports.sort_abc("game_stat.txt")) + "\n")

    # What is the line number of the given title?
    game_name = "World of Warcraft"
    export_data.write("The line number of " + game_name + ": " +
                      str(reports.get_line_number_by_title("game_stat.txt", game_name)) + "\n")

    # Which is the latest game?
    export_data.write("The lastest game in the file: " + reports.get_latest("game_stat.txt") + "\n")

    # bonus: What is the release date of top sold fps shooter game?
    export_data.write("The highest-selling FPS was released in " +
                      str(reports.when_was_top_sold_fps("game_stat.txt")) + "\n")

    # Is there a game from a given year?
    year = "1989"
    export_data.write("There was at least one release in " + year + ": " +
                      str(reports.decide("game_stat.txt", year)) + "\n")

    # bonus: What are the genres?
    export_data.write("The following genres are in the file: " + str(reports.get_genres("game_stat.txt")) + "\n")

    # How many games do we have by genre?
    genre = "RPG"
    export_data.write("Number of games in the " + genre +
                      " genre: " + str(reports.count_by_genre("game_stat.txt", genre)))
