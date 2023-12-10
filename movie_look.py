from movie_main import movies_df

user_movie = input("What are you searching for? ")

# block carries out a case insensitive search
user_movie = user_movie.lower()
movies_df['title_lower'] = movies_df['title'].str.lower()
match_row = movies_df[movies_df['title_lower'] == user_movie]
# remove temporary column
movies_df.drop('title_lower', axis=1, inplace=True)
movies_df['title_lower'] = movies_df['title'].str.lower()

# assign row entries to variables so we can display them
if not match_row.empty:
    match_title = match_row['title'].values[0]
    match_genre = match_row['genre'].values[0]
    match_rating = match_row['rating'].values[0]

    print(f"Found! {match_title} is a {match_genre} movie with a rating of {match_rating}")
else:
    print("Sorry Movie not found.")

# menu return block
choice = input("\nWould you like to return to menu? Y/N ")
if choice == 'Y':
    exec(open('movie_main.py').read())
else:
    print("Goodbye")
    exit()

