package hello;

public class Person {
	String name;
	int age;
	String nationality;
	boolean isMale;
	
	public Person(String name, int age, String nationality, boolean isMale) {
		this.name = name;
		this.age = age;
		this.nationality = nationality;
		this.isMale = isMale;
		
		String gender;
		if(this.isMale == true) {
			gender = "male";
		}else {
			gender = "female";
		}
		
		System.out.println(this.name + " is a " + this.age + " year old " + gender + " from " + this.nationality + ".");
	}
	
	public static void main(String[] args) {
		Person person1 = new Person("Bob", 19, "Romania", true);
		Person person2 = new Person("Jasmine", 24, "Brazil", false);
	}

}
