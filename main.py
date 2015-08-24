from movie import Movie

import fresh_tomatoes


# The Movie class takes arguments in this order:
# title, poster url, trailer url, imdb url

movies = [
	Movie("Monty Python and the Holy Grail",
		"http://ia.media-imdb.com/images/M/MV5BMTkzODczMTgwM15BMl5BanBnXkFtZTYwNTAwODI5._V1_SX214_AL_.jpg",
		"https://www.youtube.com/watch?v=LG1PlkURjxE",
		"http://www.imdb.com/title/tt0071853/",
		),
	Movie("Hero",
		"http://ia.media-imdb.com/images/M/MV5BMTk5NjQyMzIwM15BMl5BanBnXkFtZTcwODQyNjYyMQ@@._V1_SX214_AL_.jpg",
		"https://www.youtube.com/watch?v=srFhXDZhUZI",
		"http://www.imdb.com/title/tt0299977/",
		),
	Movie("Pride and Prejudice (1995)",
		"http://ia.media-imdb.com/images/M/MV5BMTU1MDY4OTU5OF5BMl5BanBnXkFtZTcwOTg5NzAyMw@@._V1_SY317_CR5,0,214,317_AL_.jpg",
		"https://www.youtube.com/watch?v=P5MmcT_vcBU",
		"http://www.imdb.com/title/tt0112130/",
		),
	Movie("Avengers",
		"http://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
		"https://www.youtube.com/watch?v=eOrNdBpGMv8",
		"http://www.imdb.com/title/tt0848228/",
		),
	Movie("Back to the Future",
		"http://ia.media-imdb.com/images/M/MV5BMjA5NTYzMDMyM15BMl5BanBnXkFtZTgwNjU3NDU2MTE@._V1_SX214_AL_.jpg",
		"https://www.youtube.com/watch?v=qvsgGtivCgs",
		"http://www.imdb.com/title/tt0088763/",
		),
	Movie("Robin Hood: Men in Tights",
		"http://ia.media-imdb.com/images/M/MV5BMTA2OTYyODU3MDheQTJeQWpwZ15BbWU3MDA5MjIwNDE@._V1_SY317_CR3,0,214,317_AL_.jpg",
		"https://www.youtube.com/watch?v=dX4Ik-cyp-I",
		"http://www.imdb.com/title/tt0107977/",
		)
]

fresh_tomatoes.open_movies_page(movies)
