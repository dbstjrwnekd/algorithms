#include <string>
#include <vector>

using namespace std;

string solution(string number, int k)
{
    if (k == 0)
        return number;
    string answer = "";
    vector<int> stack;
    for (int i = 0; i < number.size(); i++)
    {
        int num = (int)(number[i] - '0');
        while (stack.size() && stack.back() < num && k > 0)
        {
            k -= 1;
            stack.pop_back();
        }
        stack.push_back(num);
    }
    while (k > 0)
    {
        stack.pop_back();
        k -= 1;
    }

    for (int i = 0; i < stack.size(); i++)
    {
        answer += to_string(stack[i]);
    }
    return answer;
}
