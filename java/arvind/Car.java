package hello;

import java.util.Calendar;

public class Car {

	String make;
	String model;
	int year;
	boolean isNew;
	String owner;
	
	public boolean isOld() {
		int currentYear = Calendar.getInstance().get(Calendar.YEAR);
		if(currentYear - year > 10) {
			System.out.println("It is an old car.");
			return true;
		}else {
			System.out.println("It is a new car.");
			return false;
		}
	}
	
	public void Sell(String newOwner) {
		owner = newOwner;
		if(isNew) {
			isNew = false;
		}
		System.out.println("The car was sold. It is now owned by " + owner + ".");
	}
	
	public static void main(String[] args) {
		Car someCar = new Car();
		someCar.make = "Toyota";
		someCar.model = "Camry";
		someCar.year = 2007;
		someCar.isNew = true;
		someCar.owner = "Old Guy";
		
		System.out.println("The vehicle in question is a " + someCar.make + " " + someCar.model);
		
		someCar.isOld();
		
		System.out.println("The car is owned by " + someCar.owner + ".");
		
		someCar.Sell("New Guy");
	}

}
