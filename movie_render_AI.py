from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import *
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from mutagen.mp3 import MP3

def output_name_modifier(title_name):
    title_with_codec = title_name[:-10] + ".mp4"
    title_with_codec.replace('/', "_")
    vid_name = "./outputs/" + title_with_codec.replace(" ", "_")
    return vid_name

def clean_string(thelist):#cleans the output from \n separators, and converts the list into the string
    for el in thelist:
        if el == '\n':
            thelist.remove(el)
    tempString = ''
    for x in thelist:
        tempString += x
    return tempString

def get_title_format_string(): #getting the title(AIDA for ...) and formatting the string, so that it can be used
    file = open("redditAIDAscript.txt", "r")
    sumstring = file.readlines()
    post = clean_string(sumstring) #constructing the string from the list of output
    title_name = post[:post.find("?")+2]
    file.close()
    return title_name

def video_construct(img_source, video_source, audio_source, subtitle_source, title_name):

    audio = AudioFileClip(audio_source)
    audio_len = MP3(audio_source)
    audio_len_secs = int(round(audio_len.info.length) + 1)
    clip = VideoFileClip(video_source)
    myvideo = clip.resize(height=1920, width=1080) #ya dolbayob. Solgasny, i uznali

    

    #global vid_name
     #Reaplces spaces with _
    #vid_name = "./outputs/" + "crazy bimbo.mp4"
    
    sub_text = lambda txt : TextClip(txt, font='Georgia-Regular', fontsize=72, color='white', align="center", bg_color="black")
    
    subtitles = SubtitlesClip(subtitle_source, sub_text)
    subtitles = subtitles.set_pos("center")

    reddit_post = (ImageClip(img_source)
           .set_start(0) #which second to start displaying image
           .set_duration(3) #how long to display image
           .set_position(("center", "center")))

    title = TextClip(title_name, font='Georgia-Regular', size=(930, 0), color='white').set_start(0).set_duration(3).set_position(("center", "center"))
    
    final = CompositeVideoClip([myvideo, subtitles, reddit_post, title]).set_duration(audio_len_secs) #Compiles all the tracks into one list. The furthest element on the list, is on the foreground.
    final = final.set_audio(audio)
    final.write_videofile(output_name_modifier(title_name), fps=myvideo.fps, threads=2, codec="libx264") #Starts the render
    final.close()
    #clean_up(audio_source, subtitle_source)
    return print("Video written!")

def clean_up(audio_source, subtitle_source): #delete used tts audio and subtitles
    source_list = [audio_source, subtitle_source]
    file_path = source_list
    for x in file_path:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print("File has been deleted")
        else:
            print("File does not exist")
    return

def video_split(film_source): 
    film = VideoFileClip(film_source) #Load the File
    duration = film.duration #Get duration in seconds
    coefficient = duration / 59 #Calculate into how many clips vid can be chopped
    for x in range(int(round(coefficient))): #Chop it into clips with unique names in numerical order
        start_time = (coefficient * x)
        end_time = start_time + 59
        n = film.subclip(start_time, end_time)
        n = n.volumex(0.4)
        abra = "clip_"+ str(x) + ".mp4"
        print(abra) #Nevermind this, it just looks better this way xD
        n.write_videofile(abra)
    return

if __name__ == "__main__":
    print(get_title_format_string()[:-1])