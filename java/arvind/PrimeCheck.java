package hello;

import java.util.*;
public class PrimeCheck {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter a number: ");
		int inputNum = scanner.nextInt();
		
		int potentialFactor = 2;
		while(inputNum % potentialFactor != 0) {
			potentialFactor++;
		}
		if(potentialFactor == inputNum) {
			System.out.println("It is a prime number");
		}else {
			System.out.println("It is not a prime number because it is divisible by " + potentialFactor);
		}
	}

}
