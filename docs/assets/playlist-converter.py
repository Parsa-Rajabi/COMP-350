from pytube import Playlist
import csv

yt_play = Playlist("https://www.youtube.com/playlist?list=PLpQQipWcxwt_wKeFEmZL15qOZEkiVUQAq")

video_title_list = []
for i in yt_play.videos:
    video_title_list.append(i.title)

title_url_list = list(zip(video_title_list, yt_play.video_urls))

# Write the output to a markdown file
with open('yt_playlist.md', 'w', newline='') as file:
    for title, url in title_url_list:
        # Write each video as a markdown bullet point with link
        file.write(f"- [{title}]({url})\n")