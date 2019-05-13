# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-05-13 13:22 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

from downloader import Downloader
from tools import AppConfig
import requests

class MockDataGetter(object):
  
  def get(self,url):
    if url == "https://play.google.com/store/apps/category/GAME":
      with open("testdata/GAME","r") as file:
        return (file.read(),None)
    return ("","Error: cannot get the source on a mock object"  )
  
def testDownloader():
  conf = AppConfig()
  conf.dataGetter = MockDataGetter()
  # import ipdb; ipdb.set_trace();
  d = Downloader(conf)
