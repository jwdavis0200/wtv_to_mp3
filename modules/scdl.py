from sclib import SoundcloudAPI, Track, Playlist
import os
class Sc_dl:
  def __init__(self, url):
    self.api = SoundcloudAPI()
    self.track = self.api.resolve(url)
    assert type(self.track) is Track
    
  def download_audio(self):
    out_path = os.path.join(os.path.expanduser("~"), "wtv_mp3")
    file_name = f'{self.track.artist} - {self.track.title}.mp3'
    file_path = os.path.join(out_path, file_name)
    
    with open(file_path, "wb+") as file:
      self.track.write_mp3_to(file)
    
    print(file_name + " has been downloaded to " + out_path)
    
    
      