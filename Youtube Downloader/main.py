
import os
import yt_dlp as youtube_dl

def download_video(url, path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    url = input("Masukkan URL video YouTube: ")
    path = input("Masukkan path untuk menyimpan video: ")
    download_video(url, path)
    print("Video berhasil diunduh!")

if __name__ == "__main__":
    main()
