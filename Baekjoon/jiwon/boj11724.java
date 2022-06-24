package jiwon;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class boj11724 {
    static boolean[] visited;
    static List<List<Integer>> arr = new ArrayList<>();
    static Integer answer;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        answer = 0;

        visited = new boolean[n+1];

        for(int i=0;i<=n;i++) {
            arr.add(new ArrayList<>());
        }

        for(int i=0;i<m;i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();

            arr.get(a).add(b);
            arr.get(b).add(a);
        }
        for(int i=1;i<=n;i++) {
            if(!visited[i]) {
                dfs(i);
                answer++;
            }
        }
        System.out.println(answer);
    }

    static public void dfs(int x) {
        visited[x] = true;
        for(int num : arr.get(x)) {
            if(!visited[num]) {
                dfs(num);
            }
        }
    }
}
