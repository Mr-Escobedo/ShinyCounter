#include "counter_class.hpp"

Counter::Counter(int pcount = 0, int pstep = 1)
	:count(pcount), step(pstep)
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
