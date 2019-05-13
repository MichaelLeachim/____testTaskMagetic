# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-05-13 13:20 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@


class Downloader(object):
  
  # Inject requests 
  def __init__(self,conf):
    self.dataGetter  = conf.dataGetter
    
  def getPage(self,category):
    # import ipdb; ipdb.set_trace();
    return self.dataGetter.get("https://play.google.com/store/apps/category/"+category)
  
  def parseListOfCategories(self,category):
    pass
  
  def getListOfCategories(self):
    import ipdb; ipdb.set_trace();    
    return self.dataGetter.get("https://play.google.com/store/apps/category/GAME")
    
  def getAllGamesPerPage(page):
    pass
    
  

