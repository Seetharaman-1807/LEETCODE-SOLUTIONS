import java.util.*;

class Solution {
    public int[] decimalRepresentation(int n) {
        List<Integer> parts = new ArrayList<>();
        int place = 1;
        while (n > 0) {
            int digit = n % 10;
            if (digit != 0) {
                parts.add(digit * place);
            }
            n /= 10;
            place *= 10;
        }

        Collections.reverse(parts);

        int[] ans = new int[parts.size()];
        for (int i = 0; i < parts.size(); i++) {
            ans[i] = parts.get(i);
        }

        return ans;
    }
}