import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = '/home/kdover/Programming/python_3/python-100days/4-6/movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(MOVIE_DATA, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors
    


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    r = dict(directors)
    for director in directors:
        if len(directors[director]) < MIN_MOVIES:
            result = r.pop(director, None)
        else:
            r[director].append(_calc_mean(directors[director]))
    return r

    
        


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    average = 0
    for movie in movies:
        average += movie.score
    return (average / len(movies))


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg:.1f}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    sortedDict = sorted(directors.items(), key = lambda x: x[1][len(x[1])-1], reverse=True)
    for counter, director in enumerate(sortedDict, 1):
        if counter <= 20:
            print(fmt_director_entry.format(counter=counter,director=director[0],
                            avg=director[1][len(director[1]) - 1]))
            print(sep_line)
            for movie in director[1]:
                if type(movie) is not float:
                    print(fmt_movie_entry.format(year=movie.year,title=movie.title,score=movie.score))
            print("\n\n\n")        
        else:
            break



def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()