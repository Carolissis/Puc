class Main {
    public static void main(String[] args) {
        int start = 2;
        int end = 10000000;
        int numberOfThreads = 4;
        int interval = (end - start + 1) / numberOfThreads;
        
        Thread[] threads = new Thread[numberOfThreads];
        
        for (int i = 0; i < numberOfThreads; i++) {
            int threadStart = start + i * interval;
            int threadEnd = (i == numberOfThreads - 1) ? end : threadStart + interval - 1;
            
            threads[i] = new Thread(new Runnable() {
                @Override
                public void run() {
                    procuraNumPrimo(threadStart, threadEnd);
                }
            });
            
            threads[i].start();
        }
    }

    public static void procuraNumPrimo(int start, int end) {
        for (int i = start; i <= end; i++) {
            if (ePrimo(i)) {
                System.out.println(i + " é primo");
            }
        }
    }

    public static boolean ePrimo(int num) {
        if (num <= 1) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}
