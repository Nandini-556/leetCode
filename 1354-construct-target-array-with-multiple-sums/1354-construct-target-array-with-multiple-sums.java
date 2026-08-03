import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    public boolean isPossible(int[] target) {

        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        long sum = 0;

        for (int num : target) {
            pq.offer(num);
            sum += num;
        }

        while (true) {

            int max = pq.poll();
            long rest = sum - max;

            // All elements are 1
            if (max == 1 || rest == 1)
                return true;

            // Invalid cases
            if (rest == 0 || max < rest || max % rest == 0)
                return false;

            int previous = (int)(max % rest);

            pq.offer(previous);

            sum = rest + previous;
        }
    }
}