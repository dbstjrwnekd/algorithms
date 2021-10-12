#include <string>
#include <vector>
#include <queue>
#include <sstream>
#include <iostream>

using namespace std;

vector<string> split(string str, char delimiter);

vector<int> solution(vector<string> operations)
{
    vector<int> answer;
    int count = 0;
    int deleted = 0;
    priority_queue<int, vector<int>> pq1;
    priority_queue<int, vector<int>, greater<int>> pq2;
    int max = 0;
    int min = 2147483647;

    for (int i = 0; i < operations.size(); i++)
    {
        vector<string> operation = split(operations[i], ' ');
        string op = operation[0];
        int num = stoi(operation[1]);
        if (op == "I")
        {
            count++;
            max = max > num ? max : num;
            min = min < num ? min : num;
            pq1.push(num);
            pq2.push(num);
        }
        else
        {
            if (deleted < count)
            {
                deleted++;
                if (num == 1)
                {
                    pq1.pop();
                }
                else
                {
                    pq2.pop();
                }
            }
        }
        if (deleted == count)
        {
            pq1 = priority_queue<int, vector<int>>();
            pq2 = priority_queue<int, vector<int>, greater<int>>();
        }
    }

    int temp = count - deleted;

    if (temp == 0)
    {
        answer.push_back(0);
        answer.push_back(0);
    }
    else
    {
        answer.push_back(pq1.top());
        answer.push_back(pq2.top());
    }

    return answer;
}

vector<string> split(string input, char delimiter)
{
    vector<string> answer;
    stringstream ss(input);
    string temp;

    while (getline(ss, temp, delimiter))
    {
        answer.push_back(temp);
    }

    return answer;
}
