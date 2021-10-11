#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int step = 0;
    int days = (int)ceil((100-progresses[step])/(float)speeds[step]);
    int count = 0;
    while(step < progresses.size()){
        int step_days = (int)ceil((100-progresses[step])/(float)speeds[step]);
        if(step_days <= days){
            count++;
            step++;
        }else{
            answer.push_back(count);
            count = 0;
            days = step_days;
        }
    }
    if(count != 0) answer.push_back(count);
    return answer;
}
