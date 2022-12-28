import java.util.Scanner;
public class myJavaProject{
	public static void main(String[] args){
//			   Scanner sc = new Scanner(System.in);
//			   int savings = sc.nextInt();
  //             
//			   if (savings>5000){
//					   System.out.println("Mrs. X");
//			   }
//			   else {
//			          System.out.println("Mrs. Y");
//			  
//			 }

//			 takes input and stores it in variable 'l'			   
             System.out.println("Enter the length");
             Scanner sc = new Scanner(System.in);
             int l = sc.nextInt(); 
           
//           making array
			 int marks[] = new int[l];  
             System.out.println("Enter your array:");
//           input array i as marks [0], marks[1]  till l-1 
//           loop used for increasing i
			 for(int i = 0; i<marks.length ;  i++ ){
			   Scanner ab = new Scanner(System.in);
               int rest = ab.nextInt();
               
               marks[i] = rest;
			}// for loop
	        
// the code above is working as below
//			 marks[0] = 100;
//			 marks[1] = 95;
//			 marks[2] = 95;
//			 marks[3] = 91;
//			 marks[4] = 100;
		
//          printing the array
            System.out.println("The array is: ");
			for(int i = 0; i<marks.length ; i++) {
				System.out.println(marks[i] );
					
			} // for loop
			//this loop has varable count and increases it by the value of marks[i]
			int sum1 = 0;
			int count = 0;
			for(int i = 0; i<marks.length;i++){
				sum1 = sum1 + marks[i];
				count = count + 1;
			}
			System.out.print("The sum of the array is ");
			System.out.println(sum1);
			System.out.print("The number of items in the array is ");
			System.out.println(count);
		//



	   }//for main function
}//for class
