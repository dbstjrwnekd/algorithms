const Deque = require('./collections/deque'); //http://www.collectionsjs.com

const find_subarrays = function(arr, target) {
  result = [];
  // TODO: Write your code here
  let left = 0,
    product = 1;

  for (let right = 0; right<arr.length; right++) {
    product *= arr[right];

    while (product >= target && left <= right) {
      product /= arr[left];
      left++;
    }
    let tempList = new Deque();
    for (let i = right; i > left-1; i--) {
      tempList.unshift(arr[i]);
      result.push(tempList.toArray());
    }
  }

  return result;
};
