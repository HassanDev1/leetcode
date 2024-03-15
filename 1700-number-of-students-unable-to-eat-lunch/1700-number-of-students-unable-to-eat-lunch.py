class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        st_q = deque(students)
        sa_q = deque(sandwiches)
        count = 0
        while st_q:
            if st_q[0] == sa_q[0]:
                st_q.popleft()
                sa_q.popleft()
                count = 0
            else:
                st_q.append(st_q.popleft())
                count += 1
                if count % len(st_q) == 0:
                    break
        return len(st_q)
                
        
                
        