#include<stdio.h>
#include<musly/musly.h>
int main()
{	int i;
	musly_jukebox* jb;
	musly_track* track;
	musly_track* tracks[20];
	int trackId[20];
	float similarity[20];
	printf("1\n");
	track=
	jb =musly_jukebox_poweron(NULL,NULL);
	printf("12\n");
	musly_track_analyze_audiofile(jb,"1.wav",0,track);
	tracks[0]=track;
	printf("12\n");
	musly_track_analyze_audiofile(jb,"2.wav",0,track);
	printf("12\n");
	tracks[1]=track;
	musly_track_analyze_audiofile(jb,"a.wav",0,track);
	printf("12\n");
	tracks[2]=track;
	musly_track_analyze_audiofile(jb,"b.wav",0,track);
	printf("123\n");
	tracks[3]=track;
	musly_jukebox_setmusicstyle(jb,tracks,4);
	printf("1234\n");
	musly_jukebox_addtracks (jb,tracks,trackId,4);
	printf("12345\n");
	musly_jukebox_similarity(jb,tracks[1],1,tracks,trackId,4,similarity);
	for(i=0;i<4;i++)
		printf("%d",similarity[i]);
	return 0;


}