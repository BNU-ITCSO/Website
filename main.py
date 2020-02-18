from flask import Flask, render_template
from server.En2ZhDict import *

app = Flask(__name__)

@app.route('/pages/<url1>/<url2>')
def getPages(url1, url2):
    return render_template('pages/origin.html',
                           title=En2ZhDictForPages(url2),
                           content='pages/{}/{}'.format(url1, url2))

@app.route('/pages/<url>')
def getRootPages(url):
    return render_template('pages/origin.html',
                           title=En2ZhDictForRootPages[url],
                           content='pages/{}'.format(url))

@app.route('/')
def getIndex():
    return render_template('pages/origin.html', content='index.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
