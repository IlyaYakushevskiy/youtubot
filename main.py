import transcript
import movie_render_AI
from gctts import tts_record
from srt_gen import make_srt
import logging 
import yt_upload



logging.basicConfig(filename='log.txt', filemode='w', format='%(name)s - %(levelname)s - %(text)s')



img_source = "./sources/reddit_title.jpg"
video_source = "./sources/minecraft_tt.mp4"
audio_source = "./sources/output.mp3"
subtitle_source = "./sources/subtitles.srt"
print("Input files found..")

#quality = "FHD"
#title_with_codec = movie_render_AI.get_title_format_string()[:-1] + ".mp4"
topic = input("input topic: Am I the Asshole for ")
text = "Am I the Asshole for " + topic + transcript.get_transript(topic)
title_name = text[:text.find("?")+1] #Creates title name (Ex: Am I the Asshole for giving sloppy toppy to my hairdresser?)
print(title_name)

transcript.filewriter("redditAIDAscript.txt", text)




tts_record(text)
#make_srt(text)


#print(title_with_codec)
movie_render_AI.video_construct(img_source, video_source, audio_source, subtitle_source, title_name)
#yt_upload.video_uploader(vid_name, )
#movie_render_AI.video_split("D:/thrash/vid_cut.mp4")
#vid_upload()



