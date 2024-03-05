class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda c: c[0])

        count = 0
        i = curr_end = 0

        while i < len(clips):
            if clips[i][0] > curr_end:
                return -1

            max_end = curr_end
            while i < len(clips) and clips[i][0] <= curr_end:
                max_end = max(clips[i][1], max_end)
                i += 1

            count += 1
            curr_end = max_end

            if curr_end >= time:
                return count

        return -1
