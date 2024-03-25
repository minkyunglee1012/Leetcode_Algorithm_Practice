class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students and sandwiches[0] in students:
            if students[0] != sandwiches[0]:
                pop = students.pop(0)
                students.append(pop)

            else:
                students.pop(0)
                sandwiches.pop(0)

        return len(students)