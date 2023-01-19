import pysrt

# Read in text data from a file
#with open("requirements.txt", "r") as f:
#    text = f.read()

text = "So, I'm a cat person. I have three of them, and they kind of run the place. Whenever Tom Cruise comes over, they go apeshit trying to get away from him. I don't understand it. He's super nice to them, always greets them when he comes in and attempts to pet them, but it's like they can smell something off of him, like they're scared of him.:He's a good sport though, he always chuckles and tells them it's alright and he's not going to hurt them, but no matter what he does, they keep running away. It's gotten to the point where he's like the cat-chaser, just kind of running around the house trying to catch them wherever they go, which isn't exactly dignified for a Hollywood star. People come over and it's ridiculously embarrassing. Am I the Asshole for not trying to do something about it?"

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