package S;
class PiggyBank
{
	int bal,lt;
	void deposit(int x)
	{
		this.bal=this.bal+x;
		this.lt=+x;
	}
	void withdraw(int x)
	{
		this.bal=this.bal-x;
		this.lt=+x;
	}
	void print()
	{
		System.out.println("Balance ="+this.bal);
		System.out.println("Last Transition ="+this.lt);
	}
}
class BankAccount
{
	public static void main (String [] args)
	{
		System.out.println("Welcome to PiggyBank");
		PiggyBank h1=new PiggyBank();
		PiggyBank h2=new PiggyBank();
		h1.print();
		h1.deposit(12333);
		h1.print();
		h1.withdraw(2333);
		h1.print();
		h2.print();
		h2.withdraw(2000000000);
		h2.print();
	}
}
	