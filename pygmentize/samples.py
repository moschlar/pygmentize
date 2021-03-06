"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

from pygmentize import Pygmentize

class DemoPygmentize(Pygmentize):
    # Provide default parameters, value, etc... here
    # default = <some-default-value>
    pass

if __name__ == '__main__':
    widget = DemoPygmentize()
    print widget.display(lexer='python', source='print "Hello World!"')
    widget = DemoPygmentize(full=True)
    print widget.display(lexer='python', source='print "Hello World!"')