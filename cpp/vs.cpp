#include<iostream>
#include<string>
#include<dirent.h>
using namespace std;
int main()
{
    string dirname;
    DIR *dp;
    struct dirent *dirp;
    cout << "Please input a directory: ";
    cin >> dirname;
    if((dp = opendir(dirname.c_str())) == NULL)
    {
        cout << "Can't open " << dirname << endl;
    }
    while((dirp = readdir(dp)) != NULL)
    {
        cout << dirp->d_name << endl;
    }
    closedir(dp);
    return 0;
}
