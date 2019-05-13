# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-05-13 13:19 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@

from flask import Flask
from flask import request

import json
from tools import RenderCategoryResults


app = Flask(__name__)

@app.route("/")
def mainPage():
  search_string = request.args.get('search') or ""
  with open("workdata/data.txt","r") as datum_file:
    datum = json.load(datum_file)
    return RenderCategoryResults([[cat,game] for [cat,game] in datum if search_string in game.lower()])
