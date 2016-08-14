__author__ = 'Orka'
import urllib.request
class FindMovieLength(object):
    def __init__(self, movie):
        self.movie = movie
        self.url = None

    def search_url(self):
        movie_url = 'http://m.imdb.com/find?q=' + self.movie.replace(' ', '+').replace('(', '%28').replace(')', '%29')
        #print bralh
        with urllib.request.urlopen(movie_url) as HTML:
            html = HTML.read()
        html = str(html)
        try:
            lower = html.index('/title/') + len('/title/')
            movie_id = 9
            html = html[lower:lower+movie_id]
            url = 'http://m.imdb.com/title/' + html + '/'
            return url
        except ValueError:
            return 'movie not found'

    def find_time(self, movie_url = None):
        if movie_url == None:
            movie_url = self.search_url()
        if movie_url != 'movie not found':
            with urllib.request.urlopen(movie_url) as movie_page:
                html = movie_page.read()
            html = str(html)
            if '"duration"' in html:
                lower = html.index('"duration"')
                html = html[lower:]
                lower = html.index('  ')
                html = html[lower:].replace(' ', '')
                upper = html.index('min')
                html = int(html[:upper])
                return html
            else:
                return('not found')

    def find_category(self, movie_url = None):
        if movie_url == None:
            movie_url = self.search_url()
        if movie_url != 'movie not found':
            with urllib.request.urlopen(movie_url) as movie_page:
                html = movie_page.read()
            html = str(html)
            categories = []
            if 'itemprop="genre">' in html:
                while 'itemprop="genre">' in html:
                    lower = html.index('itemprop="genre">')
                    html = html[lower:]
                    cat = html[len('itemprop="genre">'):html.index('<')]
                    categories.append(cat)
                    html = html[html.index('<'):]
                return ', '.join(categories)
            else:
                return('not found')

    def find_director(self, movie_url = None):
        if movie_url == None:
            movie_url = self.search_url()
        if movie_url != 'movie not found':
            with urllib.request.urlopen(movie_url) as movie_page:
                html = movie_page.read()
            html = str(html)
            directors = []
            if '<span itemprop="name">\\n' in html:
                lower = html.index('<span itemprop="name">\\n') + len('<span itemprop="name">\\n')
                html = html[lower:]
                while html.index(',') < html.index('\\n'):
                    director = html[:html.index(',')]
                    directors.append(director)
                    html = html[html.index(director) + len(director) + len(', \\'):]
                else:
                    director = html[:html.index('\\n')]
                    directors.append(director)
                return ', '.join(directors)
            else:
                return('not found')
    def save_time(self, movie_list):
        temp_list = []
        for each in movie_list:
            if each[1] == '' or each[1] =='not found':
                temp_list.append([each[0], ''])

        for each in temp_list:
            movie_url = self.search_url()
            #if movie_url != 'movie not found':
            #    movie_length =