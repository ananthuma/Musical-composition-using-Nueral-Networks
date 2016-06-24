	#include <musly/musly.h>
	#include<stdio.h>
	#include <iostream>
	#include <fstream>
	#include <cstdlib>
		main()
		{
		musly_jukebox* mj ;
		musly_track* track;
		musly_track* trac[10];
		musly_track* track2;
		//musly_track** tracks;
		//musly_trackid* trackids;
		int trackids[10];
		float similarities[1000];
		//const char *j;
		int chk,i; 
		
		musly_debug(4);		
		mj = musly_jukebox_poweron(NULL,NULL);
		track=musly_track_alloc(mj);
		for(i=0;i<5;i++)
			trac[i]=musly_track_alloc(mj);
		musly_track_analyze_audiofile(mj,"1.wav",0,trac[0]);
		
		musly_track_analyze_audiofile(mj,"2.wav",0,trac[1]);
		musly_track_analyze_audiofile(mj,"a.wav",0,trac[4]);
		musly_track_analyze_audiofile(mj,"b.wav",0,trac[2]);
		musly_track_analyze_audiofile(mj,"1.wav",0,trac[3]);
		//tracks=&trac;
		musly_jukebox_addtracks(mj,trac,trackids,3);
		musly_jukebox_setmusicstyle(mj,trac,3);
		chk = musly_jukebox_similarity(mj,trac[3],3,trac,trackids,5,similarities);
		for(i=0;i<5;i++)
			printf("\n%f",similarities[i]);

		//musly_jukekox_poweroff(mj);
		printf("\nchk=%d\n",chk);
		musly_track_alloc(mj);
		}
