class RunnableDemo implements Runnable {
    private Thread t;
    private String threadName;

    RunnableDemo( String name) {
        threadName = name;
        // System.out.println("Creating " +  threadName );
    }

   public void run() {
    try {
        Thread.sleep(13000);
    }catch (InterruptedException e) {
        System.out.println("Thread " +  threadName + " interrupted.");
    }
        // for(;;);
    }

    public void start () {
        t = new Thread (this, threadName);
        t.start ();
    }
}

public class HelloWorld {
    public static void main(String args[]) {
        System.out.println("before 3s");
        try {
            Thread.sleep(3000);
        }catch (InterruptedException e) {
            System.out.println("Sleep failed");
        }
        System.out.println("after 3s");

        for (int i = 0; i < 100; ++i) {
            new RunnableDemo("").start();
        }

        System.out.println("after thread start");

        while (true);
    }
}
