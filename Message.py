class message():
    def __init__(self, message):
        self.chat_id=message["from"]["id"]
        if message.get('text'):
            self.type='text'
            self.value=message['text']
        else:
            self.type=False
            self.value=False
     
    def _text_response(self,mes):
        response = {
         'text' : mes 
         }
        method_name='sendMessage'
        return method_name,response
    def _invalid_res(self):
        response={
         'text' : '.....Invalid ! Please try Again Later......!'
         }
        method_name='sendMessage'
        return method_name,response
    def get_response(self):
        if(self.type and hasattr(self,'_%s_response' %self.type)):
            result=getattr(self,'_%s_response' %self.type)()
        else:
               result=getattr(self,'_invalid_res')()
        assert isinstance(result,tuple) and len(result)==2 and isinstance(result[1], dict)
         
        result[1].update({
         'chat_id' : self.chat_id
         }
         )
         
         
         
        return result



