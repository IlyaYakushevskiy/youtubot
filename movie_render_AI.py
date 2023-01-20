from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import *
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip



video_source = "C:/Users/mrass/Downloads/minecraft_tt.mp4"
audio_source = "C:/Users/mrass/Downloads/narration.mp3"
subtitle_source = "C:/Users/mrass/Downloads/subtitles.srt"
img_source = "C:/Users/mrass/Downloads/reddit_title.jpg"
titles = "AIDA for bringing my daughter to the footbal field?" #testline
#film_source = ""
vid_name = "final.mp4"


def video_construct(img_source, video_source, audio_source, subtitle_source, vid_name):

    
    clip = VideoFileClip(video_source)
    myvideo = clip.resize(height=1920, width=1080)
    audio = AudioFileClip(audio_source)
    
    
    sub_text = lambda txt : TextClip(txt, font='Georgia-Regular', fontsize=72, color='white', align="center")
    
    subtitles = SubtitlesClip(subtitle_source, sub_text)
    subtitles = subtitles.set_pos("center")
    #subtitles = subtitles.set_pos((myvideo.w/2 - 70, myvideo.h/2 - 110))
    #Black dynamic background could be added.
    #sub_text = subtitles.set_pos((myvideo.w/2, myvideo.h/2))
    #sub_rect = ColorClip(size=(50, 100), color=(0,0,0), duration=subtitles.duration)
    #sub_rect = sub_rect.set_pos(lambda t: (myvideo.w/2-2, myvideo.h/2-2))
    reddit_post = (ImageClip(img_source)
           .set_start(0) #which second to start displaying image
           .set_duration(3) #how long to display image
           .set_position(("center", "center")))
    title = TextClip(titles, font='Georgia-Regular', size=(930, 0), color='white').set_start(0).set_duration(3).set_position(("center", "center"))
    
    final = CompositeVideoClip([myvideo, subtitles, reddit_post, title]) #Compiles all the tracks into one list. The furthest element on the list, is on the foreground.
    final = final.set_audio(audio)
    final.write_videofile(vid_name, fps=myvideo.fps) #Starts the render
    final.close()
    clean_up(audio_source, subtitle_source)
    return

def clean_up(audio_source, subtitle_source):
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

#video_construct(img_source, video_source, audio_source, subtitle_source, vid_name)
video_split("C:/Users/mrass/Downloads/Fulcrum.mp4")