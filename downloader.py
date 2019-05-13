# -*- coding: utf-8 -*-
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
  
  # Inject dataGetter,logger module
  def __init__(self,conf):
    self.dataGetter  = conf.dataGetter
    self.logging      = conf.logging
    
  def getGamesList(self,category):
    return self._getList("https://play.google.com/store/apps/category/"+category,self.storegex)
  
  def getCategoriesList(self):
    res,err = self._getList("https://play.google.com/store/apps/category/GAME",self.categorygex)
    if err == None:
      return  ["GAME"] + res, err
    return res,err
  
  ## Get all distinct items that match categorygex  
  ## Get all distinct items that match storegex
  def _getList(self,link,selector):
    res,err = self.dataGetter.get(link)
    if (err != None):
      return [],err
    result = set()
    for item in selector.finditer(res):
      point = item.groups()
      if len(point)>0:
        result.add(point[0])
    return sorted(list(result)),None
  
  # Will download needed data in specified format
  # Will log potential errors.
  # Will return [] as a result
  # Will return partially, if cannot download
  # some of the links. Will log them on Fatal level
  def downloadAllDataAsList(self):
    cats,err = self.getCategoriesList()
    if err != None:
      self.logging.fatal("Cannot get categories list: ",err)
      return []

    result = []
    
    for cat in cats:
      games, err = self.getGamesList(cat)
      if err != None:
        self.logging.fatal("Cannot get games on cat: ",cat," with err: ",err)
        continue
      for game in games:
        result.append([cat,game])
    return result
  
  # pprint according to a spec
  def downloadAllData(self):
    result = []
    for item in self.downloadAllDataAsList():
      result.append(item[0]+"/"+item[1])
    return result  
