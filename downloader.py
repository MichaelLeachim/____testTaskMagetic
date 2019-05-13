# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-05-13 13:20 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

import re

class Downloader(object):
  
  ## Do not use CSS/XPATH because there is no requirement for it 
  ## in the test task + Google uses dynamic HTML classes to
  ## avoid scrappers
  
  storegex = re.compile(u"/store/apps/details\?id\=(.*?)\"",re.MULTILINE)
  categorygex = re.compile(u"/store/apps/category/(GAME_.*?)\"",re.MULTILINE)
  
  # Inject dataGetter module
  def __init__(self,conf):
    self.dataGetter  = conf.dataGetter
    
  def getGamesList(self,category):
    return self.getList("https://play.google.com/store/apps/category/"+category,self.storegex)
  
  def getCategoriesList(self):
    return self.getList("https://play.google.com/store/apps/category/GAME",self.categorygex)
  
  ## Get all distinct items that match categorygex  
  ## Get all distinct items that match storegex
  def getList(self,link,selector):
    res,err = self.dataGetter.get(link)
    if (err != None):
      return [],err
    result = set()
    for item in selector.finditer(res):
      point = item.groups()
      if len(point)>0:
        result.add(point[0])
    return sorted(list(result)),None
