# xbmc-addon-sfvideoportal
An addon for xbmc providing access to the SF videoportal from srf.ch

It is the same, that you can find in the mindmade repository, with added feature to go back in time from shows.

Here a quick write up, what the plugin actually does for future reference. 

You need to check the source of this readme.md for the details of the SRF webpage and the streams. I honestly have no time to bother with the syntax of this file.

#Shows
Shows listed at: 
http://www.srf.ch/player/tv/sendungen

Each show has those parts:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<li class="az_item pos_0"><a href="/player/tv/sendung/aeschbacher?id=0a7932df-dea7-4d8a-bd35-bba2fe2798b5"><img class="az_thumb retina_image" src="http://ws.srf.ch/asset/image/audio/1aefee2d-e66b-4412-b9a6-46833b0ea648/WEBVISUAL/1417537275000.jpg/scale/width/144" data-src2x="http://ws.srf.ch/asset/image/audio/1aefee2d-e66b-4412-b9a6-46833b0ea648/WEBVISUAL/1417537275000.jpg/scale/width/300" width="144" height="81" alt="Aeschbacher" /></a><h3><a class="sendung_name" href="/player/tv/sendung/aeschbacher?id=0a7932df-dea7-4d8a-bd35-bba2fe2798b5">Aeschbacher</a></h3><p class="az_description">Talkshow mit Kurt Aeschbacher aus der Labor-Bar in Zürich-West.</p><div class="last_episode"><div class="kamera_icon_big_light"></div><a href="/player/tv/quicklink/0a7932df-dea7-4d8a-bd35-bba2fe2798b5" class="last_episode_link">Letzte Sendung ansehen</a></div></li>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Shows divided by:
```
 <a class="sendung_name" href="/player/tv/sendung/aeschbacher?id=0a7932df-dea7-4d8a-bd35-bba2fe2798b5">Aeschbacher</a>
```

#Episodes
##Episodes divded by:
```
<li class="sendung_item">
```

##Titel:
```
<div class="title_date">Aeschbacher vom 11.12.2014, 22:24 Uhr</div>
```

##Description:
```
<div class="description">Vollen Einsatz geben: This Schenkel, Wildhüter der Stadt Zürich, Profiboxerin Nicole Boss, Rotkreuz-Pflegefachfrau Sabine Hediger und Vollblutmusiker Karl Rechsteiner. </div>
```

#Episode ID:
```
<a href="/player/tv/aeschbacher/video/voller-einsatz?id=f3608137-891f-4b1b-b615-46155730fbbe">
```
id=de8d87bd-91cb-4260-9c54-19e959f53a8a

##JSON with streams:
```
http://www.srf.ch//webservice/cvis/segment/de8d87bd-91cb-4260-9c54-19e959f53a8a/.json?nohttperr=1;omit_video_segments_validity=1;omit_related_segments=1
```

##Playlists:
In the JSON you can find the section playlists, which list high (latest episodes) and low definition streams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"playlists":{"playlist":[{"streaming":"hls","quality":"100","url":"http:\/\/srfvodhd-vh.akamaihd.net\/i\/vod\/aeschbacher\/2015\/01\/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,.mp4.csmil\/master.m3u8"},{"streaming":"hds","quality":"100","url":"http:\/\/srfvodhd-vh.akamaihd.net\/z\/vod\/aeschbacher\/2015\/01\/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,.mp4.csmil\/manifest.f4m"},{"streaming":"hls","quality":"200","url":"http:\/\/srfvodhd-vh.akamaihd.net\/i\/vod\/aeschbacher\/2015\/01\/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,q50,q60,.mp4.csmil\/master.m3u8"},{"streaming":"hds","quality":"200","url":"http:\/\/srfvodhd-vh.akamaihd.net\/z\/vod\/aeschbacher\/2015\/01\/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,q50,q60,.mp4.csmil\/manifest.f4m"}]}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


##hls: quality 100 m3u8 (low definition)
```
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,.mp4.csmil/master.m3u8
```

Content of the .m3u8 file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=133000,RESOLUTION=320x180,CODECS="avc1.66.30, mp4a.40.2"
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,.mp4.csmil/index_0_av.m3u8?null=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=333000,RESOLUTION=480x272,CODECS="avc1.66.30, mp4a.40.2"
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,.mp4.csmil/index_1_av.m3u8?null=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=659000,RESOLUTION=512x288,CODECS="avc1.77.30, mp4a.40.2"
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,.mp4.csmil/index_2_av.m3u8?null=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1323000,RESOLUTION=640x360,CODECS="avc1.77.30, mp4a.40.2"
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,.mp4.csmil/index_3_av.m3u8?null=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=30000,CODECS="mp4a.40.2"
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,.mp4.csmil/index_0_a.m3u8?null=

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


##hds: quality 200 m3u8 (high definition)
```
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,q50,q60,.mp4.csmil/master.m3u8
```

Content of the .m3u8 file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=133000,RESOLUTION=320x180,CODECS="avc1.66.30, mp4a.40.2"
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,q50,q60,.mp4.csmil/index_0_av.m3u8?null=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=333000,RESOLUTION=480x272,CODECS="avc1.66.30, mp4a.40.2"
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,q50,q60,.mp4.csmil/index_1_av.m3u8?null=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=659000,RESOLUTION=512x288,CODECS="avc1.77.30, mp4a.40.2"
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,q50,q60,.mp4.csmil/index_2_av.m3u8?null=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1323000,RESOLUTION=640x360,CODECS="avc1.77.30, mp4a.40.2"
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,q50,q60,.mp4.csmil/index_3_av.m3u8?null=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2123000,RESOLUTION=960x544,CODECS="avc1.77.30, mp4a.40.2"
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,q50,q60,.mp4.csmil/index_4_av.m3u8?null=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=3619000,RESOLUTION=1280x720,CODECS="avc1.77.30, mp4a.40.2"
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,q50,q60,.mp4.csmil/index_5_av.m3u8?null=
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=30000,CODECS="mp4a.40.2"
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,q50,q60,.mp4.csmil/index_0_a.m3u8?null=

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


working HD stream at 1280x720: 
```
http://srfvodhd-vh.akamaihd.net/i/vod/aeschbacher/2015/01/aeschbacher_20150108_222443_v_webcast_h264_,q10,q20,q30,q40,q50,q60,.mp4.csmil/index_5_av.m3u8?null=
```

##Period:
Describes the point in time. Only one month at the time displayed
December 2014
&period=2014-12







Alternativen:
http://www.srf.ch/player/tv/aeschbacher/video/voller-einsatz?id=f3608137-891f-4b1b-b615-46155730fbbe
http://podcastsource.sf.tv/nps/podcast/aeschbacher/2014/12/aeschbacher_20141211_222427_v_podcast_h264_q30.mp4







