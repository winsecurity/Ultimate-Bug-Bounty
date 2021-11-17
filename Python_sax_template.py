import sys, string

from xml.sax import saxutils, handler, make_parser


class ContentGenerator(handler.ContentHandler):

    def __init__(self, out = sys.stdout):
        handler.ContentHandler.__init__(self)
        
    def startDocument(self):
        print 'start'

    def startElement(self, name, attrs):
        print 'start', name
        for attr_name, value in attrs.items():
            print attr_name, value

    def endElement(self, name):
        print 'end', name

    def characters(self, content):
        print content

    def ignorableWhitespace(self, content):
        print 'whitespace', '"', content, '"'
        
    def processingInstruction(self, target, data):
        print 'processing instruction', target, data

if __name__ == '__main__':        
    parser = make_parser()
    parser.setContentHandler(ContentGenerator())
    parser.parse(sys.argv[1])