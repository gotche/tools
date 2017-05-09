from flask import Flask, abort, make_response
app = Flask(__name__)


@app.route('/videos/<video_id>')
def view_video(video_id):
    # check logged-in, eligible to see video, etc
    # In this code sample we will just let see videos with a concrete id
    if int(video_id) > 100:
        abort(404)

    # the media_url is the resource uri in the remote service
    media_url = f'http://mediaserver/videos/{video_id}'

    # we will use the internal redirection to send the resource url
    redirect_path = f'/raw_videos/url/{media_url}'

    # return an empty response with X-Accel-Redirect header
    response = make_response('')
    response.headers['X-Accel-Redirect'] = redirect_path
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
