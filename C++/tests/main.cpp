#include <iostream>
#include "counter_class.cpp"
using namespace std;

int main()
{
	Counter c = Counter(0, 1);
	c.up();
	cout<<c.get_count()<<endl;
	return 0;
}
