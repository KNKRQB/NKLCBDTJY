package jiwon;

import java.util.*;

public class boj1260 {
    static List<List<Integer>> arr = new ArrayList<>();
    static boolean[] visited;
    static int n;
    static int m;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();
        int v = scanner.nextInt();

        visited = new boolean[n+1]; //배열들 초기화
        for(int i=0;i<=n;i++) {
            arr.add(new ArrayList<>());
        }

        for(int i=1;i<=m;i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();

            arr.get(a).add(b);
            arr.get(b).add(a);
        }

        for(int i=1;i<=n;i++) {
            Collections.sort(arr.get(i));
        }

        dfs(v);
        System.out.println();
        visited = new boolean[n+1];
        bfs(v);

    }

    public static void dfs(int x) { //dfs: stack 사용
        visited[x] = true;
        System.out.print(x + " ");
        for(int num : arr.get(x)) {
            if(!visited[num]) {
                dfs(num);
            }
        }
    }

    public static void bfs(int x) { //bfs: queue 사용
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(x);
        visited[x] = true;

        while(!queue.isEmpty()) {
            int value = queue.poll();
            System.out.print(value + " ");

            for(int num : arr.get(value)) {
                if(!visited[num]) {
                    visited[num] = true;
                    queue.offer(num);
                }
            }
        }
    }
}
