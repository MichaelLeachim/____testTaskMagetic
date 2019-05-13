# -*- coding: utf-8 -*-
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-05-13 13:51 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@



class MockDataGetter(object):
  def get(self,url):
    try:
      # import ipdb;ipdb.set_trace()
      with open("testdata/"+url.split("/")[-1],"r") as file:
        res = file.read()
        res.decode("utf8")
        return res, None
    except:
      return (u"","Error: cannot get the source on a mock object"  )
