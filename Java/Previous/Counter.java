//Author: Kevin C. Escobedo
//Email: escobedo001@gmail.com
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.FileWriter;
import java.io.IOException;

class Counter
{
	int count;
	int step;
	String fileName;
	public Counter(int count, int step, String fileName)
	{
		this.count = count;
		this.step = step;
		this.fileName = fileName;
	}

	void up()
	{
		this.count += this.step;
	}

	void down()
	{
		this.count -= this.step;
	}

	int get_count()
	{
		return this.count;
	}

	int get_step()
	{
		return this.step;
	}

	void set_count(int newCount)
	{
		this.count = newCount;
	}

	void set_step(int newStep)
	{
		this.step = newStep;
	}

	void save()
	{
		try
		{
			FileWriter file = new FileWriter(this.fileName);
			int data = this.get_count();
			file.write(Integer.toString(data));
			file.close();
		}
		catch(IOException e)
		{

		}
	}

	void read()
	{
		try
		{
			File file = new File(this.fileName);
			Scanner reader = new Scanner(file);
			while(reader.hasNextLine())
			{
				String data = reader.nextLine();
				this.set_count(Integer.parseInt(data));
			}
			reader.close();
		}
		catch(FileNotFoundException e)
		{

		}
	}
}
