import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int input;
    int cnt = 0;

    for (int i = 0; i < n; i++) {
      input = sc.nextInt();

      for (int j = 2; j <= input; j++) {
        if (j == input)
          cnt++;
        if (input % j == 0) {
          break;
        }
      }
    }

    // for (int i = 0; i < n; i++) {
    // int sqrtNum = (int) Math.sqrt(arr[i]);
    // for (int j = 2; j <= sqrtNum; j++) {
    // if (arr[i] % j == 0) {
    // break;
    // }
    // cnt++;
    // }
    // }

    System.out.println(cnt);
    sc.close();
  }
}
