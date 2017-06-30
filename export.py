import reports


def main(file_name):
    with open("report.txt", "w") as export_data:
        # How many games are in the file?
        export_data.write("Number of games in the file: " + str(reports.count_games(file_name)) + "\n")

        # bonus: What is the abc ordered list of titles?
        export_data.write("ABC ordered list of titles:" + str(reports.sort_abc(file_name)) + "\n")

        # What is the line number of the given title?
        try:
            export_data.write("Line number of given title: " + str(reports.get_line_number_by_title(file_name)) + "\n")
        except ValueError:
            print("Game not found!")
            export_data.write("There's no game with that name in the file!\n")

        # Which is the latest game?
        export_data.write("The latest game in the file: " + reports.get_latest(file_name) + "\n")

        # bonus: What is the release date of top sold fps shooter game?
        export_data.write("The highest-selling FPS was released in " +
                          str(reports.when_was_top_sold_fps(file_name)) + ".\n")

        # Is there a game from a given year?
        export_data.write("There was at least one game released in the given year: " +
                          str(reports.decide(file_name)) + "\n")

        # bonus: What are the genres?
        export_data.write("The following genres are in the file: " + str(reports.get_genres(file_name)) + "\n")

        # How many games do we have by genre?
        try:
            export_data.write("Number of games in a genre: " +
                              str(reports.count_by_genre(file_name)))
        except ValueError:
            print("No games in that genre!")
            export_data.write("There are no games in the given genre in the file!")


main("game_stat.txt")
