# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!

#Load the CSV file and store as netflix_df.
netflix_df=pd.read_csv("netflix_data.csv")
print(netflix_df)

#Filter the data to remove TV shows and store as netflix_subset.

netflix_subset = netflix_df.query('type == "Movie"')
print(netflix_subset)

#Investigate the Netflix movie data, 
#keeping only the columns "title", "country", "genre", "release_year", "duration", 
#and saving this into a new DataFrame called netflix_movies.

netflix_movies= netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]
print(netflix_movies)

# saving the resulting DataFrame as short_movies; 
#inspect the result to find possible contributing factors.

short_movies=netflix_movies[netflix_movies['duration'] < 60]
print(short_movies)

#Using a for loop and if/elif statements, 
#iterate through the rows of netflix_movies 
#and assign colors of your choice to four genre groups 
#("Children", "Documentaries", "Stand-Up", and "Other" for everything else). 
#Save the results in a colors list. Initialize a figure object called fig and create a scatter plot for movie duration by release year using the colors list to color the points and using the labels "Release year" for the x-axis, "Duration (min)" for the y-axis, and the title "Movie Duration by Year of Release".


colors = []
for genre in netflix_movies['genre']:
    if genre == 'Children':
        colors.append('orange')
    elif genre == 'Documentaries':
        colors.append('blue')
    elif genre == 'Stand-Up':
        colors.append('yellow')
    else:
        colors.append('green')

# Creating the scatter plot
fig, ax = plt.subplots()
scatter = ax.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)

# Adding labels and title
ax.set_xlabel('Release year')
ax.set_ylabel('Duration (min)')
ax.set_title('Movie Duration by Year of Release')

# Display the plot
plt.show()