class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # if we use simple pattern it will break easily
        # for example, ":::" will break when we have ":"
        # ["hello", ":", "world"] -> "hello:::::::world" -> ["hello", "", ":world"]

        # record all length, then use '#' to append actual combined string
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append(",")
        res.pop() # remove last extra ","
        res.append("#")
        res.extend(strs)

        # input: ["hello", "world"] -> ["5", ",", "5", "#", "hello", "world"]
        return "".join(res)
        # output "5,5#helloworld"

    def decode(self, s: str) -> List[str]:
        # input "5,5#helloworld"
        if not s:
            return []
        # split only one time
        combined_sizes, combined_s = s.split("#", maxsplit=1)

        # split the sizes
        sizes = combined_sizes.split(",")
        
        # get all slices from the string
        res = []
        counter = 0
        for size in sizes:
            res.append(combined_s[counter:counter + int(size)])
            counter += int(size)
        return res
        
