from modules.ytdl import Yt_dl
from modules.scdl import Sc_dl

if __name__ == "__main__":
  
  sc_or_yt = str(input("Use Youtube[y] or Soundcloud[s]?"))
  url = str(input("What is the url you would like to download from youtube or soundcloud?"))
  if sc_or_yt.strip() == "y":
    ytdl_obj = Yt_dl(url)
    v_or_a = str(input("Video[v] or audio[a]?"))
    if v_or_a.strip() == "a":
      ytdl_obj.download_audio()
    elif v_or_a.strip() == 'v':
      ytdl_obj.download_video()
      
  elif sc_or_yt.strip() == "s":
    scdl_obj = Sc_dl(url)
    scdl_obj.download_audio()