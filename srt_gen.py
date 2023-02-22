import pysrt
from mutagen.mp3 import MP3
import re
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

    sentence = re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)
    tts_speed = audio.info.length/len(text) # time pro 1 char tts 
    subtitles = []
    chr_prev = 0
    #len chunk equals n words
    for i, chunk, in enumerate(sentence):
        if len(chunk) > 4:
            words = chunk.split(" ")
            words = [words[i:i+4] for i in range(0, len(words), 4)]
            chunk = "\n".join(" ".join(words) for words in words)
    print(len(chunk.split()))
    # Create a new SubRipItem
    sub = pysrt.SubRipItem()
    sub.index = i + 1
    sub.text = chunk
    sub.start.seconds = chr_prev * tts_speed 
    chr_prev += len(chunk)
    
    sub.end.seconds = (chr_prev ) * tts_speed 

    
    print("chunk is ",chunk)
    print("len of chnk  is ",len(chunk))
    print("lchr_prev is ", chr_prev)
    # Append the SubRipItem to the list of subtitles
    subtitles.append(sub)
    subs = pysrt.SubRipFile(subtitles)
    subs.save("./sources/subtitles.srt", encoding='utf-8')
    return
#if __name__ == "__main__": 
#    text = "Am I the Asshole for playing with my child's toys that he doesn't play with anymore?  My six year old son has an obsession with collecting toys, but he cannot keep them organized and they end up in a huge pile. I have asked him to clean up his toys many times but he doesn't, and I am not going to force him to do so.:Sometimes I find myself playing with his toys, mainly the ones that are hidden in the pile because he doesn't play with them anymore. I find it fun and it helps pass the time when I'm bored. :He sees me playing with his toys and gets mad, saying that he wanted to play with those toys and I should leave them alone. :I tell him that he hasn't played with the toys in a long time and he should organize his toys if he wanted to play with them. :Am I the asshole for playing with my son's toys?"
 #   print(len(text))
 #   print(audio.info.length)
 #   tts_speed = audio.info.length/len(text)
 #   print("speed is ", tts_speed)
 #   make_srt(text)