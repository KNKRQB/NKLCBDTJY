package jiwon;

import java.util.*;

public class line_summer_intern_2 {
    public static void main(String[] args) {
        int n = 5;
        int[] times = {2, 4, 5};
        System.out.println(solution(n, times));
    }
    public static int solution(int n, int[] times) {
        if(n==2) {
            return times[0];
        }
        if(n==3) {
            return times[0]*2;
        }

        int answer = times[0]; // 1번은 잘라야되니까
        int[] dp = new int[n+1]; //인덱스가 줄 갯수, 줄 자르는데 걸리는 시간
        dp[0] = 0;
        dp[1] = 0;
        dp[2] = times[0];
        dp[3] = dp[2] + times[0];

        for(int i=3;i<=n;i++) { //i는 줄갯수
            dp[i] = dp[i-1] + times[0];
            for(int j=2;j<=i/2;j++) {
                dp[i] = Math.min(dp[i-j] + times[j-1], dp[i]);
            }
            System.out.println("dp["+i+"] = " + dp[i]);
        }

        return dp[n];
    }
}

