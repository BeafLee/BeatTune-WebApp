from flask import Flask, render_template, request, redirect, send_file
import os
import io
import moviepy.editor as mp
from pytube import YouTube

url_video = "https://www.youtube.com/watch?v=bguUc2ZhNaY"

app = Flask(__name__)

path = os.getcwd() + '/download/'

@app.route('/')
def home():
    return render_template('index.html')

   

@app.route('/download/mp4', methods=['POST'])
def mp4_downloader():
    print("into")
    url = request.form['url']
    print(url)

    video = YouTube(url)

    # Obtener la mejor resolución disponible
    stream = video.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

    # Descargar el video
    url_video = stream.download(path, 'video.mp4')

    # Devolver el video como un archivo adjunto directamente al navegador
    return send_file(
        url_video,
        as_attachment=True,
        download_name=f"{video.title}.mp4",
        mimetype='video/mp4'
    )



if __name__ == '__main__':
    app.run(host='localhost', debug=True)