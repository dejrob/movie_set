# movie_set
# this script provides a movie info system based on user input

from data_loader import load_movies_data
movies_df = load_movies_data()

def main():
    # displays options
    print("\nWelcome to the movie set!\nSelect an option:")
    print("A: Recommend Movie\nB: Lookup Movie\nC: View Top Movies\nD: Exit")

    # matches option input to the scripts
    option = input("== ")
    if option == 'A':
        exec(open('movie_rec.py').read(), globals(), {'movies_df': movies_df})
    elif option == 'B':
        exec(open('movie_look.py').read(), globals(), {'movies_df': movies_df})
    elif option == 'C':
        # put movies in descending order by rating then display first 5 rows
        top_movies = movies_df.sort_values(by='rating', ascending=False).head(5)
        # exclude the 'id' column from the output
        top_movies_result = top_movies[['title', 'rating', 'genre']]
        # change index from 0... to 1.. for better user experience
        top_movies_result = top_movies_result.reset_index(drop=True)
        top_movies_result.index = top_movies_result.index + 1
        print("\nOur top movies are:\n", top_movies_result)

    elif option == 'D':
        print("Goodbye")
        exit()
    else:
        print("Invalid Input")
        print("Do you want to try again? Y/N")
        choice = input("== ")
        if choice == 'Y':
            # loops to start of main to retry option input
            main()
        else:
            print("Goodbye")

    # menu return block
    choice = input("Do you want to return to menu? Y/N ")
    if choice == 'Y':
        main()
    else:
        print("Goodbye")
        exit()


if __name__ == "__main__":
    main()
