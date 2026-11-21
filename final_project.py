'''
Movie Flix Analyzer  (COMP 4005 final project)

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
'''

question_1_string = "Which 10 directors have the most movies rated 8.0 or higher on IMDb?"
question_2_string = "What is the average IMDb rating of movies in each decade?"
question_3_string = "Do longer movies get higher IMDb ratings? (short / medium / long)"

# Maps a column name to its position. It starts empty, and then it is filled in at the bottom of the file.
columns_to_index = {}


# Loading and helpers
def load_data(filename):
    '''Reads the TSV file and returns a list of rows. Each row is a list of strings.'''
    rows = []
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            rows.append(line.strip("\n").split("\t"))
    return rows


def build_column_index(header):
    '''Returns a dictionary mapping each column name to its position.'''
    index = {}
    for position in range(len(header)):
        index[header[position].strip('"')] = position
    return index


def clean(value):
    '''Removes spaces and quote marks from the text.'''
    return value.strip().strip('"')


def to_number(value):
    '''Returns the value as a float, or None if it is blank or not a number.'''
    try:
        return float(value)
    except ValueError:
        return None


# QUESTION 1: top 10 directors with movies rated 8.0+
def filter_rating_at_least(rows, minimum):
    '''Uses filter to Keep movies whose IMDb rating is a valid number'''
    kept = []
    for row in rows:
        rating = to_number(row[columns_to_index["imdb.rating"]])
        if rating is not None and rating >= minimum:
            kept.append(row)
    return kept


def filter_has_director(rows):
    '''Uses filter to Keeps movies that have a director listed.'''
    kept = []
    for row in rows:
        director = clean(row[columns_to_index["directors[0]"]])
        if director != "":
            kept.append(row)
    return kept


def map_to_director(rows):
    '''Uses map to turn each movie row into just its director's name.'''
    directors = []
    for row in rows:
        directors.append(clean(row[columns_to_index["directors[0]"]]))
    return directors


def reduce_count_values(items):
    '''Counts how many times each item appears. Then returns a dictionary.'''
    counts = {}
    for item in items:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
    return counts


def reduce_top_n(counts, n):
    '''Returns the biggest entries as a tuple list of (count, name), biggest first.'''
    pairs = []
    for key, value in counts.items():
        pairs.append((value, key))
    return sorted(pairs, reverse=True)[:n]


def run_question_1(rows):
    '''Runs the Question 1 pipeline and prints the answer.'''
    rated = filter_rating_at_least(rows, 8.0)
    with_director = filter_has_director(rated)
    directors = map_to_director(with_director)
    counts = reduce_count_values(directors)
    top = reduce_top_n(counts, 10)

    print(question_1_string)
    print("Movies rated 8.0+: " + str(len(rated)))
    print("Skipped (no director listed): " + str(len(rated) - len(with_director)))
    for count, name in top:
        print(name + ": " + str(count) + " movies")


# QUESTION 2: average IMDb rating by decade
def filter_valid_rating_and_year(rows):
    '''Uses filter to keeps movies that have a valid rating and year'''
    kept = []
    for row in rows:
        rating = to_number(row[columns_to_index["imdb.rating"]])
        year = clean(row[columns_to_index["year"]])
        if rating is not None and year.isdigit():
            kept.append(row)
    return kept


def map_to_decade_rating(rows):
    '''Uses map to turn each movie row into a tuple list (decade, rating).'''
    pairs = []
    for row in rows:
        year = int(clean(row[columns_to_index["year"]]))
        rating = to_number(row[columns_to_index["imdb.rating"]])
        decade = year // 10 * 10
        pairs.append((decade, rating))
    return pairs


def reduce_average_by_key(pairs):
    '''Uses reduce to take (key, number) tuples and then returns a dictionary key called average number.'''
    totals = {}
    counts = {}
    for key, value in pairs:
        if key in totals:
            totals[key] = totals[key] + value
            counts[key] = counts[key] + 1
        else:
            totals[key] = value
            counts[key] = 1
    averages = {}
    for key in totals:
        averages[key] = totals[key] / counts[key]
    return averages


def run_question_2(rows):
    '''Runs the Question 2 pipeline and prints the answer.'''
    valid = filter_valid_rating_and_year(rows)
    pairs = map_to_decade_rating(valid)
    averages = reduce_average_by_key(pairs)

    print(question_2_string)
    print("Skipped (missing rating or bad year): " + str(len(rows) - len(valid)))
    for decade in sorted(averages):
        print(str(decade) + "s: " + str(round(averages[decade], 2)))


# QUESTION 3: do longer movies rate higher?
def filter_valid_runtime_and_rating(rows):
    '''Uses filter to Keep movies that have both a valid runtime and a valid rating.'''
    kept = []
    for row in rows:
        rating = to_number(row[columns_to_index["imdb.rating"]])
        runtime = to_number(row[columns_to_index["runtime"]])
        if rating is not None and runtime is not None:
            kept.append(row)
    return kept


def length_bucket(runtime):
    '''Returns "Short (under 90 min)", "Medium (90-120 min)", or "Long (over 120 min)".'''
    if runtime < 90:
        return "Short (under 90 min)"
    elif 90<= runtime <= 120:
        return "Medium (90-120 min)"
    else:
        return "Long (over 120 min)"


def map_to_length_bucket_rating(rows):
    '''Uses map to turn each movie row into a (length bucket, rating) tuple.'''
    pairs = []
    for row in rows:
        runtime = to_number(row[columns_to_index["runtime"]])
        rating = to_number(row[columns_to_index["imdb.rating"]])
        pairs.append((length_bucket(runtime), rating))
    return pairs


def run_question_3(rows):
    '''Runs the Question 3 pipeline and prints the answer.'''
    valid = filter_valid_runtime_and_rating(rows)
    pairs = map_to_length_bucket_rating(valid)
    averages = reduce_average_by_key(pairs)

    print(question_3_string)
    print("Skipped (missing runtime or rating): " + str(len(rows) - len(valid)))
    for bucket in ["Short (under 90 min)", "Medium (90-120 min)", "Long (over 120 min)"]:
        print(bucket + ": " + str(round(averages[bucket], 2)))


# Menu
if __name__ == "__main__":
    data = load_data("mflix.movies.tsv")
    rows = data[1:]
    columns_to_index = build_column_index(data[0])
    print("Loaded " + str(len(rows)) + " movies.")

    while True:
        print()
        print("Pick one")
        print("1) " + question_1_string)
        print("2) " + question_2_string)
        print("3) " + question_3_string)
        print("4) Exit")
        try:
            answer = int(input().strip())
            if answer == 1:
                run_question_1(rows)
            elif answer == 2:
                run_question_2(rows)
            elif answer == 3:
                run_question_3(rows)
            elif answer == 4:
                break
            else:
                print("Needs to be between 1 and 4, not " + str(answer))
        except ValueError:
            # Fails if the user types something that is not a number
            print("Please type a number from 1 to 4.")