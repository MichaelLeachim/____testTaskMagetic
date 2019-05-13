# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ Copyright (c) Michael Leahcim                                                      @
# @ You can find additional information regarding licensing of this work in LICENSE.md @
# @ You must not remove this notice, or any other, from this software.                 @
# @ All rights reserved.                                                               @
# @@@@@@ At 2019-05-13 13:22 <thereisnodotcollective@gmail.com> @@@@@@@@@@@@@@@@@@@@@@@@


import requests,logging

from downloader import Downloader
from data_getter import DataGetter

from tools import AppConfig
from mocks import MockDataGetter

def testGetCategoriesList():
  conf = AppConfig()
  conf.dataGetter = MockDataGetter()
  conf.logging    = logging
  d = Downloader(conf)
  
  res,err = d.getCategoriesList()
  assert err == None
  assert res == ['GAME','GAME_ACTION', 'GAME_ADVENTURE', 'GAME_ARCADE', 'GAME_BOARD', 'GAME_CARD', 'GAME_CASINO', 'GAME_CASUAL', 'GAME_EDUCATIONAL', 'GAME_MUSIC', 'GAME_PUZZLE', 'GAME_RACING', 'GAME_ROLE_PLAYING', 'GAME_SIMULATION', 'GAME_SPORTS', 'GAME_STRATEGY', 'GAME_TRIVIA', 'GAME_WORD']
  
def testDownloadAllData():
  conf = AppConfig()
  conf.dataGetter = MockDataGetter()
  conf.logging = logging
  d = Downloader(conf)
  data = d.downloadAllData()
  assert len(str(data)) ==  49850
  
def testGetGamesList():
  conf = AppConfig()
  conf.dataGetter = MockDataGetter()
  conf.logging = logging
  d = Downloader(conf)
  
  res,err = d.getGamesList("GAME")
  assert err == None
  assert res ==  ['air.com.hypah.io.slither', 'air.com.lunime.gachalife', 'air.com.sgn.cookiejamblast.gp', 'bling.crush.match3.free.android', 'bubbles.pop.power', 'com.aim.racing', 'com.amanotes.beathopper', 'com.ansangha.drdriving', 'com.azurgames.stackball', 'com.bethsoft.blade', 'com.bigduckgames.flow', 'com.bitmango.go.wordcookies', 'com.budgestudios.googleplay.BarbieDreamhouse', 'com.budgestudios.googleplay.DCSuperHeroGirls', 'com.coldfiregames.spaceclicker', 'com.ea.game.pvz2_na', 'com.ea.game.pvzfree_row', 'com.ffgames.racingincar2', 'com.fingersoft.hcr2', 'com.fungames.blockcraft', 'com.hutchgames.formularacing', 'com.hypemasters.dunk3d', 'com.igg.android.craftlegend', 'com.jdpapps.wordsearch', 'com.kiloo.subwaysurf', 'com.king.bubblewitch3', 'com.king.candycrush4', 'com.king.candycrushsaga', 'com.king.candycrushsodasaga', 'com.lemongame.klondike.solitaire', 'com.mastercomlimited.racethetraffic', 'com.mgc.runnergame', 'com.mojang.minecraftpe', 'com.more.dayzsurvival.gp', 'com.mrxw.android.ltgames', 'com.my.evolution2', 'com.netease.hdjygb', 'com.nexon.godzilla', 'com.nianticlabs.hpwu.prod', 'com.nyouinc.latalew', 'com.orangeapps.piratetreasure', 'com.outfit7.mytalkingangelafree', 'com.outfit7.mytalkingtom2', 'com.playgendary.kickthebuddy', 'com.playrix.township', 'com.pnixgames.bowmax', 'com.razmobi.monstertrucks2', 'com.roblox.client', 'com.robtopx.geometryjump', 'com.sgn.geniesandgems.gp', 'com.sgn.pandapop.gp', 'com.skgames.trafficracer', 'com.skgames.trafficrider', 'com.smilerlee.klondike', 'com.spacegame.basic3', 'com.spacegame.solitaire.basic', 'com.supercell.clashroyale', 'com.topebox.evilrivals', 'com.wordsmobile.RealBikeRacing', 'es.socialpoint.wordlife', 'jpark.AOS5', 'me.pou.app', 'net.peakgames.toonblast']



  
  

  
