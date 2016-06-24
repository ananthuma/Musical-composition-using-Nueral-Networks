#include <musly/musly.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <fstream>
#include <fstream>
#include <string>
#include <alloca.h>
#include <string>
#include <iostream>
#include <iostream>
#include <cstring>
#include <memory>
char files[20][20];
char filetochk[20];
int num;
void read()
{

	char* S; 
	int i=0;
    std::ifstream file("selected");
    std::string str; 

    while (std::getline(file, str))
    {
    	std::strcpy(files[i],str.c_str());
     	i++;
    }
    num=i-1;
    std::strcpy(filetochk,str.c_str());
}
void similarityCheck()
	{
	read();
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
	std::ofstream file2("result");
	for(i=0;i<num;i++)
		file2<<similarities[i]<<"\n";

	//return similarities;
	//musly_jukekox_poweroff(mj);
	printf("\nchk=%d\n",chk);
	musly_track_alloc(mj);
	}

#include <boost/python.hpp>
 
BOOST_PYTHON_MODULE(simchk)
{
    using namespace boost::python;
    def("similarity", similarityCheck);
}
/*Compile
g++ -c -fPIC simchk.cpp -o simchk.o -I /usr/include/python2.7/ -lmusly
g++ -shared -Wl,-soname,simchk.so -o simchk.so  simchk.o -lpython2.7 -lboost_python -lmusly
*/