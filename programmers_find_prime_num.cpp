#include <string>
#include <vector>
#include <cmath>
#include <iostream>
#include <set>

using namespace std;

void getPrimeSum(string numbers, int *sum, vector<bool> pos, string found, set<int> &table);
bool isPrime(int num);

int solution(string numbers)
{
    int answer = 0;
    set<int> table;
    vector<bool> pos(numbers.size(), false);
    getPrimeSum(numbers, &answer, pos, "", table);
    return answer;
}

void getPrimeSum(string numbers, int *sum, vector<bool> pos, string found, set<int> &table)
{
    int num = atoi(found.c_str());
    if (*table.find(num) == table.size())
    {
        if (isPrime(num))
            *sum += 1;
        table.insert(num);
    }
    for (int i = 0; i < numbers.size(); i++)
    {
        if (!pos[i])
        {
            pos[i] = true;
            string next_string = found + numbers[i];
            getPrimeSum(numbers, sum, pos, next_string, table);
            pos[i] = false;
        }
    }
}

bool isPrime(int num)
{
    if (num < 2)
        return false;
    if (num == 2)
        return true;
    for (int i = 2; i <= sqrt(num) + 1; i++)
    {
        if (num % i == 0)
            return false;
    }
    return true;
}