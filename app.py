from flask import Flask, render_template, Response

# Raspberry Pi camera module (requires picamera package)
#from camera_pi import Camera
import func

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def gen():
    while True:
        frame = func.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
