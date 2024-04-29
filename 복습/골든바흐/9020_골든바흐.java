package midterm;

import java.util.Scanner;

public class Goldbach {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// System.out.print("골드바흐(두개의 소수)");
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		boolean[] prime_flag = new boolean[1000];
		for (int i = 2; i < prime_flag.length; i++) {
			prime_flag[i] = true;
		}

		int sqrtN = (int) Math.sqrt(prime_flag.length);
		for (int i = 2; i <= sqrtN; i++) {
			if (prime_flag[i]) {
				for (int j = i * i; j < prime_flag.length; j += i) {
					prime_flag[j] = false;
				}
			}
		}

		int num = sc.nextInt();
		int p = num / 2, q = num / 2;
		while (true) {
			if (prime_flag[p] == true && prime_flag[q] == true) {
				System.out.println(p + "+" + q);
				break;
			}
			p--;
			q++;
		}

		sc.close();

	}

}
