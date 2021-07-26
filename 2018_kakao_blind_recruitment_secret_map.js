function solution(n, arr1, arr2) {
  const answer = [];

  for (let i = 0; i < n; i++) {
    const num = arr1[i] | arr2[i];
    answer.push(get_row(num.toString(2).padStart(n, 0)));
  }

  return answer;
}

let get_row = (number) => {
  let row = "";
  for (let i = 0; i < number.length; i++) {
    if (number[i] == "0") row += " ";
    else row += "#";
  }
  return row;
};
