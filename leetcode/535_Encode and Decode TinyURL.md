# 535. Encode and Decode TinyURL

Acceptance: 0.828
Difficulty: Medium
Skills: Dictionary, Hash
Solved: October 9, 2021

# Description

TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl` and it returns a short URL such as `http://tinyurl.com/4e9iAk`. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the `Solution` class:

- `Solution()` Initializes the object of the system.
- `String encode(String longUrl)` Returns a tiny URL for the given `longUrl`.
- `String decode(String shortUrl)` Returns the original long URL for the given `shortUrl`. It is guaranteed that the given `shortUrl` was encoded by the same object.

[Design URL Shortening service like TinyURL - LeetCode Discuss](https://leetcode.com/discuss/interview-question/124658/Design-a-URL-Shortener-(-TinyURL-)-System/)

# Sample Inputs

Give some valid inputs the candidate can expect to test their solution with.

- [https://leetcode.com/problems/design-tinyurl](https://leetcode.com/problems/design-tinyurl)

# Expected Outputs

For each sample input above, list the expected output. 

- [http://tinyurl.com/4e9iAk](http://tinyurl.com/4e9iAk)

# Example 1:

```python
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"

Explanation:
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after deconding it.
```

# Solutions

Provide possible solutions in common languages to this problem.

### Python

```python
class Codec:

    def __init__(self):
        self.num = 0
        self.shortToLong = {}
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        n = str(self.num)
        self.shortToLong[n] = longUrl #n will be a shortUrl
        self.num += 1
        return n;
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.shortToLong[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```

> Runtime: 59 ms, faster than 8.84% of Python3 online submissions for Encode and Decode TinyURL.
Memory Usage: 14 MB, less than 93.18% of Python3 online submissions for Encode and Decode TinyURL.
> 

```python
class Codec:
    def __init__(self): self.tiny_urls = {}
        
    def encode(self, L: str) -> str:
        num_form = random.randint(1,1E10) #shortUrl
        while num_form in self.tiny_urls: num_form = random.randint(1,1E10)
        self.tiny_urls[num_form] = L
        return 'http://tinyurl.com/' + str(num_form)

    def decode(self, S: str) -> str: return self.tiny_urls[int(S[19:])]
```

# 해설

해시테이블, 파이썬의 Dictionary를 이용하여 <ID, URL>와 같이 저장해둘 수 있다. 그러면, LongUrl이 필요할때(decode) 딕셔너리에서 Key가 ID인 Value를 찾아 반환하고, ShortUrl은 매번 새로운 값을 만들어 딕셔너리의 Key로 이용하고 해당 Key에 실제 Url을 저장할 수 있다.

기존 인터뷰에 나온 문제에 대한 해설 참고자료

[Design URL Shortening service like TinyURL - LeetCode Discuss](https://leetcode.com/discuss/interview-question/124658/Design-a-URL-Shortener-(-TinyURL-)-System/)