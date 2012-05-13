from tw.core.testutil import WidgetTestCase
from pygmentize import *

class TestWidget(WidgetTestCase):
    # place your widget at the TestWidget attribute
    TestWidget = Pygmentize
    # Initilization args. go here 
    widget_kw = dict(lineanchors= 'myline',
                     lexer='python', source='print "Hello World!"')

    def test_render(self):
        # Asserts 'foo' and 'test' (the test widget's id) appear in rendered 
        # string when 'foo' is passed as source code to render
        self.assertInOutput(['foo', 'test'], source="foo")
        # Asserts 'ohlalala' does not appear in rendered string when render 
        # is called without args
        self.assertNotInOutput(['ohlalala'])

    def test_highlight(self):
        # Assert that highlighting worked by checking for high
        self.assertInOutput(['<table class="highlighttable">', '<div class="highlight">'])

    def test_lineanchor(self):
        # Assert that our lineanchor is used
        self.assertInOutput(['name="myline-1"', 'class="myline-1"'])
        # And not the default one
        self.assertNotInOutput(['name="line-1"', 'class="line-1"'])

class TestWidgetFull(WidgetTestCase):
    # place your widget at the TestWidget attribute
    TestWidget = Pygmentize
    # Initilization args. go here 
    widget_kw = dict(full=True, title='I am the title, yeah',
                     lexer='python', source='print "Hello World!"')

    def test_render(self):
        # Since we render the full page, no surrounding div with the id
        # should exist
        self.assertNotInOutput(['<div id="test"'])

    def test_highlight(self):
        # Assert that a whole html page exists
        self.assertInOutput(['<html>', '<style type="text/css">', '</style>',
                             '<table class="highlighttable">', '<div class="highlight">',
                             '</html>'
                             ])

    def test_title(self):
        # Assert that the title got rendered
        self.assertInOutput(['<title>I am the title, yeah</title>',
                             '<h2>I am the title, yeah</h2>'])

class TestWidgetNoLineNos(WidgetTestCase):
    # place your widget at the TestWidget attribute
    TestWidget = Pygmentize
    # Initilization args. go here 
    widget_kw = dict(linenos= False,
                     lexer='python', source='print "Hello World!"')

    def test_highlight(self):
        # Assert that no linenos column exists
        self.assertNotInOutput(['<td class="linenos">'])
