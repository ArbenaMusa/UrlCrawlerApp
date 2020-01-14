from lxml import html
import requests

from MyApp import MyApp


class URLCrawler:
    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        self.current_depth = 0
        self.depth_links = []
        self.apps = []

    def get_app_from_link(self, link):
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)
        linka = tree.xpath('//*/a/@href')
        links = []
        for li in linka:
            if len(li) != 0:
                if li[0] == '/':
                    li = link + li
                if li not in links and li[0] != '#' and li[0] != '?':
                    links.append(li)

        app = MyApp(links)
        return app

    def crawl(self):
        app = self.get_app_from_link(self.starting_url)
        self.apps.append(app)
        self.depth_links.append(app.links)

        while self.current_depth < self.depth:
            current_links = []
            for link in self.depth_links[self.current_depth]:
                current_app = self.get_app_from_link(link)
                current_links.extend(current_app.links)
                self.apps.append(current_app)
            self.current_depth += 1
            self.depth_links.append(current_links)

    def get_related_links(self):
        return self.depth_links
