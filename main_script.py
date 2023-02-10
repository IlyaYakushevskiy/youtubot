import transcript
import movie_render_AI


img_source = "./sources/reddit_title.jpg"
video_source = "./sources/minecraft_tt.mp4"
audio_source = "./sources/narration.mp3"
subtitle_source = "./sources/narration.srt"
print("Input files found..")

quality = "FHD"
title_with_codec = movie_render_AI.get_title_format_string()[:-1] + ".mp4"
transcript.main()
#print(title_with_codec)
movie_render_AI.video_construct(img_source, video_source, audio_source, subtitle_source, title_with_codec, quality)
#movie_render_AI.video_split("D:/thrash/vid_cut.mp4")
#vid_upload()

