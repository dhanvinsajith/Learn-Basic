using System;

namespace giraffe
{
/*  //CLASSES
    class Phone
    {
        public string company;
        public int modelYear;
        public string modelName;
        public string userName;
        public int sellingPrice;
        public string condition;
        public bool isNegotiable;
        public int buyYear;
    }
*/


/*  //CONSTRUCTORS AND OBJECT METHODS
    class Book
    {
        public int _pages;

        public Book(string title, string author, int pages)
        {
            _pages = pages;
            
            if(LongBook() == true){
                Console.WriteLine(title + " is a book written by " + author + " and it is a long read with " + pages + " pages." + "\n\n------------------------------------------------------------------------\n\n");
            }else{
            Console.WriteLine(title + " is a book written by " + author + " and it is a short read with " + pages + " pages." + "\n\n------------------------------------------------------------------------\n\n");
            }
        }

        //object method vv & constructor ^^

        public bool LongBook()
        {
            if(_pages >= 300){
                return true;
            }
            return false;
        }
    }
*/


/*   //GETTERS AND SETTERS && STATIC CLASS ATTRIBUTES
    class Movie
    {
        private string rating;

        //static variable belongs to the class itself and is called by: Movie.movieCount
        private static int movieCount = 0;

        //variables title, studio and rating belong to each mmovie created
        public Movie(string title, string studio, string _rating)
        {
            Rating = _rating;
            _rating = rating;
            movieCount++;

            Console.WriteLine(movieCount + ".) The movie " + title + " by " + studio + " studios is rated " + _rating);
        }

        //makes sure invalid values cannot be set to rating variable
        public string Rating
        {
            get {return rating;}
            set { 
                if(value == "G" || value == "PG" || value == "PG-13" || value == "PG-15" || value == "R" || value == "TBD"){
                    rating = value;
                }else{
                    rating = "TBD (invalid rating inserted)";
                }
            }
        }
    }
*/


/*  //STATIC METHODS AND CLASSES
    //making it- static class Arith -will not allow you to make instances of it in the program
    class Arith
    {
        //virtual is required for overwriting
        public virtual void Startup()
        {
            Console.WriteLine("Arith starting up...");
        }

        public static void Add(int add1, int add2)
        {
            Console.WriteLine(add1 + add2);
        }

        public static void Subtract(int sub1, int sub2)
        {
            Console.WriteLine(sub1 - sub2);
        }

        public static void Multiply(int mult1, int mult2)
        {
            Console.WriteLine(mult1 * mult2);
        }

        public static void Divide(int div1, int div2)
        {
            Console.WriteLine(div1 / div2);
        }

        public static void Exponent(int exp1, int exp2)
        {
            int result = 1;
            for (int i = 0; i < exp2; i++)
            {
                result *= exp1;
            }

            Console.WriteLine(result);
        }

        public static void Sqrt(int sqr1)
        {
            Console.WriteLine(Math.Sqrt(sqr1));
        }
    }
*/


/*    //INHERITANCE
    //vv now maths class has all properties of arith class AND anything more you put inside it
    class Maths : Arith
    {
        public static void Trigonometry()
        {
            Console.WriteLine("User Performs Trigonometry");
        }

        public static void Geometry()
        {
            Console.WriteLine("User Performs Geometrical Calculations");
        }

        public static void Series()
        {
            Console.WriteLine("User Performs Pattern Calculations");
        }

        public static void Percentage()
        {
            Console.WriteLine("User Performed Percentage Calculations");
        }

        //specifically overwrite a specific method from the inherited class
        public override void Startup()
        {
            Console.WriteLine("Maths starting up...");
        }
    }
*/



    class Program
    {
        static void Main(string[] args)
        {
/*          //WORKING WITH STRINGS
            string opening = "Hello World!";
            Console.WriteLine(opening.Length);
            Console.WriteLine(opening.ToUpper());
            Console.WriteLine(opening.ToLower());
            Console.WriteLine(opening.Contains("!"));
            Console.WriteLine(opening[11]);
            Console.WriteLine(opening.IndexOf("or"));
            Console.WriteLine(opening.Substring(6, 5));
*/


/*          //WORKING WITH NUMBERS
            int num = 9;
            num++; //adds 1
            num--; //negates 1
            Console.WriteLine(Math.Abs(-40));
            Console.WriteLine(Math.Pow(num, 2));
            Console.WriteLine(Math.Sqrt(num));
            Console.WriteLine(Math.Max(27, 30));
            Console.WriteLine(Math.Min(27, 30));
            Console.WriteLine(Math.Round(6.60));
*/


/*          //GETTING USER INPUT
            Console.WriteLine("Enter your Name: ");
            string name = Console.ReadLine();
            Console.WriteLine("Enter your Age: ");
            int age = Convert.ToInt32(Console.ReadLine());
            int year = 2021-age;

            Console.WriteLine("Hello, " + name + " who was born in " + year + "." );
*/


/*          //MADLIB
            Console.WriteLine("LET'S PLAY A MAD LIB!");

            string lib1, lib2, lib3, lib4, lib5, lib6;

            Console.Write("Insert a Noun(plural): ");
            lib1 = Console.ReadLine();
            Console.Write("Insert an Occupation: ");
            lib2 = Console.ReadLine();
            Console.Write("Insert an Animal(plural): ");
            lib3 = Console.ReadLine();
            Console.Write("Insert a Place: ");
            lib4 = Console.ReadLine();
            Console.Write("Insert a Verb: ");
            lib5 = Console.ReadLine();
            Console.Write("Insert a Noun: ");
            lib6 = Console.ReadLine();

            Console.WriteLine("----------------------------------------------------------");

            Console.WriteLine("In the book War of the " + lib1 + ", the main character is an anonymous " + lib2 + 
                              "\nwho records the arrival of " + lib3 + " in " + lib4 + ". Needless to say, havoc reigns as the\n" + lib3 + 
                              " continue to " + lib5 + " everything in sight, until they are killed by the \ncommon " + lib6 + ".");
*/                



/*          //ARRAYS
            int[] luckyNumbers = {7, 14, 13, 27, 64, 256, 999};
            luckyNumbers[1] = 9;
            Random rol = new Random();
            int dec = rol.Next(0, 7);
            Console.WriteLine("YOUR lucky number is " + luckyNumbers[dec]);
*/


/*          //METHODS
            Console.WriteLine("Press enter to begin identification process...");
            Console.ReadKey();
            MeetNGreet(447);
            MeetNGreet(448);
*/


/*          //RETURN TYPES
            Console.WriteLine(cube(16));
            Console.WriteLine(cube(13));
            Console.WriteLine(cube(9));
            Console.WriteLine(cube(27));
*/


/*          //IF STATEMENTS
            Console.Write("Enter marks out of 100: ");
            int marks = Convert.ToInt32(Console.ReadLine());
            if(marks > 75){
                if(marks > 90){
                    Console.WriteLine("Keep It Up");
                }else{
                    Console.WriteLine("Well Done, Can do Better");
                }
            }else if(marks < 76 && marks > 50){
                Console.WriteLine("Try harder for Next Exam");
            }else{
                Console.WriteLine("You need to try a LOT harder");
            }
*/


/*          //BETTER CALCULATOR
            Console.Write("Enter first number: ");
            double num1 = Convert.ToDouble(Console.ReadLine());

            Console.Write("Enter second number: ");
            double num2 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("------------------------------------------");

            Console.Write("What do you want to do with the mubers(Enter operator: +, -, *, /): ");
            string op = Console.ReadLine();

            Console.WriteLine("------------------------------------------");

            if(op == "+"){
                Console.WriteLine("The answer to " + num1 + op + num2 + " = " + (num1+num2));
            }else if(op == "-"){
                Console.WriteLine("The answer to " + num1 + op + num2 + " = " + (num1-num2));
            }else if(op == "*"){
                Console.WriteLine("The answer to " + num1 + op + num2 + " = " + (num1*num2));
            }else if(op == "/"){
                Console.WriteLine("The answer to " + num1 + op + num2 + " = " + (num1/num2));
            }else{
                Console.WriteLine("Cannot be Calclated. Invalid Operator");
            }
*/


/*          //SWITCH STATEMENTS
            Console.Write("Give me Month Number: ");
            int _monthNum = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Your corresponding month is " + GetMonth(_monthNum-1));
*/


/*          //WHILE LOOPS
            int index = 1000;
            int _index = 0;
            while(_index<index){
                Console.WriteLine("Still smaller" + index);
                index++;
                _index += 2;
            }

            //do while combination
            int year = 2000;
            int height = 10;
            //int _year;
            do{
                Console.WriteLine("small- " + height + "cm- " + year);
                year++;
                height += 19 - (year - 2000);
            }while(height < 180);
*/


/*          //GUESSING GAME
            string secretWord = "Batmobile";
            string userGuess = "";
            int x = 0;
            Console.WriteLine("Guess the word!");
            while(userGuess != secretWord && userGuess != "batmobile"){
                userGuess = Console.ReadLine();
                if(x == 1){
                    Console.WriteLine("\nCLUE 1: IT IS A VEHICLE");
                }
                else if(x == 2){
                    Console.WriteLine("\nCLUE 2: IT IS BLACK IN COLOR");
                }
                else if(x == 3){
                    Console.WriteLine("\nCLUE 3: IT BELONGS TO A SUPERHERO");
                }
                else if(x == 4){
                    Console.WriteLine("\nCLUE 4: IT TRANSFORMS A LOT");
                }
                if(userGuess != secretWord && userGuess != "batmobile" && x != 9){
                    Console.WriteLine("\nTry Again");
                }
                x++;
                if(x == 10){
                    break;
                }
            }
            if(x != 10){
                Console.WriteLine("--------------------------------------------------------------------- \nding ding ding! You guessed right. The word was 'Batmobile'");
            }
            else{
                Console.WriteLine("--------------------------------------------------------------------- \nYou Failed to guess in 10 attempts.");
            }
*/


/*          //FOR LOOPS
            Console.Write("Enter diamond length: ");

            int n = Convert.ToInt32(Console.ReadLine());
            int diamondLength;

            if(n%2 == 0){
                diamondLength = (n/2)+1;
            }else{
                diamondLength = ((n+1)/2);
            }

            Console.WriteLine("\nThe closest Diamond is: \n------------------------------------------------------------------\n");

            //top half
            for (int i = 0; i < diamondLength+1; i++)
            {
                for (int j = 1; j < (diamondLength+1)-i; j++)
                {
                    Console.Write(" ");
                }
                for (int k = 1; k < i+1; k++)
                {
                    Console.Write("* ");
                }
                Console.WriteLine();
            }

            //bottom half
            for (int h = diamondLength-1; h > 0; h--)
            {
                for (int l = diamondLength-h; l > 0; l--)
                {
                    Console.Write(" ");
                }
                for (int m = h; m > 0; m--)
                {
                    Console.Write("* ");
                }
                Console.WriteLine();
            }
*/


/*          //EXPONENT METHOD
            Console.Write("Enter a number: ");
            int int1 = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter it's power: ");
            int int2 = Convert.ToInt32(Console.ReadLine());
            Exponent(int1, int2);

            Console.WriteLine("\n--------------------------------------------\n\nThe final result is " + Exponent(int1, int2));
*/


/*          //DOUBLE ARRAY (each subpart can be any length)
            string[][] tierList;
            tierList = new string[][]
            {
                new string[]{
                "Kay/O", "Skye", "Sova", "Viper" },
                new string[]{
                "Astra", "Breach", "Cypher", "Jett", "Killjoy", "Omen", "Phoenix", "Raze", "Reyna", "Sage" },
                new string[]{
                "Brimstone", "Yoru" }
            };

            Console.WriteLine("The new agent is " + tierList[0][0]);
            Console.WriteLine("The worst agent is still " + tierList[2][1]);
            Console.Write("The most balanced agents are: ");

            for (int i = 0; i < 10; i++)
            {
                Console.Write(tierList[1][i] + " ");
            }
*/


/*          //2D ARRAYS (all subparts have to be same length)
            int[,] numPad = {
                {1, 2},
                {3, 4},
                {5, 6},
                {7, 8},
                {9, 0},
            };

            Console.WriteLine(numPad[2, 1] + numPad[4, 0] + numPad[0, 1]);
*/


/*          //EXCEPTION HANDLING
            try{
                Console.Write("\nEnter divident: ");
                int num1 = Convert.ToInt32(Console.ReadLine());
                
                Console.Write("Enter divisor: ");
                int num2 = Convert.ToInt32(Console.ReadLine());

                int num3 = num1/num2;
                Console.WriteLine("\n------------------------------------\n\nThe quotient is: " + num3);
            }
            //catch finds out error in try block and executes its code if anything is wrong.
            //executes code for any error found
            catch(Exception e){
                Console.WriteLine("\n------------------------------------\n\nError in entered values. (" + e.Message + ")");
            }
            //You can also put in exception name in catch block paranthesis to make it find only specific errors
            catch(DivideByZeroException z){
                Console.WriteLine("\n------------------------------------\n\nError in entered values. (" + z.Message + ")");
            }
            catch(FormatException f){
                Console.WriteLine("\n------------------------------------\n\nError in entered values. (" + f.Message + ")");
            }
            //Code in finally will be executed no matter what
            finally{
                Console.WriteLine("This will be printed out no matter what.");
            }
*/


/*          //CLASSES
            Phone user1 = new Phone();
            Console.Write("Name: ");
            user1.userName = Console.ReadLine();

            Console.Write("Phone Company Name: ");
            user1.company = Console.ReadLine();

            Console.Write("Model Name: ");
            user1.modelName = Console.ReadLine();

            Console.Write("Manufacturing Year: ");
            user1.modelYear = Convert.ToInt32(Console.ReadLine());

            Console.Write("Year is was Bought: ");
            user1.buyYear = Convert.ToInt32(Console.ReadLine());

            Console.Write("Phone Condition: ");
            user1.condition = Console.ReadLine();

            Console.Write("Selling Price: ");
            user1.sellingPrice = Convert.ToInt32(Console.ReadLine());

            Console.Write("Price Negotiable? (yes/no): ");
            string negotiability = Console.ReadLine();
            int x = 0;
            while(x == 0){
                if(negotiability == "no"){
                    user1.isNegotiable = false;
                    x = 1;
                }else if(negotiability == "yes"){
                    user1.isNegotiable = true;
                    x = 1;
                }else{
                    Console.Write("\nPlease choose between 'yes' or 'no': ");
                    negotiability = Console.ReadLine();
                }
            }
            Console.WriteLine("\n------------------------------------------------\n\n");

            Console.WriteLine("SELLING " + user1.company + " " + user1.modelName + " " + user1.modelYear + ".\n\n" + 
                              user1.company + " " + user1.modelName + " " + user1.modelYear + " for sale by " + user1.userName + " at a price of " + user1.sellingPrice + "$.\n" +
                              "The phone is in " + user1.condition + " condition and is " + (2021 - user1.buyYear) + " years old.");
            if(user1.isNegotiable){
                Console.WriteLine("**PRICE IS NEGOTIABLE**");
            }else{
                Console.WriteLine("**PRICE IS NOT NEGOTIABLE**");
            }
            Console.WriteLine("Further details will be given after the price has been settled and the deal has been made.");
*/


/*          //CONSTRUCTORS AND OBJECT METHODS
            Book book1 = new Book("Harry Potter", "J.K Rowling", 500);
            Book book2 = new Book("Lord Of The Rings", "Tolkein", 800);
            Book book3 = new Book("The BFG", "Roald Dahl", 250);
*/


/*          //GETTERS AND SETTERS && STATIC CLASS ATTRIBUTES
            Movie movie1 = new Movie("Loki", "Marvel", "PG-13");
            Movie movie2 = new Movie("Haikyuu!", "Production I.G", "PG");
            Movie movie3 = new Movie("Godzilla", "Toho", "ass");
*/


/*          //STATIC METHODS AND CLASSES && INHERITANCE
            Arith.Add(27, 14);
            Arith.Subtract(24, 8);
            Arith.Multiply(8, 6);
            Arith.Divide(120, 6);
            Arith.Exponent(5, 3);
            Arith.Sqrt(289);

            Arith arith1 = new Arith();
            arith1.Startup();
            Maths maths1 = new Maths();
            maths1.Startup();
*/

            

            Console.ReadKey();
        }


/*      //METHODS
        static void MeetNGreet(int userNumber)
        {
            Console.WriteLine("Enter your Name: ");
            string name = Console.ReadLine();
            Console.WriteLine("Enter your Age: ");
            int age = Convert.ToInt32(Console.ReadLine());
            int year = 2021-age;

            Console.WriteLine("User number " + userNumber + ": " + "Hello, " + name + " who was born in " + year + "." );
        }
*/

/*      //RETURN TYPES
        static int cube(int side)
        {
            int cubed = side * side * side;
            return cubed;
        }
*/

/*      //SWITCH STATEMENTS
        static string GetMonth(int monthNum)
        {
            string monthName;

            switch(monthNum){
                case 0:
                    monthName = "January";
                    break;
                case 1:
                    monthName = "February";
                    break;
                case 2:
                    monthName = "March";
                    break;
                case 3:
                    monthName = "April";
                    break;
                case 4:
                    monthName = "May";
                    break;
                case 5:
                    monthName = "June";
                    break;
                case 6:
                    monthName = "July";
                    break;
                case 7:
                    monthName = "August";
                    break;
                case 8:
                    monthName = "September";
                    break;
                case 9:
                    monthName = "October";
                    break;
                case 10:
                    monthName = "November";
                    break;
                case 11:
                    monthName = "December";
                    break;
                default:
                    monthName = "Invalid Month Number";
                    break;

            }

            return monthName;
        }
*/

/*      //EXPONENT METHOD
        static int Exponent(int num, int pow){
            int result = 1;
            for (int i = 0; i < pow; i++)
            {
                result *= num;
            }

            return result;
        }
*/


    }
}
