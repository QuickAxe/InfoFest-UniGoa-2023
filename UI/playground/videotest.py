# import tkinterweb as tkw
# from tkinter import *

# root = Tk()

# frame = tkw.HtmlFrame(root)
# frame.load_website("https://youtube.com")
# frame.pack()

# root.mainloop()

# from pytube import YouTube
# import webbrowser

# # Input the YouTube video URL
# video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# # Create a YouTube object
# yt = YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# # Get the video title and thumbnail URL
# video_title = yt.title
# thumbnail_url = yt.thumbnail_url

# # Open the video in a web browser
# webbrowser.open(video_url)

# # Display the video details
# print("Playing YouTube video:")
# print("Title:", video_title)
# print("Thumbnail URL:", thumbnail_url)

import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

with ydl:
    result = ydl.extract_info(
        'http://www.youtube.com/watch?v=BaW_jenozKc',
        download=False # We just want to extract the info
    )

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

print(video)
video_url = video['url']
print(video_url)