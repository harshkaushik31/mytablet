import java.util.Scanner;
public class newBegining{
// write your code here		
		public static void main(String[] args){
		System.out.println("Namaste World");
		
		System.out.println("Enter the number of rows");
		Scanner sc = new Scanner(System.in);
		int row = sc.nextInt();

		System.out.println("Enter the number of columns");
		Scanner hi = new Scanner(System.in);
		int col = hi.nextInt();

		for(int i = 0; i<row; i++){
		    for(int j = 0; j<col; j++){
			    System.out.print("* ");
			}
			System.out.println(" ");

		}
		
		}		
}
// this is extra
