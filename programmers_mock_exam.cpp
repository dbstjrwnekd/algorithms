#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> answers)
{
    vector<int> answer;
    vector<vector<int>> scores = {
        {1, 2, 3, 4, 5},
        {2, 1, 2, 3, 2, 4, 2, 5},
        {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
    int max = 0;
    vector<int> sums = {0, 0, 0};
    for (int i = 0; i < answers.size(); i++)
    {
        for (int j = 0; j < sums.size(); j++)
        {
            if (answers[i] == scores[j][i % scores[j].size()])
                sums[j]++;
            if (max < sums[j])
                max = sums[j];
        }
    }
    for (int i = 0; i < sums.size(); i++)
    {
        if (sums[i] == max)
            answer.push_back(i + 1);
    }

    return answer;
}