# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-05-13 13:19 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

from flask import Flask
app = Flask(__name__)

@app.route("/")
def mainPage():
  return "Hello World!"


