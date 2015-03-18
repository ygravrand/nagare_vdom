from nagare import presentation, wsgi, component

from .vdom_renderer import VDomRenderer
from .root_component import RootComponent

class Nagare_vdom(object):
    
    def __init__(self):
        self.counter = component.Component(Counter())
        
        
class Counter(object):
    
    def __init__(self):
        self.value = 0
        
    def incr(self):
        self.value += 1
        
    def decr(self):
        self.value -= 1


@presentation.render_for(Nagare_vdom)
def render(self, h, comp, *args):

    h.head << h.head.title('Up and Running !')

    h.head.css_url('/static/nagare/application.css')
    h.head.css('defaultapp', '#main { margin-left: 20px; padding-bottom: 100px; background: url(/static/nagare/img/sakura.jpg) no-repeat 123px 100% }')
    
    h.head.javascript_url('bundle.js')
    with h.div(id='body'):
        h << h.a(h.img(src='/static/nagare/img/logo.png'), id='logo', href='http://www.nagare.org/', title='Nagare home')

        with h.div(id='content'):
            h << h.div('Congratulations!', id='title')

            with h.div(id='main'):
                h << h.h1('Your application is running')

                h << 'This is an async counter: ' << self.counter.render(h.AsyncRenderer())

    with h.div(id='footer'):
        with h.table:
            with h.tr:
                h << h.th('About Nagare')
                h << h.th('Community')
                h << h.th('Learn', class_='last')

            with h.tr:
                with h.td:
                    with h.ul:
                        h << h.li(h.a('Description', href='http://www.nagare.org/trac/wiki/NagareDescription'))
                        h << h.li(h.a('Features', href='http://www.nagare.org/trac/wiki/NagareFeatures'))
                        h << h.li(h.a('Who uses Nagare?', href='http://www.nagare.org/trac/wiki/WhoUsesNagare'))
                        h << h.li(h.a('Licence', href='http://www.nagare.org/trac/wiki/NagareLicence'))

                with h.td:
                    with h.ul:
                        h << h.li(h.a('Blogs', href='http://www.nagare.org/trac/blog'))
                        h << h.li(h.a('Mailing list', href='http://www.nagare.org/trac/wiki/MailingLists'))
                        h << h.li(h.a('IRC', href='http://www.nagare.org/trac/wiki/IrcChannel'))
                        h << h.li(h.a('Bug report', href='http://www.nagare.org/trac/wiki/BugReport'))

                with h.td(class_='last'):
                    with h.ul:
                        h << h.li(h.a('Documentation', href='http://www.nagare.org/trac/wiki'))
                        h << h.li(h.a('Demonstrations portal', href='http://www.nagare.org/portal'))
                        h << h.li(h.a('Demonstrations', href='http://www.nagare.org/demo'))
                        h << h.li(h.a('Wiki Tutorial', href='http://www.nagare.org/wiki'))

    return h.root


@presentation.render_for(Counter)
def render_counter_async(self, h, comp, *args):
    with h.p:
        h << self.value
        h << h.a('+').action(self.incr)
        h << ' '
        h << h.a('-').action(self.decr)
    return h.root


class WSGIApp(wsgi.WSGIApp):
    
    renderer_factory = VDomRenderer
    
    def _phase1(self, root, request, response, callbacks):
        # Don't return any render function
        super(WSGIApp, self)._phase1(root, request, response, callbacks)

# ---------------------------------------------------------------


app = WSGIApp(lambda * args: RootComponent(Nagare_vdom(*args)))