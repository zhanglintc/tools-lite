class Solution {
public:
    int maxnum;
    int maxPoints(vector<Point> &points) {
        if(points.size() == 0)
            return 0;
        if(points.size() == 1)
            return 1;
        if(points.size() == 2)
            return 2;
        int count(0);
        maxnum = 0;
        int distanceflag;
        int lenght,lenght1,lenght2;
        vector<Point>::reverse_iterator it1,it2,it3;
        while(1)
        {
            count = 2;
            it1 = points.rbegin();
            it2 = it1+1;
            lenght = getdistance(it1->x,it1->y,it2->x,it2->y);
            distanceflag = (it1->x - it2->x)>>31;
            for( ;it2 != points.rend(); ++it2)
            {
                for(it3 = it2+1; it3 != points.rend(); ++it3)
                {
                    lenght1 = getdistance(it1->x,it1->y,it3->x,it3->y);
                    lenght2 = getdistance(it2->x,it2->y,it3->x,it3->y);
                    if(isonline(lenght,lenght1,lenght2,checklenght(it3->x,it1->x,it2->x),distanceflag))
                        ++count;
                }
            }
            points.pop_back();
            setmaxnum(count);
            if(points.size() == 2)
            break;
        }
        return maxnum;
    }
    inline int checklenght(int thispoint, int pointone, int pointtwo)
    {
        if((thispoint > pointone) && (thispoint > pointtwo))
            return 1;
        else if((thispoint < pointone) && (thispoint < pointtwo))
            return -1;
        else
            return 0;
    }
    int getdistance(int x1, int y1, int x2, int y2)
    {
        int temp1,temp2;
        temp1=(x1-x2)*(x1-x2);
        temp2=(y1-y2)*(y1-y2);
        return (temp1+temp2);
    }
    inline bool isonline(int &lenght,int &lenght1,int &lenght2,int lenghtflag, int flag)
    {
        switch(lenghtflag)
        {
            case -1:
                if(flag == 0)
                    return ((lenght+lenght2) == lenght1)?true:false;
                else
                    return ((lenght+lenght1) == lenght2)?true:false;
            case 0:
                return ((lenght1+lenght2) == lenght)?true:false;
            case 1:
                if(flag ==0)
                    return ((lenght+lenght1) == lenght2)?true:false;
                else
                    return ((lenght+lenght1) == lenght2)?true:false;
            
            default:
                return false;
        }
    }
    inline void setmaxnum(int num)
    {
        if(num > maxnum)
            maxnum = num;
    }
};

