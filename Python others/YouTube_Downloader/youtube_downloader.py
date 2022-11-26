
# Install required model
from pytube import YouTube

# Get the link to the video
link = input("Link to your video: ")
yt = YouTube(link)

# Get all the format available for videos
videos = yt.streams.all()

# List of format with indexes
video = list(enumerate(videos))

# Print all formats with proper Option number
for i in video:
    print("\nOption", i[0])
    print(i[1])

# Get the option from user
while True:
    # Check if input is a number
    try:
        dn_option = int(input("\nOption number: "))
        break
    except ValueError:
        print("It has to be a number. Try again")
        continue

# Download the video\audio for chosen format
dn_video = videos[dn_option]
dn_video.download()
