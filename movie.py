

class Movie:
	"""
	Contains information regarding a movie.
	
	@var title: the title of the movie
	@vtype title: str
	@var poster_image_url: a url pointing to an image poster of the movie.
	@vtype poster_image_url: str
	@var trailer_youtube_url: a url pointing to a youtube trailer of the movie.
	@vtype trailer_youtube_url: str
	"""
	def __init__(self, title, poster_image_url, trailer_youtube_url,
			imdb_url):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.imdb_url = imdb_url
