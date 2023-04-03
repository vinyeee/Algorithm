import java.util.Scanner;
public class Main{
	public static void main(String[] args)
	{
		Scanner scanner = new Scanner(System.in);
		int number;
		int sum=1;
		int count=1;
		int start=1;
		int end=1;
		
		number=scanner.nextInt(); 
		
		while(true)
		{
			if(end==number)
			{
				break;
			}
			
			if(sum>number)
			{
				sum=sum-start;
				start++;
			}
			else if(sum<number)
			{  
				end++;
				sum=sum+end;
			}
			else if(sum==number)
			{
				end++;
				sum=sum+end;
				count++;
			}
		}
		
		System.out.println(count);
		
	}
}
