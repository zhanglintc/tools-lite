using System;
using System.Threading;
using System.Collections.Generic;

public class MyThreadObject
{
    private bool mController;
    private Thread mThread;

    public MyThreadObject()
    {
        mController = false;
        mThread = new Thread(ThreadExecutor);
        mThread.Start();
    }

    private void ThreadExecutor()
    {
        // *************************
        // Attention:  mController => !mController
        // You only want to quit when "Release()" being called
        // Thus only "!mController" makes this thread running
        // *************************
        while(!mController)
        {
            Thread.Sleep(1);
        }
    }

    public void Release()
    {
        mController = true;
        if(mThread != null)
        {
            //mThread.Abort();
            mThread = null;
        }
    }
}

public class Entry {
    public static void Main()
    {
        while(true)
        {
            List<MyThreadObject> list = new List<MyThreadObject>();
            for(int i = 0; i < 100; ++i)
            {
                MyThreadObject t = new MyThreadObject();
                list.Add(t);
            }

            // Attention:  it seems like that sleep not worked here
            Thread.Sleep(3 * 1000);

            // Attention:  if I comment out these "Release()" calls
            // 103 threads will be alive
            // Otherwise only 3 threads remains
            for(int i = 0; i < list.Count; ++i)
            {
                list[i].Release();
            }
            list.Clear();

            // *************************
            // Attention:  add an endless loop here
            // Otherwise new threads will be newed in next turn
            // *************************
            while(true){}
        }
    }
}

