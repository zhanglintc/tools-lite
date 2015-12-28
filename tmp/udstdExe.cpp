#include "iostream"

using namespace std;

int bss;

int main(int argc, char const *argv[])
{
    int stack = 0;
    int *heap  = (int *)malloc(sizeof(int));
    static int data = 0;

    cout << endl;

    cout << "bss: ";
    cout << &bss << endl;

    cout << "stack: ";
    cout << &stack << endl;

    cout << "heap: ";
    cout << &heap << endl;

    cout << "data: ";
    cout << &data << endl;

    cout << endl;
    return 0;
}