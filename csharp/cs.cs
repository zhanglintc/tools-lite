using System;
using System.Threading;

class ThreadTest
{
    static void Main()
    {
        // create 100 thread
        for(int i = 0; i < 10; i++){
            Thread t = new Thread(ThreadFunction);
            t.Start();
        }

        Console.Write("Main thread\n");
        for(;;);
    }

    static void ThreadFunction()
    {
        Console.Write("child thread\n");
        // for(;;);
    }

}



