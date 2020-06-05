import java.io.*;
import java.util.*;

public class Counter
{
	private int count = 0;
	private int step = 0;

	public Counter()
	{
		count = 0;
		step = 1;
	}

	public Counter(int newCount, int newStep)
	{
		count = newCount;
		step = newStep;
	}

	void up()
	{
		count += step;
	}

	void down()
	{
		count -= step;
	}

	void resetCount()
	{
		count = 0;
	}

	int getCount()
	{
		return count;
	}

	void setCount(int newCount)
	{
		count = newCount;
	}

	void save() throws IOException
	{
		FileWriter fw = new FileWriter("count.sav");
		fw.write(count + "");
		fw.close();
	}

	void read()
	{
		Scanner input = null;
		try
		{
			input = new Scanner(new File("count.sav"));
			while(input.hasNextLine())
			{
				String line = input.nextLine();
				int storedValue = Integer.parseInt(line);
				setCount(storedValue);
			}

		}
		catch(FileNotFoundException e)
		{
			
		}
	}

}
