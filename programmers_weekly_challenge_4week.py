def solution(table, languages, preference):
    answer = []
    jobPreferScore = {}
    for info in table:
        job, five, four, three, two, one = info.split()
        jobPreferScore[job] = {five:5, four:4, three:3, two:2, one:1}
    
    maxScore = 0
    for job in sorted(jobPreferScore.keys(), reverse=True):
        score = 0
        for i in range(len(languages)):
            lang, pre = languages[i], preference[i]
            if lang in jobPreferScore[job]:
                score += jobPreferScore[job][lang] * pre
        if score >= maxScore:
            answer = job
            maxScore = score
    return answer
    