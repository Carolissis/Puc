class Main {
    public static void main(String[] args) {
        int start = 2;
        int end = 10000000;
        procuraNumPrimo(start, end);
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