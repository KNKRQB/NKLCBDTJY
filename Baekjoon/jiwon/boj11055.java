package jiwon;

import java.util.Scanner;


public class boj11055 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        int[] dp = new int[n];

        for(int i=0;i<n;i++) {
            arr[i] = scanner.nextInt();
        }

        int max = 0;
        for(int i=0;i<n;i++) {
            dp[i] = arr[i];
            for(int j=0;j<i;j++) {
                if(arr[i]>arr[j] && dp[i] < dp[j] + arr[i]) {
                    dp[i] = dp[j] + arr[i];
                }
            }
            max = Math.max(max, dp[i]);
        }
        System.out.println(max);
    }
}
