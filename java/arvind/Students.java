package hello;

import java.util.ArrayList;

public class Students {

	public static void main(String[] args) {
		ArrayList<String> studentNames = new ArrayList<String>();
		ArrayList<Integer> studentMarks = new ArrayList<Integer>();
		studentNames.add("Macc Zucc");
		studentNames.add("Po");
		studentNames.add("Big Man Jeff");
		studentNames.add("Mr. Mac");
		studentMarks.add(90);
		studentMarks.add(100);
		studentMarks.add(35);
		studentMarks.add(200);
		
		System.out.println("There are " + studentNames.size() + " students in the class.");
		System.out.println("The students are: " + studentNames + " .");
		System.out.println("They each scored " + studentMarks + " marks respectively.");
	}

}
