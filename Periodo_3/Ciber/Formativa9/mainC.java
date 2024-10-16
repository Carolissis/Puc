class Main {
    public static void main(String[] args) {
        int start = 2;
        int end = 10000000;
        int mid = (start + end) / 2;
        
        Thread thread1 = new Thread(new Runnable() {
            @Override
            public void run() {
                procuraNumPrimo(start, mid);
            }
        });
        
        Thread thread2 = new Thread(new Runnable() {
            @Override
            public void run() {
                procuraNumPrimo(mid + 1, end);
            }
        });
        
        thread1.start();
        thread2.start();
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