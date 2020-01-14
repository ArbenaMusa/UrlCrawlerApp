from flask import Flask, render_template, request, redirect, url_for

from UrlCrawler import URLCrawler

app = Flask(__name__)


@app.route('/')
def get_crawl_page():
    return render_template('index.html', title='URL-Crawling')


@app.route('/index.html', methods=['GET', 'POST'])
def getcrawl():
    error = ""
    if request.method == 'POST':
        givenUrl = request.form['givenUrl']
        givenDepth = int(request.form['givenDepth'])

    crawler = URLCrawler(givenUrl, givenDepth)

    crawler.crawl()
    links = crawler.get_related_links()
    for app in crawler.apps:
        print(app)
    return render_template('index.html', len = len(links), links = links)


if __name__ == '__main__':
    app.run()
