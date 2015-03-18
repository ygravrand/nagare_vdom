import types
from peak.rules import when
from nagare import presentation, component

class RootComponent(component.Component):
    pass

@when(presentation.render, (RootComponent, object, object, int))
@when(presentation.render, (RootComponent, object, object, types.NoneType))
@when(presentation.render, (RootComponent, object, object, str))
def render(next_method, self, renderer, comp, model):
    res = next_method(self, renderer, comp, model)
    return renderer.render_vdom_js(res)
