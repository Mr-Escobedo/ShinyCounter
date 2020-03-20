//Kevin C. Escobedo
//escobedo001@gmail.com

class CounterTests
{
	static Counter c;
	public static void main(String[] args)
	{
		c = new Counter(0, 1, "test.cnt");
		runAllTests();
	}

	static void runAllTests()
	{
		testUp();
		testDown();
	}

	static void testUp()
	{
		for(int i = 0; i < 10; i++)
		{
			c.up();
		}

		System.out.println("Counter should be 10: " + c.get_count());
	}

	static void testDown()
	{
		for(int i = 0; i < 10; i++)
		{
			c.down();
		}

		System.out.println("Counter should be 0: " + c.get_count());
	}
}
