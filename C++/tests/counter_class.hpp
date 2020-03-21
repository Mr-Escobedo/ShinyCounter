class Counter
{
private:
        int count;
        int step;
public:
        Counter(int pcount, int pstep);
        void up();
        void down();
        void reset_count(int new_count);
        void reset_step(int new_step);
        int get_count();
        int get_step();
	void write();
	void read();

};

