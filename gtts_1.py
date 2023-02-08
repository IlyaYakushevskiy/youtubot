from gtts import gTTS
import pysrt

# Read in text data from a file
#with open("requirements.txt", "r") as f:
#    text = f.read()

text = " Hey everyone, I have a bit of a situation and I was wondering if I am the asshole in this scenario. A few weeks ago, I noticed that there are always a bunch of hot bitches hanging out near my apartment. I figured they were just local girls who wanted to have a fun time, so I started to chat with them and eventually invited them over. My problem is that my girlfriend found out and was really pissed off. She said that I was being disrespectful to her and that it made her uncomfortable. I offered to apologize and promised that I wouldn't do it again, but she still doesn't want to talk about it. Am I the asshole for wanting to invite hot bitches over to my place?"

# Generate speech from the text
tts = gTTS(text)

# Save the speech to an MP3 file
tts.save("./source_content/gtts_output.mp3")

# Split the text into chunks
chunks = text.split(".")

# Create a list of subtitles
subtitles = []
for i, chunk in enumerate(chunks):
    # Create a new SubRipItem
    sub = pysrt.SubRipItem()
    sub.index = i + 1
    sub.text = chunk
    sub.start.seconds = i * 10
    sub.end.seconds = (i+1) * 10
    # Append the SubRipItem to the list of subtitles
    subtitles.append(sub)

# Create a SubRipFile object
subs = pysrt.SubRipFile(subtitles)

# Save the subtitles to an SRT file
subs.save("subtitles.srt", encoding='utf-8')