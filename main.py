import transcript
import movie_render_AI
from gctts import tts_record
from srt_gen import make_srt
import logging 
import yt_upload


img_source = "./sources/reddit_title.jpg"
video_source = "./sources/minecraft_tt.mp4"
audio_source = "./sources/output.mp3"
subtitle_source = "./sources/subtitles.srt"
print("Input files found..")

#quality = "FHD"
#title_with_codec = movie_render_AI.get_title_format_string()[:-1] + ".mp4"
topic = input("input topic: Am I the Asshole for ")

text = "Am I the Asshole for Breaking  Up with Him Over His  Hot Dog Habit? Post: I met this amazing guy a few  months ago. We hit it  off right away and had  an amazing  first couple of  dates. We started seeing  each other more often,  and things were really good , until I noticed something strange . :Every time I went to  his house, he was eating a hot  dog. Just one hot dog. Every  single time. I couldn't believe it . :At first I tried not to be too judgmental , but it got to a point where I  was getting really annoyed. I 'd try to talk to him  while he was eating,  and he'd just be picking at  his hot dog the whole time . :I was getting frustrated, so  I eventually talked to him about it . He just kind of laughed and  said it was no big deal.  So I broke up with him. :Now  friends are telling me I'm being an asshole. Was I out of line for ending our relationship just because he ate a hot dog every day?"

separator = "Post:"
if separator in text:
    title_name, rest_of_text = text.split(separator, 1)
    text = title_name + rest_of_text #making beautiful human readable text 
else:
    first_sentence = text 

print("title name is :", title_name)
print("full text:", text)

words = rest_of_text.split()
new_text = []
for i in range(0, len(words), 4):
    new_text.append(" ".join(words[i:i+4]))
new_text = "\n".join(new_text)
text = title_name + new_text

"""USE FOR PRODUCTION ONLY"""
#text = "Am I the Asshole for " + topic + transcript.get_transript(topic)



#title_name = text[:text.find("?")+1] #Creates title name (Ex: Am I the Asshole for giving sloppy toppy to my hairdresser?)

transcript.filewriter("redditAIDAscript.txt", text) #should rename to "temp" or smth


tts_record(text)
make_srt(text)

logging.basicConfig(filename="log.txt", level=logging.INFO, format='%(asctime)s:%(message)s') # here we do  log 
logging.info(text)



movie_render_AI.video_construct(img_source, video_source, audio_source, subtitle_source, title_name)





#print(title_with_codec)
# #yt_upload.video_uploader(vid_name, )
#movie_render_AI.video_split("D:/thrash/vid_cut.mp4")
#vid_upload()



