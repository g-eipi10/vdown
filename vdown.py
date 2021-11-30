import subprocess

print('\n=================================\nDownload videos by yt-dlp - v2\n=================================')

# Update yt-dlp
update = f"./yt-dlp.exe -U"
subprocess.call(['powershell', update])

while True:
    print('\nPlease paste YouTube link here or press Enter to exit')
    print('Vui long dan link YouTube vao day hoac nhan Enter de thoat')
    vid = input('>>> ')
    if vid == '':
        break
    else:
        vid = vid.replace('"','')
        vid = vid.split('&')[0]
        print(f'--- {vid} ---')

        command = f"./yt-dlp.exe -N 32 --remux-video mp4 --ffmpeg-location ./ffmpeg.exe {vid}"
        subprocess.call(['powershell', command])

        print('\n\n--------------------------\nFinish. Enjoy the video\n--------------------------')
        # input('Enter to exit...')
