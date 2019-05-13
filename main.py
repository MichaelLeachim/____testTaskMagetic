# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-05-13 15:11 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

import json

import fire
import logging
import pystache

from downloader import Downloader
from data_getter import DataGetter
from tools import AppConfig

class Facade(object):
  
  def __init__(self):
    logging.basicConfig(filename='log/app.log', filemode='w')
    
  def downloadData(self,save_to='workdata/data.txt'):
    conf = AppConfig()
    conf.dataGetter = DataGetter()
    conf.logging = logging
    d = Downloader(conf)
    data = d.downloadAllDataAsList()
    with open(save_to, 'w') as outfile:  
      json.dump(data, outfile)
      
  def showInTemplate(self,path="workdata/output.html",input_data='workdata/data.txt'):
    with open(input_data,"r") as datum_file:
      datum = json.load(datum_file)
      with open("templates/base.html","r") as template_file:
        template_string = template_file.read()
        with open(path,"w") as write_to:
          write_to.write(pystache.render(template_string,context=datum))
  def runHTTPServer(self,port):
    pass
  
if __name__ == '__main__':
  fire.Fire(Facade)
  
  
  



