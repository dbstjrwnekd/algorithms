#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve)
{
    set<int> losts(lost.begin(), lost.end());
    set<int> reserves(reserve.begin(), reserve.end());

    for (int i = 0; i < lost.size(); i++)
    {
        if (reserves.find(lost[i]) != reserves.end())
        {
            reserves.erase(lost[i]);
            losts.erase(lost[i]);
        }
    }

    vector<int> newList;
    newList.assign(losts.begin(), losts.end());
    sort(newList.begin(), newList.end());
    for (int i = 0; i < newList.size(); i++)
    {
        int lost_num = newList[i];
        if (0 < lost_num - 1 && lost_num - 1 <= n)
        {
            if (reserves.find(lost_num - 1) != reserves.end())
            {
                reserves.erase(lost_num - 1);
                losts.erase(lost_num);
                continue;
            }
        }
        if (0 < lost_num + 1 && lost_num + 1 <= n)
        {
            if (reserves.find(lost_num + 1) != reserves.end())
            {
                reserves.erase(lost_num + 1);
                losts.erase(lost_num);
                continue;
            }
        }
    }

    return n - losts.size();
}
