# movie-flix-analyzer
Python command-line program that analyzes the Movie Flix (IMDb) dataset to answer three questions about the data. The program uses filter, map, and reduce pipelines to answer the questions: top directors, average rating by decade, and rating by movie length.

This Python code analyzes mflix.movies.tsv, which has around 21,000
movies with IMDb ratings. There are three questions I provided,
which will be answered by a chain of small functions called pipeline.

HOW TO USE
There is no need to install any packages because everything uses built-in Python.
1. Put final_project.py and mflix.movies.tsv in the same folder.
2. Run python final_project.py
3. There will be a menu in the terminal where it asks the user to
type 1, 2, or 3 to run a question, or 4 to exit.

QUESTIONS (each one uses filter, map, and reduce steps)
1. Which 10 directors have the most movies rated 8.0 or higher on IMDb?
- I used a filter to include ratings of 8.0 or higher.
- I used a map to apply a movie to the director's name.
- I used reduce to keep the 10 biggest counts.
2. What is the average IMDb rating of movies in each decade?
- I used a filter to get valid ratings and years.
- I used a map to apply the movie to the decade and rating.
- I used reduce to get the average rating per decade.
3. Do longer movies get higher IMDb ratings? (short / medium / long)
- I used a filter to get valid runtime and rating.
- I used a map to apply the movie to the length group and rating.
- I used reduce to get the average rating per length group.
Short is under 90 minutes, medium is 90 to 120 minutes, and long is over 120.

Filter: takes a list and returns a smaller list.
For example, I used a filter to return the most rated movies above a score of 8.0.

Map: takes a list and returns a new list of the same length.
For example, I used a map to change each movie row to the director's name.

Reduce: takes a list and reduces it to display only a single result.
For example, I used reduce to show only 10 directors who have the highest rated 8.0 or higher.

Some movies have missing data. For example some of them had
no rating, no runtime, no director, or a invalid year.
The filter code removes those rows, and reports how many data were skipped.

Sample output
Pick one
1) Which 10 directors have the most movies rated 8.0 or higher on IMDb?
2) What is the average IMDb rating of movies in each decade?
3) Do longer movies get higher IMDb ratings? (short / medium / long)
4) Exit
1
Which 10 directors have the most movies rated 8.0 or higher on IMDb?
Movies rated 8.0+: 1302
Skipped (no director listed): 134
Martin Scorsese: 11 movies
Jan Troell: 10 movies
Alfred Hitchcock: 10 movies
Satyajit Ray: 9 movies
Hayao Miyazaki: 9 movies
Steven Spielberg: 7 movies
Stanley Kubrick: 7 movies
Quentin Tarantino: 7 movies
Mani Ratnam: 7 movies
Christopher Nolan: 7 movies

Pick one
1) Which 10 directors have the most movies rated 8.0 or higher on IMDb?
2) What is the average IMDb rating of movies in each decade?
3) Do longer movies get higher IMDb ratings? (short / medium / long)
4) Exit
2
What is the average IMDb rating of movies in each decade?
Skipped (missing rating or bad year): 96
1890s: 5.9
1900s: 7.0
1910s: 6.72
1920s: 7.24
1930s: 7.25
1940s: 7.25
1950s: 7.16
1960s: 7.1
1970s: 7.03
1980s: 6.66
1990s: 6.62
2000s: 6.56
2010s: 6.54

Pick one
1) Which 10 directors have the most movies rated 8.0 or higher on IMDb?
2) What is the average IMDb rating of movies in each decade?
3) Do longer movies get higher IMDb ratings? (short / medium / long)
4) Exit
3
Do longer movies get higher IMDb ratings? (short / medium / long)
Skipped (missing runtime or rating): 487
Short (under 90 min): 6.59
Medium (90-120 min): 6.58
Long (over 120 min): 7.11
