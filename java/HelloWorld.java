class RunnableDemo implements Runnable {
   private Thread t;
   private String threadName;

   RunnableDemo( String name) {
      threadName = name;
      System.out.println("Creating " +  threadName );
   }

   public void run() {
      // System.out.println("Running " +  threadName );
      try {
      //    for(int i = 4; i > 0; i--) {
      //       System.out.println("Thread: " + threadName + ", " + i);
      //       // 让线程睡眠一会
            Thread.sleep(15000);
         // }
      }catch (InterruptedException e) {
         System.out.println("Thread " +  threadName + " interrupted.");
      }
      // System.out.println("Thread " +  threadName + " exiting.");
      // for(;;);
   }

   public void start () {
      // System.out.println("Starting " +  threadName );
      // if (t == null) {
         t = new Thread (this, threadName);
         t.start ();
      // }
   }
}

public class HelloWorld {

    public static void main(String args[]) {
        for (int i = 0; i < 100; ++i) {
            new RunnableDemo( "Thread-1").start();
        }
        while (true);
    }
}
