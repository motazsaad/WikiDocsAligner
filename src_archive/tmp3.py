from html.parser import HTMLParser

class WikiExtractParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'doc':
            self.id, self.title = self.get_id(attrs)
            print(self.id, self.title)
            self.recording = True

    def handle_data(self, data):
        if self.recording:
            print("data  :", data[:100])

    def handle_endtag(self, tag):
        if tag == 'required_tag':
            self.recording = False

    def get_id(self, attrs):
        id = None
        title = None
        for attr in attrs:
            a, v = attr
            if a == 'id':
                id = v
            if a == 'title':
                title = v
        return id, title


# parser = WikiExtractParser()
# parser.feed(wiki_doc)