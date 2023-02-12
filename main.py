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

text = "Am I the Asshole for for beeing so talanted and good in whatever I do. Post: So I'm a 20 year old guy and I've had a lot of luck with pretty much whatever I've set my mind to. I'm in university studying computer science, I'm really good at sports, I make some money with coding projects and whatever else I try my hand at seems to turn out pretty successful. :The problem is twofold. On one hand, my friends and family tend to get really jealous of me and resent my success which is really hurtful. On the other hand, I find myself constantly comparing myself to others and worrying that I'm not good enough and that I should be doing better, much better. I'm kinda in a state of paralysis and feeling like I can only go so far and then it all falls apart:Am I the Asshole for having too much natural talent?"

"""USE FOR PRODUCTION ONLY"""
#text = "Am I the Asshole for " + topic + transcript.get_transript(topic)

separator = "Post:"
if separator in text:
    title_name, rest_of_text = text.split(separator, 1)
    text = title_name + rest_of_text #making beautiful human readable text 
else:
    first_sentence = text 

print("title name is :", title_name)
print("full text:", text)

#title_name = text[:text.find("?")+1] #Creates title name (Ex: Am I the Asshole for giving sloppy toppy to my hairdresser?)

transcript.filewriter("redditAIDAscript.txt", text) #should rename to "temp" or smth


tts_record(text)
make_srt(text)

logging.basicConfig(filename="log.txt", level=logging.INFO, format='%(asctime)s:%(message)s') # here we do beautul log 
logging.info(text)


#print(title_with_codec)
movie_render_AI.video_construct(img_source, video_source, audio_source, subtitle_source, title_name)
#yt_upload.video_uploader(vid_name, )
#movie_render_AI.video_split("D:/thrash/vid_cut.mp4")
#vid_upload()



