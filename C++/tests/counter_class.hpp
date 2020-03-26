#include <string>
#include <iostream>
#include <fstream>


class Counter
{
private:
        int count;
        int step;
	std::string name;
public:
        Counter(int pcount, int pstep, std::string pname);
        void up();
        void down();
        void reset_count(int new_count);
        void reset_step(int new_step);
        int get_count();
        int get_step();
	std::string get_name();
	void write();
	void read();

};

