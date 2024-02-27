from sclib import SoundcloudAPI, Track, Playlist
import os
class Sc_dl:
  def __init__(self, url):
    self.api = SoundcloudAPI()
    self.track = self.api.resolve(url)
    assert type(self.track) is Track
    
  def progress_function(self, stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f'Downloading : {pct_completed:.2f}%', end='\r')
    
  def download_audio(self):
    out_path = os.path.join(os.path.expanduser("~"), "wtv_mp3")
    artist_name = "".join(ch for ch in self.track.artist if ch.isalnum() or ch == " ").replace("/","_")
    track_name = "".join(ch for ch in self.track.title if ch.isalnum() or ch == " ").replace("/", "_")
    file_name = f'{artist_name} - {track_name}.mp3'
    file_path = os.path.join(out_path, file_name)
    
    with open(file_path, "wb+") as file:
      self.track.write_mp3_to(file)
    
    print(file_name + " has been downloaded to " + out_path)
    
    
      