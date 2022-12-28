import java.util.Scanner;
//To print the sum of two number
public class test{
      public static void main(String[]args){
		  System.out.println("Hello World!");
		  // Talking user input
		  System.out.println("Enter first number");
		   Scanner sc = new Scanner(System.in);
		   int a = sc.nextInt();
          System.out.println("Enter second  number");
          Scanner ab = new Scanner(System.in);
		  int b = ab.nextInt();
		  int sum = a + b;
		  System.out.println("The sum is : ");
		  System.out.println(sum);
                 
      }	      
}	
