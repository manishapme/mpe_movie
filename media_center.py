import os
import webbrowser
from jinja2 import Environment, FileSystemLoader
import movie_data


# get path to project folder
PATH = os.path.dirname(os.path.abspath(__file__))
# tell Jinja where to look for templates in this project
ENV = Environment(
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
)


def render_template(template_filename, context):
    return ENV.get_template(template_filename).render(context)


def open_movies_page(movies):
    """ Create or overwrite the output file, and open it. """

    fname = "movie_list.html"
    movie_list = movies
    context = {'movie_list': movies}

    # using with ensures the file is closed
    with open(fname, 'w') as f:
        html = render_template('fresh_tomatoes.html', context)
        f.write(html)

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.realpath(fname)
    webbrowser.open('file://' + url, new=2)


if __name__ == '__main__':
    open_movies_page(movie_data.movies)
