class Counter
{
private:
        int count;
        int step;
public:
        Counter(int pcount = 0, int pstep = 1);
        void up();
        void down();
        void reset_count(int new_count = 0);
        void reset_step(int new_step = 1);
        int get_count();
        int get_step();

};

