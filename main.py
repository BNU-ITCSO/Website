from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pages/<url1>/<url2>')
def getPages(url1, url2):
    return render_template('pages/origin.html',
                           title=url2[:url2.__len__()-5],
                           content='pages/{}/{}'.format(url1, url2))

@app.route('/pages/<url>')
def getRootPages(url):
    en2zhDict = {
        'introduction.html': '活动介绍',
        'recruit.html': '招新计划',
        'technology.html': '技术服务'
    }

    return render_template('pages/origin.html',
                           title=en2zhDict[url],
                           content='pages/{}'.format(url))

@app.route('/')
def getIndex():
    return render_template('pages/origin.html', content='index.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
