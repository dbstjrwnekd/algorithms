function solution(cacheSize, cities) {
  if (cacheSize === 0) return cities.length * 5;

  let answer = 0;
  const cache = {};
  let curSize = 0;

  cities.forEach((cityName) => {
    const city = cityName.toLowerCase();

    Object.keys(cache).forEach((c) => (cache[c] += 1));

    if (city in cache) {
      cache[city] = 0;
      answer += 1;
    } else {
      answer += 5;
      if (curSize < cacheSize) {
        curSize += 1;
      } else {
        const maxCache = Object.keys(cache).sort(
          (a, b) => cache[b] - cache[a]
        )[0];
        delete cache[maxCache];
      }
      cache[city] = 0;
    }
  });

  return answer;
}
