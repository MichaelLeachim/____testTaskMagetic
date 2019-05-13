# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-05-13 13:35 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

import requests

class DataGetter(object):
  
  # downloads data from the URL
  # Returns tuple content,error
  # If everything is ok, error == None
  @staticmethod
  def get(link,params=None, **kwargs):
    try:
      result = requests.get(link,params=params,**kwargs)
      if result.ok:
        # import ipdb;ipdb.set_trace()
        # print type(result.content)
        return (result.content.decode("utf8"),None)
      return result.content,result.reason
    except Exception as e:
      return (None, "Error: " + str(e))
    
    
      

