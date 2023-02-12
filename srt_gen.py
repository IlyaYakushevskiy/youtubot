import pysrt
from mutagen.mp3 import MP3

# Read in text data from a file
#with open("requirements.txt", "r") as f:
#    text = f.read()

audio = MP3("sources/output.mp3")

def split_text_into_subtitles(text, max_length):
    chunks = []
    chunk = ""
    words = text.split(" ")
    for word in words:
        if len(chunk) + len(word) + 1 > max_length:
            chunks.append(chunk)
            chunk = ""
        chunk += word + " "
    chunks.append(chunk)
    return chunks

def make_srt(text):
     # Split the text into chunks
     chunks = text.split(".")
     tts_speed = audio.info.length/len(text) # time pro 1 char tts 
     # Create a list of subtitles
     subtitles = []
     chr_prev = 0
     for i, chunk, in enumerate(chunks):
         # Create a new SubRipItem
         sub = pysrt.SubRipItem()
         sub.index = i + 1
         sub.text = chunk
         sub.start.seconds = chr_prev * tts_speed * 100
         sub.end.seconds = (chr_prev + len(chunk[i])) * tts_speed * 100
         chr_prev += len(chunk[i])
         # Append the SubRipItem to the list of subtitles
         subtitles.append(sub)
         subs = pysrt.SubRipFile(subtitles)
         subs.save("./sources/subtitles.srt", encoding='utf-8')

if __name__ == "__main__": 
    #text = "Am I the Asshole for playing with my child's toys that he doesn't play with anymore?  My six year old son has an obsession with collecting toys, but he cannot keep them organized and they end up in a huge pile. I have asked him to clean up his toys many times but he doesn't, and I am not going to force him to do so.:Sometimes I find myself playing with his toys, mainly the ones that are hidden in the pile because he doesn't play with them anymore. I find it fun and it helps pass the time when I'm bored. :He sees me playing with his toys and gets mad, saying that he wanted to play with those toys and I should leave them alone. :I tell him that he hasn't played with the toys in a long time and he should organize his toys if he wanted to play with them. :Am I the asshole for playing with my son's toys?"
    text = "Am I the Asshole for Breaking \n Up with Him Over His\n Hot Dog Habit? Post: I met this amazing guy a few \nmonths ago. We hit it\n off right away and had\n an amazing \nfirst couple of\n dates. We started seeing\n each other more often,\n and things were really good\n, until I noticed something strange\n. :Every time I went to\n his house, he was eating a hot\n dog. Just one hot dog. Every\n single time. I couldn't believe it\n. :At first I tried not to be too judgmental\n, but it got to a point where I\n was getting really annoyed. I\n'd try to talk to him\n while he was eating,\n and he'd just be picking at\n his hot dog the whole time\n. :I was getting frustrated, so\n I eventually talked to him about it\n. He just kind of laughed and\n said it was no big deal.\n So I broke up with him. :Now\n friends are telling me I'm being an asshole. Was I out of line for ending our relationship just because he ate a hot dog every day?"

    print(len(text))
    print(audio.info.length)
    tts_speed = audio.info.length/len(text)
    print("speed is ", tts_speed)
    make_srt(text)
    
