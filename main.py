# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-05-13 15:11 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

import json

import fire
import logging
import mustache

from downloader import Downloader
from data_getter import DataGetter

class Facade(object):
  
  def __init__(self):
    logging.basicConfig(filename='log/app.log', filemode='w')
    
  def downloadData(self,save_to='workdata/data.txt'):
    conf = AppConfig()
    conf.dataGetter = DataGetter()
    conf.logging = logging
    d = Downloader(conf)
    data = d.downloadAllData()
    with open(save_to, 'w') as outfile:  
      json.dump(data, outfile)
      
  def showInTemplate(self,path="workdata/output.html",input_data='workdata/data.txt'):
    pass
  
  def runHTTPServer(self,port):
    pass
  
if __name__ == '__main__':
  fire.Fire(Calculator)
  
  
  



