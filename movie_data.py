"""

This files creates a list of movie objects that can be utilized by other files.
Follow the format given to create new instances of a movie. Add each new object
to the movies variable.

"""


import media

ww = media.Movie(
    title='Wonder Woman',
    storyline='Before she was Wonder Woman she was Diana, princess of the Amazons, trained warrior. When a pilot crashes and tells of conflict in the outside world, she leaves home to fight a war to end all wars, discovering her full powers and true destiny.',
    imdb_id='tt0451279',
    image_url='https://images-na.ssl-images-amazon.com/images/M/MV5BNDFmZjgyMTEtYTk5MC00NmY0LWJhZjktOWY2MzI5YjkzODNlXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
    youtube_url='https://www.youtube.com/watch?v=VSB4wGIdDwo'
)

lion = media.Movie(
    title='Lion',
    storyline='A five-year-old Indian boy gets lost on the streets of Calcutta, thousands of kilometers from home. He survives many challenges before being adopted by a couple in Australia. 25 years later, he sets out to find his lost family.',
    imdb_id='tt3741834',
    image_url='https://images-na.ssl-images-amazon.com/images/M/MV5BMjA3NjkzNjg2MF5BMl5BanBnXkFtZTgwMDkyMzgzMDI@._V1_UY268_CR0,0,182,268_AL_.jpg',
    youtube_url='https://www.youtube.com/watch?v=ziOLGzKq6oo'
)

toystory = media.Movie(
    title='Toy Story',
    storyline='A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy\'s room.',
    imdb_id='tt0114709',
    image_url='https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
    youtube_url='https://www.youtube.com/watch?v=mZtJ5DemvDc'
)

movies = [ww, lion, toystory]


if __name__ == '__main__':
    pass
