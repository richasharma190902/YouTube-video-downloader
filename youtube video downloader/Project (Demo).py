from pytube import YouTube    #import the package

url = input("Enter URL of video = ") #url of the video

my_video = YouTube(url)

print("_______________TITLE OF VIDEO_________________")  #title of the video

print(my_video.title)



my_video = my_video.streams.get_highest_resolution()

my_video.download()


print("**********VIDEO DOWNLOADED**********") #for video download