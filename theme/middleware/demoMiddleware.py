from asyncio.log import logger
import logging
logger = logging.getLogger(__name__)

class demoMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        logger.warning("Middleware called in new in call")
        return response

    def proces_view(self,request,view_func,view_args,view_kwargs):
        logger.warning("Middleware called new")
        #This code is executed just before the view is called
        pass
    def process_exception(self,request,exception):
            #This code is executed if an exception is raised
        pass
    def process_template_response(self,request,response):
            #this code is executed if the response contains the render() method
        return response