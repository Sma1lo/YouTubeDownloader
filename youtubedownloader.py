import os
import yt_dlp
import menu

"""
@author Sma1lo
"""

def download_single_video_yt_dlp(url, output_path):
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s-%(id)s.%(ext)s'),
        'ignoreerrors': True,
        'format': 'best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Error downloading {url}: {e}")


def download_playlist_yt_dlp(playlist_url, output_path):
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s-%(id)s.%(ext)s'),
        'ignoreerrors': True,
        'format': 'best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([playlist_url])
        except Exception as e:
            print(f"Error downloading playlist {playlist_url}: {e}")


def download_channel_videos_yt_dlp(channel_url, output_path):
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s-%(id)s.%(ext)s'),
        'ignoreerrors': True,
        'format': 'best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([channel_url])
        except Exception as e:
            print(f"Error downloading channel {channel_url}: {e}")


if __name__ == "__main__":
    while True:
        menu.show_menu()
        choice = input("\nEnter number: ")

        if choice == "1":
            video_url = input("Enter the video URL: ")
            output_path = input("Enter the output path (default is '.'): ") or "."
            download_single_video_yt_dlp(video_url, output_path)

        elif choice == "2":
            playlist_url = input("Enter the playlist URL: ")
            output_path = input("Enter the output path (default is '.'): ") or "."
            download_playlist_yt_dlp(playlist_url, output_path)

        elif choice == "3":
            channel_url = input("Enter the channel URL: ")
            output_path = input("Enter the output path (default is '.'): ") or "."
            download_channel_videos_yt_dlp(channel_url, output_path)

        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Try again.")
