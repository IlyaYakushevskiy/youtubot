from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo
#import movie_render_AI


#This script should be used to upload videos throughout the day, ~5 shorts and 2 full size videos

client_secrets = "client_secrets.json"

#movie_render_AI.

def yt_upload(vid_source, vid_name, vid_descr):
    # loggin into the channel
    channel = Channel()
    channel.login(client_secrets, "credentials.storage")
    
    print("login succesful")
    
    # setting up the video that is going to be uploaded
    video = LocalVideo(file_path=vid_source)
    
    print("video found")
    
    # setting snippet
    video.set_title(vid_name)
    video.set_description(vid_descr)
    video.set_tags(["this", "tag"])
    video.set_category("entertainment")
    video.set_default_language("en-US")
    video.set_made_for_kids(False)
    
    print("snipper set")
    
    # setting status
    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status("public")
    video.set_public_stats_viewable(True)
    
    print("status set")
    
    # setting thumbnail
    #video.set_thumbnail_path('test_thumb.png')
    
    print("thumbnail set")
    
    # uploading video and printing the results
    video = channel.upload_video(video)
    print(video.id)
    print(video)
    
    # liking video
    video.like()
    print("Upload successful!")
    return