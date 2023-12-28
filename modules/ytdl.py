from pytube import YouTube
import os

class Yt_dl:
  def __init__(self, url):
    self.yt = YouTube(url)
    
  def download_audio(self):
    audio = self.yt.streams.filter(only_audio=True).first()
    out_path = os.path.join(os.path.expanduser("~"), "wtv_mp3")
    out_file = audio.download(output_path= out_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
    print(self.yt.title + " has been downloaded to " + out_path )
    return
  
  def download_video(self):
    video = self.yt.streams.filter(file_extension='mp4', res='1080p').first()
    if video is None:
      video = self.yt.streams.filter(file_extension='mp4', res='720p').first()
    
    out_path = os.path.join(os.path.expanduser("~"), "wtv_mp4")
    try:
      if video is None:
        raise TypeError('No streams above 720p available!')
      out_file = video.download(output_path=out_path)
    except TypeError as e:
      print(e)
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp4"
    os.rename(out_file, new_file)
    print(self.yt.title + " has been downloaded to " + out_path)