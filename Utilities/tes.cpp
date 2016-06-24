#include <fstream>
#include <string>
#include <alloca.h>
#include <string>
#include <iostream>
#include <iostream>
#include <cstring>
#include <memory>
int main() 
{ 
	char files[20][20];
	char* S; 
	int i=0;
    std::ifstream file("selected");
    std::string str; 
    while (std::getline(file, str))
    {
    	std::strcpy(files[i],str.c_str());
     	i++;
    }

    
}