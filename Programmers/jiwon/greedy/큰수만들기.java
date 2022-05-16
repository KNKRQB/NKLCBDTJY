package jiwon.greedy;

import java.util.HashSet;
import java.util.Set;

public class 큰수만들기 {
    public static void main(String[] args) {
        System.out.println(solution("123456", 3));
    }

    public static String solution(String number, int k) {
        StringBuilder answer = new StringBuilder();
        int index=0;
        int max = 0;

        for(int i=0;i<number.length()-k;i++) {
            for(int j=index;j<=k+i;j++) {
                if(max < number.charAt(j) - '0') {
                    max = number.charAt(j)-'0';
                    index = j+1;
                }
            }
            answer.append(max);
            max=0;
        }
        return answer.toString();
    }
}
