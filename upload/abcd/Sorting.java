package S;

class Sorting {

	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		int Number[]={1, 6, 2, 4, 5};
		int i,j,temp;
		int count=Number.length;
		float m;
		System.out.print("Given list:");
		for(i=0;i<count;i++);
		{
			for(j=i+1;j<count;j++);
			{
				if(Number[i]<Number[j])
				{
					temp=Number[i];
					Number[i]=Number[j];
					Number[j]=temp;
					j++;
				}
					
			}
		}
	}

}
