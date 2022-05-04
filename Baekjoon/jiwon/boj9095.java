package jiwon;

import java.util.Scanner;

public class boj9095 {
    static int dp[] = new int[11];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt(); //테스트 케이스

        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        for(int i=4;i<11;i++) {
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
        }

        for(int i=0;i<t;i++) {
            int n = scanner.nextInt();
            System.out.println(dp[n]);
        }
    }
}
