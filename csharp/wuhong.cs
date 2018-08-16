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
        while(mController)
        {
            // do something here
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

            Thread.Sleep(5);

            for(int i = 0; i < list.Count; ++i)
            {
                list[i].Release();
            }
            list.Clear();
        }
    }
}

