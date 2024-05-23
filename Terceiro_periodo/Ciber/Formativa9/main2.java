public class Main {
    public static void main(String[] args) {
        Thread thread1 = new MinhaThread();
        Thread thread2 = new MinhaThread();
        
        thread1.setName("Thread-1");
        thread2.setName("Thread-2");
        
        thread1.start();
        thread2.start();
    }
    
    private static class MinhaThread extends Thread {
        @Override
        public void run() {
            System.out.println("Olá da thread " + Thread.currentThread().getName());
        }
    }
}