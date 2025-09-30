package D250909BJ20436;

import java.util.*;
import java.io.*;

public class Main {
    static final char[][] keyboard = {
            {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
            {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
            {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
    };
    static int[] curLRC;
    static int[] curRRC;
    static int N, minTime;
    public static void main(String[] args) throws IOException{

        /* 문제 정리
         * 특정 문자열을 입력했을 때, 이 문자열을 출력하는 데 걸리는 시간의 최솟값 구하기
         *
         * [ 아이디어 ]
         * - keyboard 3차원 배열을 만든다.
         * - 왼쪽과 오른쪽 위치를 저장한다.
         * - 저장한 위치를 중심으로 각 문자열까지의 거리를 재서 결과시간에 더한다.
         *   - 키보드를 순회하며 일치하는 문자열을 찾는다.
         * - 해당 문자를 최솟값으로 출력한다.
         * - 부르스포스로 L 선택 경우, R 선택 경우를 따지며 간다
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        char L = st.nextToken().charAt(0);
        char R = st.nextToken().charAt(0);
        String str = br.readLine();
        N = str.length();
        minTime = 0;

        for(int r = 0 ; r < 3; r++) {
            for(int c = 0; c < keyboard[r].length; c++) {
                if (keyboard[r][c] == L) {
                    curLRC = new int[]{r, c};
                }
                if (keyboard[r][c] == R) {
                    curRRC = new int[]{r, c};
                }
            }
        }
        for(int i = 0 ; i < N; i ++) {
            char curC = str.charAt(i);
            for(int r = 0 ; r < 3; r++) {
                for(int c = 0; c < keyboard[r].length; c++) {
                    if(curC == keyboard[r][c]){
                        if(isConsonant(curC)) { // 자음
                            minTime += 1 + Math.abs(curLRC[0] - r) + Math.abs(curLRC[1] - c);
                            curLRC[0] = r;
                            curLRC[1] = c;
                        } else if(isVowel(curC)) { // 모음
                            minTime += 1 + Math.abs(curRRC[0] - r) + Math.abs(curRRC[1] - c);
                            curRRC[0] = r;
                            curRRC[1] = c;
                        }
                    }
                }
            }
        }

        System.out.println(minTime);

    }

    public static boolean isVowel(char c) { // 모음
        String vowel = "yuiophjklbnm";
        return vowel.indexOf(c) != -1;
    }

    public static boolean isConsonant(char c) { // 자음
        String consonant = "qwertasdfgzxcv";
        return consonant.indexOf(c) != -1;
    }

}
