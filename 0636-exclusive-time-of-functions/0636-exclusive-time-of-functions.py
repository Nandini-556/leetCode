class Solution:
    def exclusiveTime(self, n, logs):
        result = [0] * n
        stack = []
        prevTime = 0

        for log in logs:
            fid, typ, t = log.split(":")
            fid = int(fid)
            t = int(t)

            if typ == "start":
                if stack:
                    result[stack[-1]] += t - prevTime

                stack.append(fid)
                prevTime = t

            else:   # end
                result[stack.pop()] += t - prevTime + 1
                prevTime = t + 1

        return result