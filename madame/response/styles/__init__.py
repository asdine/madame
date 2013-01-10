from madame.response.styles.hateoas import Hateoas

def default_renderer_funcs():
    renderers = {
        'hateoas' : Hateoas
    }
    return renderers
