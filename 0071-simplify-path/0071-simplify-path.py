class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for segment in path.split('/'):
            if segment == "..":
                if stack:
                    stack.pop()
            elif segment == "." or not segment:
                continue
            else:
                stack.append(segment)
        return "/" + "/".join(stack)
