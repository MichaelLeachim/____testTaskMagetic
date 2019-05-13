# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-05-13 13:22 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@


import requests

from downloader import Downloader
from tools import AppConfig
from mocks import MockDataGetter

def testGetCategoriesList():
  conf = AppConfig()
  conf.dataGetter = MockDataGetter()
  d = Downloader(conf)
  
  res,err = d.getCategoriesList()
  assert err == None
  assert res ==  ['GAME_ACTION', 'GAME_ADVENTURE', 'GAME_ARCADE', 'GAME_BOARD', 'GAME_CARD', 'GAME_CASINO', 'GAME_CASUAL', 'GAME_EDUCATIONAL', 'GAME_MUSIC', 'GAME_PUZZLE', 'GAME_RACING', 'GAME_ROLE_PLAYING', 'GAME_SIMULATION', 'GAME_SPORTS', 'GAME_STRATEGY', 'GAME_TRIVIA', 'GAME_WORD']
  
def testGetGamesList():
  conf = AppConfig()
  conf.dataGetter = MockDataGetter()
  d = Downloader(conf)
  
  res,err = d.getGamesList("GAME")
  assert err == None
  assert res == ['air.com.hypah.io.slither', 'air.com.lunime.gachalife', 'air.com.sgn.cookiejamblast.gp', 'bling.crush.match3.free.android', 'bubbles.pop.power', 'com.amanotes.beathopper', 'com.ansangha.drdriving', 'com.assassingames.ninjafrogrope', 'com.azurgames.stackball', 'com.bethsoft.blade', 'com.bigduckgames.flow', 'com.bitmango.go.wordcookies', 'com.brokenreality.planemerger.android', 'com.budgestudios.googleplay.BarbieDreamhouse', 'com.budgestudios.googleplay.DCSuperHeroGirls', 'com.coldfiregames.spaceclicker', 'com.combineinc.streetracing.driftthreeD', 'com.ea.game.pvz2_na', 'com.ffgames.racingincar2', 'com.flyairup.matchgame.JewelStarBlaze', 'com.fungames.blockcraft', 'com.housepaint.game', 'com.hutchgames.formularacing', 'com.hypemasters.dunk3d', 'com.igg.android.craftlegend', 'com.ivy.galaxyshooting.sky', 'com.kiloo.subwaysurf', 'com.king.bubblewitch3', 'com.king.candycrushsaga', 'com.king.candycrushsodasaga', 'com.lego.bricksmore', 'com.lemongame.klondike.solitaire', 'com.mojang.minecraftpe', 'com.more.dayzsurvival.gp', 'com.mrxw.android.ltgames', 'com.my.evolution2', 'com.netease.hdjygb', 'com.nexon.godzilla', 'com.nianticlabs.hpwu.prod', 'com.nyouinc.latalew', 'com.orangeapps.piratetreasure', 'com.outfit7.mytalkingangelafree', 'com.outfit7.mytalkingtom2', 'com.playgendary.kickthebuddy', 'com.pnixgames.bowmax', 'com.roblox.client', 'com.robtopx.geometryjump', 'com.rovio.angrybirds', 'com.rovio.angrybirdsrio', 'com.sgn.geniesandgems.gp', 'com.sgn.pandapop.gp', 'com.smilerlee.klondike', 'com.spacegame.basic3', 'com.spacegame.solitaire.basic', 'com.supercell.clashroyale', 'com.supercell.hayday', 'com.topebox.evilrivals', 'com.word.game.fun.puzzle.prison.escape.captain', 'es.socialpoint.wordlife', 'jpark.AOS5', 'me.pou.app', 'mini.block.craft.free.mc', 'net.peakgames.toonblast']


  
  

  
