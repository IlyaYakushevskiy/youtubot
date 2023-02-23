import transcript
import movie_render_AI
from movie_render_AI import output_name_modifier
from gctts import tts_record
from whisper_stt import run
#from srt_gen import make_srt
import logging 
from yt_upload import yt_upload
import time
import os
from os import walk
import random

#List for video topics
wordlist = ["pronouning", "BLMing", "Trumping", "LGBTQ+ing", "vaccinating", "aborting", "fat-shaming", "appropriating", "consuming","levitating","v"]
wordlist_2 = ["entering my brother when he was ", "pros", "sentencing", "pardoning", "licking my parrot's", "sentencing", "pleading", "indicting", "incarcerating", "paroling", "kissing my sister's juicy", "extraditing", "slapping my sister's juicy", "penitrating my sister ", "jur", "giving a felony", "misdemeanor"]
wordlist_15 = ["inspiring", "motivating", "empowering", "encouraging", "uplifting", "fostering", "supporting", "nurturing", "volunteering", "phila", "advo", "gratit", "app", "forgiv", "rec"]
wordlist_2_15 = wordlist_2 + wordlist_15


#Directory for long uncut vids
uncut_dir = "./sources/tempvids"

def file_bulk_cut(directory):

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)
            movie_render_AI.video_split(f, directory)

def main(i):

    img_source = "./sources/reddit_title.jpg"
    video_source = "./sources/vids/" + filenames[random.randint(0 ,len(filenames)-1)]
    audio_source = "./sources/output.mp3"
    subtitle_source = "./sources/sumfile.srt"
    print("Input files found..")

    """USE FOR MANUAL VID CREATION"""
   # topic = input("input topic: Am I the Asshole for ")

    """USE FOR SCRIPTED VID CREATION"""
    topic = i

    """USE FOR TESTS"""
    #text = "Am I the Asshole for overcoming my birthday bibbers and going out of my way to make my bribbers's birthday special? Post:My wife and I have been dating for a few years now, and each year it seems like I just check off the same few boxes on any given birthday: flowers, dinner, a present, maybe a cake, etc. We always have a nice time, but it's just become so familiar that it's starting to feel old and boring.:This year, I wanted to do something different, something special. I decided to take her out of town for a long weekend as a surprise. We had an amazing time, exploring the area and enjoying the food, but let's just say it wasn't exactly budget-friendly. I know she was happy, but my wallet was a tad lighter when we returned.:Now she's complaining to her friends about how she thinks I'm an asshole for 'not appreciating' the effort I made. I don't think this was necessary at all, but I can understand how she feels. Am I the Asshole for going above and beyond for her birthday this year? Am I the Asshole for overcoming my birthday cliches and going out of my way to make my wifes birthday special?"

    """USE FOR PRODUCTION ONLY"""
    text = "Am I the Asshole for " + topic + transcript.get_transript(topic)

    separator = "Post:"

    text = text.replace("/", "") #We somtimes get random // in output
    text = text.replace('"','') #And we get"
    text = text.replace("'", '') #' is also a possibility in a string. We don't want that
    if separator in text:
        title_name, rest_of_text = text.split(separator, 1)
        text = title_name + rest_of_text #making beautiful human readable text 


    else:
        first_sentence = text 

    print("title name is :", title_name)
    print("full text:", text)

    #title_name = text[:text.find("?")+1] #Creates title name (Ex: Am I the Asshole for giving sloppy toppy to my hairdresser?)
    print(title_name)
    transcript.filewriter("redditAIDAscript.txt", text) #should rename to "temp" or smth
    

    tts_record(text)
    #make_srt(text)
    run(audio_source, subtitle_source)

    logging.basicConfig(filename="log.txt", level=logging.INFO, format='%(asctime)s:%(message)s') # here we do beautul log 
    logging.info(text)


    #print(title_with_codec)
    movie_render_AI.video_construct(img_source, video_source, audio_source, subtitle_source, title_name)
    vid_descr = str("#Shorts"+"\n"+"#Reddit"+"\n"+"#Stories"+"\n"+"One of the best stories from reddit!")
   
   
    #movie_render_AI.video_split("D:/thrash/vid_cut.mp4")
    #yt_upload(output_name_modifier(title_name), title_name, vid_descr)#Upload to YT

    return print(title_name, "SUCCESS")

#main(wordlist[1])
filenames = next(walk("./sources/vids"), (None, None, []))[2]  # [] if no file
for i in wordlist_2_15:
    main(i)
    #time.sleep(1800)#Wait 30 min before next cycle

#print(filenames)
#main(1)

#file_bulk_cut(uncut_dir)