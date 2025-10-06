package D250915BJ5212;
import java.util.*;
import java.io.*;

public class Main {
/*
    지구 온난화로 인한 수면 상승

    R,C 지도 크기
    X 땅
    . 바다

    50년 후에는 인접 3칸 또는 네칸에 바다가 있는 땅은 모두 잠김
    50년 뒤의 모든 섬을 포함하는 가장 작은 직사각형

    - 50년 뒤어도 적어도 섬은 한 개 있음
    - 지도에 없는,벗어난 칸은 모두 바다

    [ 아이디어 ]
    - 각 칸을 순회하면서, 인접한 바다가 3칸 또는 4칸인 칸일 경우 방문처리
    - 모두 처리한 후에, 가장 왼쪽 끝/오른쪽 끝/위쪽 끝/아래쪽 끝 방향의 좌표를 구해서,
      그 직사각형 안의 좌표만 출력한다.
 */
    static int R,C,SR,SC,FR,FC;;
    static char[][] map, newMap;
    static int[] dr = {0,0,1,-1};
    static int[] dc = {1,-1,0,0};
   public static void main(String[] args) throws IOException{
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       StringTokenizer st = new StringTokenizer(br.readLine());
       R = Integer.parseInt(st.nextToken());
       C = Integer.parseInt(st.nextToken());
       SR = 987654321;
       SC = 987654321;
       FR = 0;
       FC = 0;
       map = new char[R][C];
       newMap = new char[R][C];
       for(int r = 0; r < R; r++) {
           String str = br.readLine();
           for(int c = 0; c < C; c++) {
               map[r][c] = str.charAt(c);
               newMap[r][c] = str.charAt(c);
           }
       }

       for(int r = 0; r < R; r++) {
           for(int c = 0; c < C; c++) {
                if(map[r][c] == 'X') {
                    int cnt = 0;

                    for(int k = 0; k < 4; k++) {
                        int nr = r + dr[k];
                        int nc = c + dc[k];

                        if(nr >= 0 && nc >= 0 && nr < R && nc < C) {
                            if(map[nr][nc] == '.') {
                                cnt++;
                            }
                        } else {
                            cnt++;
                        }
                    }
                    if(cnt >= 3) {
                        newMap[r][c] = '.';
                    }

                }
           }
       }
        findPoints();
       // 가장 왼쪽상단의 첫번째 X / 가장 오른쪽 하단의 첫번째 X 좌표 찾기
       for(int r = SR; r <= FR; r++) {
           for(int c = SC; c <= FC; c++) {
               System.out.print(newMap[r][c]);
           }
           System.out.println();
       }
   }
   static void findPoints() {
       for(int r = 0; r < R; r++) {
           for (int c = 0; c < C; c++) {
               if (newMap[r][c] == 'X') {
                   SR = Math.min(SR, r);
                   FR = Math.max(FR, r);
                   SC = Math.min(SC, c);
                   FC = Math.max(FC, c);
               }
           }
       }
   }
}
