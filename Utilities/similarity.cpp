#include <musly/musly.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstdlib>

void similarityCheck(int num,char** files,char*  filetochk)
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
	int chk,i=0; 
	
	musly_debug(4);		
	mj = musly_jukebox_poweron(NULL,NULL);
	track=musly_track_alloc(mj);
	for(i=0;i<num;i++)
		{
		trac[i]=musly_track_alloc(mj);
		musly_track_analyze_audiofile(mj,*((files)+i),0,trac[i]);
	}
	trac[i+1]=musly_track_alloc(mj);
	musly_track_analyze_audiofile(mj,filetochk,0,trac[i+1]);
	//tracks=&trac;
	musly_jukebox_addtracks(mj,trac,trackids,num);
	musly_jukebox_setmusicstyle(mj,trac,num);
	chk = musly_jukebox_similarity(mj,trac[i+1],i+1,trac,trackids,num,similarities);
	for(i=0;i<num;i++)
		printf("%f\n",similarities[i]);

	
	//musly_jukekox_poweroff(mj);
	printf("\nchk=%d\n",chk);
	musly_track_alloc(mj);
	}

int main()
{ char *arr[20];
	arr[0]="a.wav";
	arr[1]="1.wav";
	arr[2]="b.wav";
	arr[3]="a.wav";
	similarityCheck(3,arr,"2.wav");
 return 0;
}