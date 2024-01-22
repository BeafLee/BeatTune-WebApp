from flask import Flask, render_template, request, redirect, send_file
from werkzeug.utils import secure_filename
import os
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
    option = request.form['btn']

    url = request.form['url']
    video = YouTube(url)
    
    if option == 'mp4':            
        print("option mp4")
        
        # Obtener la mejor resolución disponible
        stream = video.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

        # Descargar el video
        url_video = stream.download(path, 'video.mp4')

        # Devolver el video como un archivo adjunto directamente al navegador
        return send_file(
            url_video,
            as_attachment= True,
            download_name= secure_filename(f"{video.title}.{option}"),
            mimetype='video/mp4'
        )
    
    elif option == 'mp3':
        print('option mp3')
        
        # Obtener la mejor resolución disponible
        stream = video.streams.filter(only_audio=True).first()

        # Descargar el video
        url_video = stream.download(path, 'audio.mp3')

        # Devolver el video como un archivo adjunto directamente al navegador
        return send_file(
            url_video,
            as_attachment=True,
            download_name= secure_filename(f"{video.title}.{option}"),
            mimetype='audio/mp3'
        )
    




if __name__ == '__main__':
    app.run(host='localhost', debug=True)