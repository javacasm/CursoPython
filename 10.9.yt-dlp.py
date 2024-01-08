# Descargar vídeo de youtube


## 

import yt_dlp


yt_opt = {}

video_url = input('Vídeo a descargar: ')

ytd = yt_dlp.YoutubeDL(yt_opt)

ytd.download([video_url])
             
             