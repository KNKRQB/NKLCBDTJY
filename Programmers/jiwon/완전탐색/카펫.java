package jiwon.완전탐색;

public class 카펫 {
    public static void main(String[] args) {

        int brown = 12;
        int yellow = 3;

        int[] answer = new int[2];

        for(int r=1;r<=yellow;r++) { // 노란 타일의 가로 개수 결정하기
            if(yellow % r == 0) {
                int col = yellow / r;
                int b = (r + col) * 2 + 4;
                if(brown == b) {
                    answer[0] = r+2;
                    answer[1] = col+2;
                }
            }
        }
    }
}
