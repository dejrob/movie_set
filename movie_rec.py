import random
from matplotlib import pyplot as plt
from movie_main import movies_df

# display bar graph showing average rating per movie genre
movies_df.groupby('genre')['rating'].mean().plot(kind='bar', color='skyblue')
plt.title('Average Rating per Genre')
plt.xlabel('Genre')
plt.ylabel('Average Rating')
plt.show()

user_genre = input("\nWhat genre are you looking for? ")

# capitalise user input genre for later searching
if len(user_genre) > 0:
    user_genre = user_genre[0].upper() + user_genre[1:].lower()
else:
    print("Invalid Input")

user_movies = movies_df[movies_df['genre'] == user_genre]

# if input invalid or match fails
if user_movies.empty:
    print(f"Sorry there are no {user_genre} movies available")
else:
    # filter data and return random suggestion
    short_list = user_movies['title'].tolist()
    random_movie = random.choice(short_list)
    print("We recommend", random_movie)

# menu return block
choice = input("\nWould you like to return to menu? Y/N ")
if choice == 'Y':
    exec(open('movie_main.py').read())
else:
    print("Goodbye")
    exit()


