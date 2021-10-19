#include <string>
#include <vector>

using namespace std;

void dfs(int depth, int sum, int target, vector<int> numbers, int &answer);

int solution(vector<int> numbers, int target)
{
    int answer = 0;
    dfs(0, 0, target, numbers, answer);
    return answer;
}

void dfs(int depth, int sum, int target, vector<int> numbers, int &answer)
{
    if (depth == numbers.size())
    {
        if (sum == target)
        {
            answer++;
        }
        return;
    }
    dfs(depth + 1, sum + numbers[depth], target, numbers, answer);
    dfs(depth + 1, sum - numbers[depth], target, numbers, answer);
}
