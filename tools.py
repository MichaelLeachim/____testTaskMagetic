# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-05-13 13:29 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

import pystache

class AppConfig:
  pass

def RenderCategoryResults(datum):
  with open("templates/base.html","r") as template_file:
    template_string = template_file.read()
    return pystache.render(template_string,context=datum)
  
  
  
