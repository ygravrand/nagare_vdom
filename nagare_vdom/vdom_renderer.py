from nagare.namespaces import xhtml, xhtml_base
from nagare.namespaces.xml import TagProp
from nagare.namespaces.xhtml5 import Renderer, AsyncRenderer
from nagare.ajax import ViewToJs, javascript_dependencies

    
def generate_action(self, renderer, action, with_request):
    act = renderer.register_callback(self._actions[0], action, with_request)
    return '%s;_a;%s' % (renderer.add_sessionid_in_url(sep=';'), act)
    
class A(xhtml.A):

    _actions = (4, None, 'data-nagare-callback')

    def async_action(self, renderer, action, with_request):
        """Register an asynchronous action

        In:
          - ``renderer`` -- the current renderer
          - ``action`` -- action
          - ``with_request`` -- will the request and response objects be passed to the action?
        """
        action = generate_action(self, renderer, action, with_request)
        
        self.set(self._actions[2], action)
        self.set('class', ' '.join([elt for elt in self.get('class', ''), 'nagare-callback' if elt]))
        self.set('href', '#')
        javascript_dependencies(renderer)
        renderer.head.javascript_url('/static/nagare/ajax.js')
        renderer.head.javascript_url('gator.min.js')
        renderer.head.javascript_url('vdom_ajax.js')


    _async_action = async_action


class VDomRenderer(Renderer):
    
    a = TagProp('a', set(xhtml_base.allattrs + xhtml_base.focusattrs + ('charset', 'type', 'name', 'href', 'hreflang', 'rel', 'rev', 'shape', 'coords', 'target', 'oncontextmenu')), A)
    
    def AsyncRenderer(self, *args, **kw):
        """Create an associated asynchronous HTML renderer

        Return:
          - a new asynchronous renderer
        """
        # If no arguments are given, this renderer becomes the parent of the
        # newly created renderer
        if not args and not kw:
            args = (self,)

        return VDomAsyncRenderer(*args, **kw)
    
    def render_vdom_js(self, output):
        return output
    
class VDomAsyncRenderer(AsyncRenderer, VDomRenderer):
        
    def render_vdom_js(self, output):
        return ViewToJs('nagare_vdom_result', '', self, output)
    
    