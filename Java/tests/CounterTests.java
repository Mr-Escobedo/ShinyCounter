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
		testNewCount();
		testNewStep();
		testReadWriteToFile();
	}

	static void testUp()
	{
		for(int i = 0; i < 10; i++)
		{
			c.up();
		}

		assert c.get_count() == 10 : "ERROR: " + c.get_count() + " != 10";

	}

	static void testDown()
	{
		for(int i = 0; i < 10; i++)
		{
			c.down();
		}

		assert c.get_count() == 0 : "ERROR: " + c.get_count() + " != 0";
	}

	static void testNewCount()
	{
		c.set_count(100);
		assert c.get_count() == 100 : "ERROR: " + c.get_count() +  " != 100"; 
	}

	static void testNewStep()
	{
		c.set_step(5);
		for(int i = 0; i < 5; i++)
		{
			c.up();
		}

		assert c.get_count() == 125 : "ERROR: " + c.get_count() + " != 125";
	}

	static void testReadWriteToFile()
	{
		c.save();
		c.set_count(0);
		c.set_step(10);

		assert c.get_count() == 0 : "ERROR: " + c.get_count() + " != 0";

		c.read();

		assert c.get_count() == 125 : "ERROR: " + c.get_count() + " != 125";

	}
}
