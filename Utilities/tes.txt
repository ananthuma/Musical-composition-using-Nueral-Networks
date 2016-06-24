#include <fstream>
#include <string>

int main() 
{ 
    std::ifstream file("Read.txt");
    std::string str; 
    while (std::getline(file, str))
    {
        // Process str
    }
}