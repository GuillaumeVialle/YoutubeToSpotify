#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json
from urllib.parse import urlparse
from urllib.parse import parse_qs

from YoutubeProcessing import *

class Server(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()

	def do_GET(self):
		# Extract query param
		video_id = ''
		query_components = parse_qs(urlparse(self.path).query)
		if 'video_id' in query_components:
			video_id = query_components["video_id"][0]

		# Find artist and song name from the youtube video_id
		# Send the message back
		self._set_headers()
		message = YoutubeProcessing.get_song_from_desciption(video_id)
		self.wfile.write(json.dumps(message).encode(encoding='utf_8'))

def run(server_class=HTTPServer, handler_class=Server, port=8080):
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	print('Starting httpd...')
	httpd.serve_forever()

if __name__ == "__main__":
	from sys import argv

	if len(argv) == 2:
		run(port=int(argv[1]))
	else:
		run()