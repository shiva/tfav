from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1257832029.440026
_template_filename='/home/shvelmur/webapps/tfav/tfav/templates/main.mako'
_template_uri='/main.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n  <title>Greetings</title>\n</head>\n<body>\n\t<form name="test" method="GET" action="/main/index">\n\tTwitter Username: <input type="text" name="uname" />\n\t               <input type="submit" name="submit" value="Submit" />\n\t</form>\n\t<hr />\n  <h1>')
        # SOURCE LINE 11
        __M_writer(escape(c.user))
        __M_writer(u' likes these:</h1>\n  <table>\n')
        # SOURCE LINE 13
        for item in c.favs:
            # SOURCE LINE 14
            __M_writer(u'    <tr><td><a href="http://twitter.com/')
            __M_writer(escape(item.author))
            __M_writer(u'">')
            __M_writer(escape(item.author))
            __M_writer(u'<a></td><td>')
            context.write(item.tweet) 
            
            __M_writer(u'\n    <a href="')
            # SOURCE LINE 15
            __M_writer(escape(item.link))
            __M_writer(u'">..</a></td></tr>\n')
        # SOURCE LINE 17
        __M_writer(u'  </table>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


