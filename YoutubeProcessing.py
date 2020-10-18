import youtube_dl

class YoutubeProcessing:
	def __init__(self):
		self.songs_info = {}

	def get_song_from_desciption(video_id):
		youtube_url = "https://www.youtube.com/watch?v={}".format(video_id)
		# use youtube_dl to collect the song name & artist name
		ydl_opts = {'nocheckcertificate': True}
		video = youtube_dl.YoutubeDL(ydl_opts).extract_info(
			youtube_url, download=False)
		song_name = video["track"]
		artist = video["artist"]
		title = video["title"]
		# return ({'song_name': str(song_name), 'artist': artist})
		return ({'title': title, 'song_name' : song_name, 'artist' : artist})