#include "counter_class.cpp"
#include <gtest/gtest.h>

TEST(CounterTest, goesUp)
{
	Counter c;
	ASSERT_EQ(0, c.get_count());
	c.up();
	ASSERT_EQ(1, c.get_count());
}

TEST(CounterTest, goesDown)
{
	int origin_count = 10;
	Counter c = Counter(origin_count, 1, ".cnt");
	ASSERT_EQ(origin_count, c.get_count());
	for(int i = 1; i < origin_count; i++)
	{
		c.down();
		ASSERT_EQ(origin_count-i, c.get_count());
	}
}

TEST(CounterTest, differentSteps)
{
	Counter c = Counter(0, 5, ".cnt");
	ASSERT_EQ(0, c.get_count());
	c.up();
	ASSERT_EQ(5, c.get_count());
	c.down();
	ASSERT_EQ(0, c.get_count());
}

TEST(CounterTest, newCount)
{
	Counter c;
	ASSERT_EQ(0, c.get_count());
	c.reset_count(100);
	ASSERT_EQ(100, c.get_count());
	c.up();
	c.reset_count(50);
	ASSERT_EQ(50, c.get_count());
}

TEST(CounterTest, newStep)
{
	Counter c;
	ASSERT_EQ(0, c.get_count());
	for(int i = 0; i < 5; i++)
	{
		c.up();
	}
	ASSERT_EQ(5, c.get_count());

	c.reset_step(5);
	c.down();
	ASSERT_EQ(0, c.get_count());
}

TEST(CounterTest, testWritingToFile)
{
	Counter c = Counter(0, 1, "test.cnt");
	for(int i = 0; i < 20; i++)
	{
		c.up();
	}
	ASSERT_EQ(20, c.get_count());

	c.write();

	std::string line;

	std::ifstream file(c.get_name());

	if(file.is_open())
	{
		getline(file, line);
		file.close();
	}

	int saved_count = std::stoi(line);

	ASSERT_EQ(saved_count, 20);
}

TEST(CounterTest, testReadingFromFile)
{
	int start = 100;
	Counter c = Counter(start, 1, "read.cnt");
	c.write();
	Counter c2 = Counter(0, 1, "read.cnt");
	ASSERT_EQ(start, c.get_count());
	ASSERT_EQ(0, c2.get_count());
	c2.read();
	ASSERT_EQ(start, c2.get_count());
}
	
int main(int argc, char** argv)
{
	testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
