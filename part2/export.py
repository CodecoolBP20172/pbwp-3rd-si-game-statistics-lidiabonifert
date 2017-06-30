import reports

file_name = "game_stat.txt"

with open("report.txt", "w") as export_data:
    # What is the title of the most played (top-seller) game?
    export_data.write("The title of the most played game is " + str(reports.get_most_played(file_name)) + ".\n")

    # How many copies have been sold in total?
    export_data.write(str(reports.sum_sold(file_name)) + " million copies were sold in total.\n")

    # How many games are sold on average?
    export_data.write(str(reports.get_selling_avg(file_name)) + " million copies were sold on average.\n")

    # How many characters long is the longest title?
    export_data.write("The longest title in the file is " + str(reports.count_longest_title(file_name)) +
                      " characters long." + "\n")

    # What is the average of the release dates?
    export_data.write("The average release date is " + str(reports.get_date_avg(file_name)) + ".\n")

    # What details are there of the game?
    try:
        title = reports.input_title()
        export_data.write("Everything about " + str(title) + ": " +
                          str(reports.get_game(file_name, title)) + "\n")
    except ValueError:
        print("Game not found!")
        export_data.write("No game found with the name: " + str(title) + "\n")

    # bonus: How many games are there in the different genres?
    export_data.write("The number of games released in each genre: " +
                      str(reports.count_grouped_by_genre(file_name)) + "\n")

    # bonus: What is the date ordered list of the games?
    export_data.write("All the titles sorted by year of release: " +
                      str(reports.get_date_ordered(file_name)) + "\n")
