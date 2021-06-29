/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let parens = { "[": "]", "{": "}", "(": ")" };
  let stack = [];
  for (let c of s) {
    if (c in parens) {
      stack.push(c);
    } else {
      if (stack.length === 0) return false;
      if (parens[stack.pop()] !== c) return false;
    }
  }
  if (stack.length !== 0) return false;
  return true;
};
