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
    chunks = split_text_into_subtitles(text, 26)
    
    tts_speed = (round(audio.info.length)+1)/len(text) # time pro 1 char tts 
    # Create a list of subtitles
    subtitles = []
    chr_prev = 0
    for i, chunk, in enumerate(chunks):
        # Create a new SubRipItem
        sub = pysrt.SubRipItem()
        sub.index = i + 1
        sub.text = chunk
        sub.start.seconds = chr_prev * tts_speed * 10
        sub.end.seconds = (chr_prev + len(sub.text)) * tts_speed * 10
        chr_prev += len(sub.text)
        # Append the SubRipItem to the list of subtitles
        subtitles.append(sub)

    # Create a SubRipFile object
    subs = pysrt.SubRipFile(subtitles)

    # Save the subtitles to an SRT file
    subs.save("./sources/subtitles.srt", encoding='utf-8')

if __name__ == "__main__": 
    text = "Am I the Asshole for watching naked videos of my girlfriend without her knowing? Post: My girlfriend and I have been together for a few months now. She's really shy and not very comfortable around sex. She told me that she doesn't want to do anything sexual until marriage, but she's okay with me coming to her house and cuddling, watching a movie or two, etc. :One day, when I was going through her computer, I stumbled across a folder with a bunch of naked videos of her, taken with her phone. It was hidden in a folder called Videos, and since she didn't tell me about it, I assumed it was just regular videos. :I watched one just to see what kind of videos she was making, and it ended up being a video of her totally naked, posing and taking pictures of herself. I was immediately embarrassed and deleted the videos as soon as I realized she was naked. I didn't tell her what I saw and I don't plan to. Am I the Asshole here?"
    print(len(text))
    print(audio.info.length)
    tts_speed = audio.info.length/len(text)
    print("speed is ", tts_speed)
    make_srt(text)
    
    