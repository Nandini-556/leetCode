class Solution {
    public boolean judgeSquareSum(int c) {
        for (int p = 2; (long) p * p <= c; p++) {
            if (c % p == 0) {
                int count = 0;
                while (c % p == 0) {
                    count++;
                    c /= p;
                }
                if (p % 4 == 3 && count % 2 != 0) {
                    return false;
                }
            }
        }
        // any remaining prime factor > sqrt(c) appears only once
        return c % 4 != 3;
    }
}