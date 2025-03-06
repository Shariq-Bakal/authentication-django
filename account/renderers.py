from rest_framework import renderers
import json

class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8' #UTF-8 supports all characters (English, Arabic, Hindi, Chinese, etc.).
    #Prevents encoding errors when handling non-English text.
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if "ErrorDetail" in str(data):
            response = json.dumps({'errors':data}) # error detail is found in data it will throw an error. You can get this error when you do not provide email and password and you can see this error by priting serializers.errors in view
        else:
            response = json.dumps(data) # is everythin works fine this will work
        return response