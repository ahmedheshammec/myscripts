@echo off
set /p "playlist_url=Enter playlist URL: "
set /p "playlist_name=Enter playlist name: " 

if "%playlist_name%" == "" (
  echo No playlist name entered. Exiting.
  exit /b 1
)

mkdir "%playlist_name%"
cd "%playlist_name%"

yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" --merge-output-format mp4 --output "%%(playlist_index)s.%%(title)s.%%(ext)s" --download-archive archive.txt "%playlist_url%"
pause
