import subprocess

NOV = 'BBB' #Name Original Video

####################### EJERCICIO-1 ################################
time_start = '00:07:05.0'
time_video = '00:00:10.0'
subprocess.run(f"ffmpeg -ss {time_start} -i EJERCICIO-5/{NOV}.mp4 -c copy -t {time_video} EJERCICIO-5/{NOV}_10s.mp4", shell=True)

####################### EJERCICIO-2 ################################

subprocess.run(f"ffmpeg -i EJERCICIO-5/{NOV}_10s.mp4 -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay EJERCICIO-5/YUVhisto_{NOV}.mp4", shell=True)

####################### EJERCICIO-3 ################################

scaleValue = ["1280:720","640:480","360:240","160:120"]
nameVideo = ["1280x720","640x480","360x240","160x120"]
for i in range(len(scaleValue)):

    subprocess.run(f"ffmpeg -i EJERCICIO-5/{NOV}_10s.mp4 -vf scale={scaleValue[i]} EJERCICIO-5/{NOV}_{nameVideo[i]}.mp4 ", shell=True)

####################### EJERCICIO-4 ################################

subprocess.run(f"ffmpeg -i EJERCICIO-5/{NOV}_10s.mp4 -ac 1 EJERCICIO-5/mono-{NOV}_10s.mp4", shell=True)
subprocess.run(f"ffmpeg -i EJERCICIO-5/mono-{NOV}_10s.mp4 -acodec mp3 -vcodec copy EJERCICIO-5/mono-mp3-{NOV}_10s.mp4", shell=True)
