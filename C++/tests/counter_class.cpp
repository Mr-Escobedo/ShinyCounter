#include "counter_class.hpp"

Counter::Counter(int pcount = 0, int pstep = 1, std::string pname = ".cnt")
	:count(pcount), step(pstep), name(pname)
	{}

void Counter::up()
{
	count += step;
}

void Counter::down()
{
	count -= step;
}

void Counter::reset_count(int new_count)
{
	count = new_count;
}

void Counter::reset_step(int new_step)
{
	step = new_step;
}

int Counter::get_count()
{
	return count;
}

int Counter::get_step()
{
	return step;
}

std::string Counter::get_name()
{
	return name;
}

void Counter::write()
{
	std::ofstream file;
	file.open(name);
	file << this->get_count();
	file.close();
}

void Counter::read()
{
	std::string line;
	std::ifstream file(name);
	if(file.is_open())
	{
		getline(file, line);
		file.close();
	}
	
	int new_count = std::stoi(line);

	this->reset_count(new_count);
}
