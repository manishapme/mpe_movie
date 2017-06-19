"""

Basic classes to store details of a single type of media. Movies, books, music.

"""
import re
import webbrowser


class Movie():
    """ The key content required to identify a movie. """

    RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title, storyline, imdb_id, image_url, youtube_url):

        self.title = title
        self.storyline = storyline
        self.imdb_id = imdb_id
        self.image_url = image_url
        self.youtube_url = youtube_url
        self.youtube_id = self.extract_youtube_id(youtube_url)

    def extract_youtube_id(self, youtube_url):
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', youtube_url)
        youtube_id = (youtube_id_match.group(0) if youtube_id_match
                      else None)

        return youtube_id

    def show_trailer(self):
        webbrowser.open(self.youtube_url)


if __name__ == '__main__':
    pass
