"""
module.py

Example of a LWPCMS module/plugin.
"""
from lwpcms.moduling.moduling import LWPCMSModule
from lwpcms.api.constants import hooks


"""
SampleModule

Example module class.

Adds an element to the <head> and the <body>.
It also appends a string to posts that is about to be published.
"""
class SampleModule(LWPCMSModule):
    
    def __init__(self):
        # You need to inherit the initialization from LWPCMSModule
        # in order for your plugin to work.
        super().__init__()
        
        # Register your events here.
        # Here, I have registered events for the layout and also
        # when a post is about to be published.
        self.register_event(hooks['layout_head'], self.layout_head)
        self.register_event(hooks['layout_footer'], self.layout_footer)
        self.register_event(hooks['post_publish'], self.post_publish)
        self.register_event(hooks['admin_sidenav'], self.admin_sidenav)
        self.register_event(hooks['site_request'], self.site_request)

    def layout_head(self, data):
        # Here I am appending some data to the <head> element of the document.
        return '<script>console.log("test");</script>'


    def layout_footer(self, data):
        # Here I am appending some data to the <footer> element of the document.
        return '<div style="display:none;">SampleModule</div>'


    def post_publish(self, data):
        # Here I am modifying the title of a post that is about to be published.
        data['post']['title'] += ' ~ SampleModule'


    def admin_sidenav(self, data):
        # Here I am adding a new button to the admin sidenav.
        data['nav']['buttons'].append(
                    {
                        "label": "SampleModule",
                        "svg": "drive_file.svg",
                        "href": "http://www.example.org/"
                    }
                )


    def site_request(self, data):
        # Here I am adding a key with an array as a value in to the global
        # site request.
        # This data can later be used and collected inside a template.
        data['package']['artists'] = ['Lindsey Stirling', 'Jordan Rudess']


# At the end of your module.py file, you need to create an instance of your
# module object.
# If you don't, your plugin won't work.
module = SampleModule()
