public class Main {
    public static void main(String[] args) throws InterruptedException {
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("Estamos na thread " + Thread.currentThread().getName());
            }
        });
        
        thread.setName("Thread da Carol");
        thread.setPriority(Thread.MAX_PRIORITY);
        
        System.out.println("Estamos na thread " + Thread.currentThread().getName() + " antes de iniciar uma nova thread");
        thread.start(); 
        
        Thread.sleep(1000); 
        
        System.out.println("Estamos na thread " + Thread.currentThread().getName() + " depois de iniciar uma nova thread");
    }
}