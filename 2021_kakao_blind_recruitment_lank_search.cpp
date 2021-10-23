#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>
#include <iostream>

using namespace std;

vector<string> split(string input, char delimiter);
int getScores(string query);
map<string, vector<int>> hm;

vector<int> solution(vector<string> info, vector<string> query)
{
    vector<int> answer;
    string pos[4][2] = {
        {"-"},
        {"-"},
        {"-"},
        {"-"}};
    for (string data : info)
    {
        vector<string> datas = split(data, ' ');
        for (int i = 0; i < datas.size() - 1; i++)
        {
            pos[i][1] = datas[i];
        }
        for (int i = 0; i < 2; i++)
        {
            for (int j = 0; j < 2; j++)
            {
                for (int k = 0; k < 2; k++)
                {
                    for (int l = 0; l < 2; l++)
                    {
                        string key = pos[0][i] + pos[1][j] + pos[2][k] + pos[3][l];
                        hm[key].push_back(atoi(datas[datas.size() - 1].c_str()));
                    }
                }
            }
        }
    }

    for (auto &instance : hm)
    {
        sort(instance.second.begin(), instance.second.end());
    }

    for (string q : query)
    {
        answer.push_back(getScores(q));
    }

    return answer;
}

int getScores(string query)
{
    vector<string> datas = split(query, ' ');
    string key = "";
    for (int i = 0; i < datas.size() - 1; i++)
    {
        if (datas[i] != "and")
            key += datas[i];
    }
    int num = atoi(datas[datas.size() - 1].c_str());

    return hm[key].end() - lower_bound(hm[key].begin(), hm[key].end(), num);
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
