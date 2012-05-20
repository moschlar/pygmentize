from tw.api import Widget, JSLink, CSSLink, CSSSource

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

from pprint import pprint

__all__ = ["Pygmentize"]

class MyHtmlFormatter(HtmlFormatter):
    '''Create lines that have unique name tags to allow highlighting'''
    
    def _wrap_lineanchors(self, inner):
        s = self.lineanchors
        i = 0
        for t, line in inner:
            if t:
                i += 1
                yield 1, u'<a name="%s-%d" class="%s-%d">%s</a>' % (s, i, s, i, line)
            else:
                yield 0, line

# declare your static resources here

## JS dependencies can be listed at 'javascript' so they'll get included
## before
# my_js = JSLink(modname=__name__, 
#                filename='static/pygmentize.js', javascript=[])

# my_css = CSSLink(modname=__name__, filename='static/pygmentize.css')

class Pygmentize(Widget):
    template = """<div id="${id}" class="${css_class}">${source}</div>"""

    params = ['lexer', 'source']

    css_class = 'pygmentize'

    def __init__(self, id=None, parent=None, children=[], style='default',
                 linenos=True, lineanchors='line', full=False, title=None,
                 **kw):
        """Initialize the widget here. The widget's initial state shall be
        determined solely by the arguments passed to this function; two
        widgets initialized with the same args. should behave in *exactly* the
        same way. You should *not* rely on any external source to determine
        initial state."""
        super(Pygmentize, self).__init__(id, parent, children, **kw)
        if full:
            self.template = "${source}"
        self.formatter = MyHtmlFormatter(style=style, linenos=linenos,
                                         lineanchors=lineanchors, full=full,
                                         title=title)
        self.css = [CSSSource(src=self.formatter.get_style_defs())]

    def update_params(self, d):
        """This method is called every time the widget is displayed. It's task
        is to prepare all variables that are sent to the template. Those
        variables can accessed as attributes of d."""
        super(Pygmentize, self).update_params(d)
        try:
            lexer = get_lexer_by_name(d.lexer)
            d.source = highlight(d.source, lexer, self.formatter)
        except:
            d.source = '<pre>%s</pre>' % d.source
        
