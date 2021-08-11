function solution(record) {
  const answer = [];
  const actions = [];
  const uids = [];
  const userInfo = {};

  record.forEach((r) => {
    const [action, uid, nick] = r.split(" ");
    switch (action) {
      case "Enter":
        actions.push("님이 들어왔습니다.");
        userInfo[uid] = nick;
        uids.push(uid);
        break;
      case "Change":
        userInfo[uid] = nick;
        break;
      case "Leave":
        actions.push("님이 나갔습니다.");
        uids.push(uid);
        break;
    }
  });

  actions.forEach((action, i) => {
    answer.push(userInfo[uids[i]] + action);
  });

  return answer;
}
