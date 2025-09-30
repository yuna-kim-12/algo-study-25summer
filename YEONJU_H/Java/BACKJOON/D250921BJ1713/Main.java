package D250921BJ1713;
import java.util.*;
import java.io.*;

class Candidate {
    int no; // 학생 번호
    int cnt; // 추천 횟수
    int myTimeIdx;
    static int timeIdx = 0; // 게시된 시점

    Candidate(int no, int cnt) {
        this.no = no;
        this.cnt = cnt;
        this.myTimeIdx = timeIdx++;
    }
}


public class Main {
    static int N, T;
    static ArrayList<Candidate> photoFrames = new ArrayList<>();
    public static void main(String[] args) throws IOException{
        /*
            후보 추천하기

            추천받은 학생 사진을 틀에 게시하고 추천받은 횟수를 표시하는 규칙
            1. 추천 시작 전, 모든 사진틀 비어있음
            2. 특정 학생 추천 시, 추천받은 학생의 사진이 반드시 사진틀에 게시
            3. 비어있는 사진틀이 없는 경우, 현재까지 추천받은 횟수가 가장 적은 학생 사진 삭제 후 게시 ( 추천 수가 같으면 게시된지 오래된 것부터 삭제)
            4. 현재 게시된 사진이 추천받은 경우 횟수만 증가
            5. 사진 삭제 시, 해당 학생의 추천 횟수 0으로 리셋

            [ 출력 ]
            사진틀의 개수, 전체 학생의 추천결과가 추천받은 순서대로 주어졌을 때 최종 후보가 누구 인지 결정하는 프로그램 작성

            [ 입력 ]
            첫 줄 : 사진의 개수 1 <= N <= 20
            둘째 줄 : 전체 학생의 총 추천 횟수 (<= 1000)
            셋째 줄 : 추천받은 학생을 나타내는 번호  (1~100 자연수 )

            [ 아이디어 ]
            1. 사진틀 배열 생성
            2. Total 총 추천 횟수 크기 + 1의 배열 생성 후 추천 데이터 담기
            3. Total 크기 + 1만큼 배열 하나
             더 생성해서 추천 데이터 순서대로 돌리며 데이터 기록하기
            4. 기록할 때마다 아래 사항을 체크한다.
            1) 방금 추천한 학생이 게시되어 있는가?
            - X :
                사진 틀이 꽉 차 있는가?
                - O : - 추천 수가 가장 적은 학생 삭제 후 게시
                      - 추천 수 같은 학생이 여러명이면 게시된지 오래된 것부터 삭제
                      - 오래된 걸 어떻게 알지?
                       : ArrayList로 add해가면서 sort 후, 가장 작은 값들 중 앞에 있는 값을 삭제
                      - 삭제된 학생 추천 횟수 0 리셋
                - X : 빈틀(0)에 해당 인덱스 기록
            - O : 추천 횟수만 증가
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        T = Integer.parseInt(br.readLine());

        int[] recommandArr = new int[T + 1]; // 추천 정보
        int[] countArr = new int[101];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int t = 1; t <= T ; t++) {
            recommandArr[t] = Integer.parseInt(st.nextToken());
        } // 입력 완료

        int curNum;
        for(int t = 1; t <= T; t++) {
            curNum = recommandArr[t];

            // 존재 시, 추천만 증가
            if(isExist(curNum)){
                Candidate found = findStudent(curNum);
                found.cnt++;
                countArr[curNum]++;
                continue;
            };

            //
            if(photoFrames.size() < N) { // 비었음 그냥 추가
                photoFrames.add(new Candidate(curNum,1));
            } else { // 삭제 후, 삭제한 것 점수 리셋, 추가
                photoFrames.sort((a, b) -> {
                    if (a.cnt != b.cnt) {
                        return Integer.compare(a.cnt, b.cnt);  // 추천 횟수 적은 순
                    }
                    return Integer.compare(a.myTimeIdx, b.myTimeIdx);  // 시간 빠른 순(오래된 순)
                });


                // 제거 후 점수 초기화
                Candidate removed = photoFrames.remove(0);
                countArr[removed.no] = 0;

                // 추가
                photoFrames.add(new Candidate(curNum,1));
            }
        }
        // 최종 내림차순 정렬
        photoFrames.sort((a,b) -> {
            return Integer.compare(a.no, b.no);
        });
        for(Candidate c : photoFrames) {
            System.out.print(c.no + " ");
        }

    }

    public static boolean isExist(int curNum){
        for(Candidate c : photoFrames) {
            if(c.no == curNum) {
                return true;
            }
        }
        return false;
    }

    public static Candidate findStudent(int curNum) {
        for(Candidate c : photoFrames) {
            if(c.no == curNum) {
                return c;
            }
        }

        return null;
    }
}

