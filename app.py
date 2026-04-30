from flask import Flask, render_template, request, redirect, url_for, session
import os
from detector import AnimalDetector

app = Flask(__name__)
app.secret_key = "wildlife_security_key"
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

detector = AnimalDetector('best.pt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return redirect(request.url)
    
    file = request.files['video']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'input_video.mp4')
        output_img = 'static/result.jpg'
        file.save(filepath)
        
        # Process full video
        results = detector.process_video(filepath, output_img)
        
        session['detections'] = results
        session['detected_names'] = ", ".join(list(set([d['label'] for d in results])))
        return redirect(url_for('result'))

@app.route('/result')
def result():
    detections = session.get('detections', [])
    names = session.get('detected_names', 'None')
    return render_template('result.html', detections=detections, names=names)

@app.route('/reset')
def reset():
    session.clear()
    if os.path.exists('static/result.jpg'):
        os.remove('static/result.jpg')
    return redirect(url_for('index'))

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True, port=5000)