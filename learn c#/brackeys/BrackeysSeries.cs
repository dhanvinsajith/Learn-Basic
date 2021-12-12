/*using System;
using System.Collections.Generic;
namespace learn_c_
{
    //DAY 5
    class Eating{
        public string eaterName;
        public string food1;
        public int stamina;
        public float eatingExperience;

        //CONSTRUCTOR sets default values for the class to make assignment easier
        //green highlights if you want to set name and food in vs
        public Eating(/*string _name, string _food1*//*){
            //_name = eaterName;
            //_food1 = food1;
            stamina = 4;
            eatingExperience = 0f;
        }

        public void StartEating(){
            if(stamina>1){
                Console.WriteLine("\n" + eaterName + " has eaten " + food1);
                stamina--;
                eatingExperience+= 120f;
            }else{
                Console.WriteLine("\n" + eaterName + " is out of stamina; Rest to eat more.");
            }
        }

        public void Rest(){
            if(stamina<1){
                Console.WriteLine("\n" + eaterName + " took a fat sleep and reagained stamina.");
                stamina = 4;
            }
        }

    }




    class Program
    {

        //static keeps track of all instances of that variable
        static void Main(string[] args)
        {
            //WINDOW FORMATTING
            Console.Title = "*Epic Title*";
            Console.ForegroundColor = ConsoleColor.Blue;
            Console.WindowHeight = 50;





            //DAY 5
            Eating eater01 = new Eating(/*name, food goes here if setting them in vs*//*);
            Console.WriteLine("Enter name of eater: ");
            eater01.eaterName = Console.ReadLine();
            
            Console.WriteLine("\nWhat food do you want to eat?");
            eater01.food1 = Console.ReadLine();
            //eater01.food2 = "Fish and Chips";

            Console.WriteLine("\nPress enter to start eating");

            while(eater01.stamina>0){
                Console.ReadKey();
                Console.WriteLine("\n" + eater01.eaterName + " has eaten " + eater01.food1);
                eater01.stamina--;
                eater01.eatingExperience+= 120f;
                Console.WriteLine("YOU ARE ON " + eater01.eatingExperience + " EXP");

                if(eater01.stamina<1){
                Console.WriteLine("\n" + eater01.eaterName + " is out of stamina; Press enter to rest and eat more.");
            }


            if(eater01.stamina<1){
                Console.ReadKey();
                Console.WriteLine("\n" + eater01.eaterName + " took a fat sleep and reagained stamina.");
                eater01.stamina = 4;
            }

            }
*/            

            







        

            //DAY 1

            //USER DETAILS QUESTIONING AND RESPONSES
/*            Console.WriteLine("Hello, what's your magnitude of fat?");

            double userFat = Convert.ToDouble( Console.ReadLine() );
            double maxFat = (userFat/2.2)*1000;

            Console.Write("WOW! You are " + userFat + " levels of fat. holy moly that's like " + maxFat + " grams.\n");



            Console.WriteLine("Now tell me your height in cm.");
            double userHeight = Convert.ToDouble(Console.ReadLine());

            if(userHeight > 200)
            {
                Console.WriteLine("Damn you're tall.");
            } else if(userHeight > 180)
            {
                Console.WriteLine("Meh average.");
            }else 
            {
                Console.WriteLine("Ha, Midget.");
            }


            Console.WriteLine("Wanna see something cool?\nType in your birth month and ill give you your zodiac sign");
            string userMonth = Console.ReadLine();

            switch (userMonth) {
                case "June":
                    Console.WriteLine("Your zodiac sign is :sunglasses:");
                    break;
                case "june":
                    Console.WriteLine("Your zodiac sign is :sunglasses:");
                    break;
                default:
                    Console.WriteLine("your zodiac sign is Retard");
                    break;
                
            }
*/


/*
            //DAY 2

            //POWER OF 2
            Console.WriteLine("How many powers of two do you want?");

            int powerNumber;

            //do is combined with while. code in the do brackets will be repeated until while condition is met
            do{
            powerNumber = Convert.ToInt32(Console.ReadLine());

            if(powerNumber>25){
                Console.WriteLine("the amount you have picked is too big, PICK AGAIN :gun:");
            }else{

            //for loop has syntax for{variable declaration; condition; specify what to repeat}.
            for (int x = 1; x <= powerNumber; x++)
            {
                double powerResult = Math.Pow(2, x); 
                Console.WriteLine(powerResult);
            }
            }
            }//while will keep repeating a codeblock until the condition in brackets is met. do can be combined with while
            while(powerNumber>25);



            //DIE ROLL
            Random deccaDie = new Random();

            int roll = 0;
            int attempts = 0;

            Console.WriteLine("press enter for deccadie");

            while(roll !=10) {
                Console.ReadKey();

                roll = deccaDie.Next(1, 11);

                Console.WriteLine("you rolled a " + roll);
                attempts++;
            }

            Console.WriteLine("WOOOOW wooohooo, are you happy you wasted " + attempts + " attempts equivalent of time trying to get a 
            meaningless number on the screen to define your meaningless existence");




            //DOUBLE DICE
            Random dice1 = new Random();
            Random dice2 = new Random();

            int roll1 = 0;
            int roll2 = 1;
            int doubleAttempts = 0;

            Console.WriteLine("press enter to doubleroll");

            while(roll1 != roll2) {
                Console.ReadKey();

                roll1 = dice1.Next(1, 7);
                roll2 = dice2.Next(1, 7);

                Console.WriteLine("you rolled a " + roll1 + " on die one and a " + roll2 + " on die two");
                doubleAttempts++;
            }

            Console.WriteLine("*luigi scream* you got two of the same number in " + doubleAttempts + " attempts. are you satisfied with yourself?");
*/            





/*            //DAY 3

            //displays ranking
            //arrays are variables which can hold multiple values
            string[] YouTubers = {"Markiplier", "KSI", "JackSepticeye", "Technoblade", "Red"};

            Console.WriteLine("Press enter for YouTuber rankings:");

            for (int y = 0; y < YouTubers.Length; y++)
            {
                Console.ReadKey();
                int ranking = y+1;
                Console.WriteLine(ranking + ") " + YouTubers[y]);
            }



            //asks and displays ranking
            string[] movies = new string[5];

            Console.WriteLine("\nType your four favorite movies:");

            for (int m = 0; m < movies.Length; m++)
            {
                movies[m] = Console.ReadLine();
            }

            Console.WriteLine("So here are your most favorite movies alphabetically: ");

            Array.Sort(movies);

            for (int m = 0; m < movies.Length; m++)
            {
                int moviesRankings = m+1;
                Console.WriteLine(moviesRankings + ". " + movies[m]);
            }



            //Lists require 'using System.Collections.Generic;' on top
            Console.WriteLine("\nI require to buy: ");

            List<string> shoppingList = new List<string>();

            shoppingList.Add("Emotions");
            shoppingList.Add("Biological Organ System");
            shoppingList.Add("Relationships");
            shoppingList.Add("Understanding of Humanity");
            shoppingList.Add("Conversational Skills");
            shoppingList.Add("Human Looks");

            for (int l = 0; l < shoppingList.Count; l++)
            {
                Console.WriteLine(shoppingList[l]);
            }

            shoppingList.Remove("Understanding of Humanity");
            //shoppingList.RemoveAt(3); can be used too^^



            //input your own list
            Console.WriteLine("\nHow many workers work in your branch? ");
            int workerNumber = Convert.ToInt32(Console.ReadLine());


            Console.WriteLine("Give names of the workers in any order: ");
            string[] workers = new string[workerNumber];

            for (int a = 0; a < workers.Length; a++)
            {
                workers[a] = Console.ReadLine();
            }

            Console.WriteLine("Here are the names of your workers arranged alphabetically: ");
            Array.Sort(workers);

            for (int a = 0; a < workers.Length; a++)
            {
                int alphNumber = a+1;
                Console.WriteLine(alphNumber + ": " + workers[a]);
            }
*/





/*            //DAY 4

            Console.WriteLine("Type in a sentence: ");

            string sentence = Console.ReadLine();

            //split function splits the sentence at whatever character given in paranthesis
            int wordCount = sentence.Split(' ').Length;

            Console.WriteLine("There are " + wordCount + " words in your sentence\n");




            //FUNCTIONS/METHODS
            Remainder(5, 2);
            Remainder(47, 4);
            Remainder(879, 47);

            int remainderResult = Remainder(39, 5);

            if(remainderResult % 2 == 0){
                Console.WriteLine("\nThe remainder of 39 and 5 is an even number.");
            }else{
                Console.WriteLine("\nThe remainder of 39 and 5 is an odd number.");
                }
*/




//            Console.ReadKey();
            


/*            //Methods or functions are used to call a whole code's actions anywhere with just the name
            //Static int to return int value and not void
            static int Remainder (int value1, int value2) {
                int remainderResult = value1 % value2;
                Console.WriteLine("The remainder is: " + remainderResult);
                return remainderResult;
            }
            

        }
    }

}
*/