# -*- coding: utf-8 -*-
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-05-13 13:50 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@
from data_getter import DataGetter

def testDataGetter():
  
  datum,err = DataGetter.get("https://play.google.com/store/apps/category/GAME_CASUAL")
  assert err == None

  datum,err = DataGetter.get("https://aslkdjalksjdklajsdlakjsd.com")
  assert err != None
  assert datum == None
