"""
-------------------------
# Student Name: Quynh Dao
#-------------------------
"""
"""
from copy import deepcopy


class Student:

    def __init__(self, sid, last, first):
        """
        -------------------------------------------------------
        Description:
            Initializes a Student Object
            Stores student id, last name and first name
            Higher 4 digits in student id represent enrolment year
        Use: student = Student(sid, last, first)
        -------------------------------------------------------
        Parameters:
            sid - seven digit student id (int)
            last - student last name (str)
            first - student first name (str) 
        Returns:
            A Student object (Student)            
        -------------------------------------------------------
        """
        self.sid = sid
        self.last = last
        self.first = first
        
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Converst a Student Object to a string
        Use: my_string = str(student_object)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            'sid:last,first'           
        -------------------------------------------------------
        """     
        return str(self.sid) + ':' + self.last + ',' + self.first    

    def list(self):
        """
        -------------------------------------------------------
        Description:
            Converst a Student object to a list
        Use: my_list = student_object.list()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            [sid,last,first]           
        -------------------------------------------------------
        """
        return [self.sid, self.last, self.first]
    
    def key(self):
        """
        -------------------------------------------------------
        Description:
            Define a student key, which is the same as sid
        Use: student_key = student_object.key()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            sid - student id (int)           
        -------------------------------------------------------
        """
        return int(self.sid)
    
    def get_year(self):
        """
        -------------------------------------------------------
        Description:
            Returns the enrolment year of the student
        Use: y = student_obj.get_year()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            year - student enrolment year (int)           
        -------------------------------------------------------
        """
        return int(str(self.sid)[:4])
    
    def get_name(self):
        """
        -------------------------------------------------------
        Description:
            Returns the full name of a student in the following format
            'first last'
        Use: name = student_obj.get_name()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            name - student full name (str)           
        -------------------------------------------------------
        """
        return "{} {}".format(self.first, self.last)
    
    # Report 5 Task 1
    # def __eq__(self, other):
        # return self.sid == other

    def __ne__(self, other):
        return not self == other
        
    def __gt__(self, other):
        if self.sid > other:
            return True 
        
        elif self.sid < other:
            return False 
    
    def __ge__(self, other):
        return self == other or self > other 
    
    def __lt__(self, other):
        if self.sid < other:
            return True 
        
        elif self.sid > other:
            return False 
    
    def __le__(self, other):
        return self < other or self == other
    
    def __hash__(self):
        hash_sid = 0 
        # get the sum of the ASCII values
        for char in str(self.sid):
            hash_sid += ord(char)
        
        hash_value = self.sid ** hash_sid
        
        return (hash_value % 100000000)  # make sure the numbe isn't more than equal digits
    
    def __eq__(self, other):
        return self.key() == other.key()

        
class Course:

    def __init__(self, crn, students):
        """
        -------------------------------------------------------
        Description:
            Initializes a Course object
        Use: my_course = Course(crn,students)
        -------------------------------------------------------
        Parameters:
            crn - course number/code (str)
            students - a list of student objects (list)
        Returns:
            A Course object (Course)            
        -------------------------------------------------------
        """
        self.crn = crn
        self.students = deepcopy(students)
        
    def key(self):
        """
        -------------------------------------------------------
        Description:
            Define a course key, which is the same as crn
        Use: course_key = course_object.key()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            crn - course code (str)   
        -------------------------------------------------------
        """
        return self.crn
    
    def __contains__(self, student):
        """
        -------------------------------------------------------
        Description:
            Check if a student is registered in a course
            Comparison is done over the student key (sid)
        Use: student_obj in course_obj
        -------------------------------------------------------
        Parameters:
            student - a student object to search for (Student)
        Returns:
            True/False
        -------------------------------------------------------
        """
        registered = False
        for s in self.students:
            if s.key() == student.key():
                registered = True
                break
        return registered
    
    def register(self, student):
        """
        -------------------------------------------------------
        Description:
            Adds a student to the current course
            Does not add student if already registered
        Use: course_object.add(student_object)
        -------------------------------------------------------
        Parameters:
            student - a student (Student)
        Returns:
            None   
        -------------------------------------------------------
        """
        if student not in self:
            self.students.append(deepcopy(student))
        return
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            Checks if the course has any students
        Use: result = course_object.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True the students list is empty, False otherwise
        -------------------------------------------------------
        """
        return len(self.students) == 0
    
    def get_student(self, student_key):
        """
        -------------------------------------------------------
        Description:
            Checks if a student is registered in class,
            if found returns the a copy of student object
            If not found returns None
        Use: student = course_object.get_student(student_key)
        -------------------------------------------------------
        Parameters:
            student_key - a key of a studnet object (int)
        Returns:
            student - copy of student object (Student)
                      None if student is not in the course
        -------------------------------------------------------
        """
        for student in self.students:
            if student.key() == student_key:
                return deepcopy(student)
        
        return None
    
    def drop(self, student):
        """
        -------------------------------------------------------
        Description:
            Removes a student from the course
        Use: student = course_object.remove(student1)
        -------------------------------------------------------
        Parameters:
            student - a student object (Student)
        Returns:
            student - copy of removed student (Student)
                      None if student is not in the course
        -------------------------------------------------------
        """
        removed_student = None
        
        for i in range(len(self.students)):
            if student.key() == self.students[i].key():
                removed_student = deepcopy(self.students[i])
                del self.students[i]
                break
                
        return removed_student
            
    def count(self):
        """
        -------------------------------------------------------
        Description:
            Finds number of students registered in the course
        Use: num_students = course_obj.count()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            number of students (int)
        -------------------------------------------------------
        """
        
        return len(self.students)
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Convert course into a string in the following format:
            crn:student1,student2,student3,...
        Use: my_str = str(course_object)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            string representation of course (str)
        -------------------------------------------------------
        """
        course = '{}:'.format(deepcopy(self.crn))
        
        for i in self.students:
            course += '{},'.format(str(i.key()))
        
        if course.endswith(','):
            course = course[:-1]
            
        return course
    
    def merge(self, course2):
        """
        -------------------------------------------------------
        Description:
            Merget given course to current course
            current course will be updated to contain students from both courses
            course2 will become empty
        Use: course1.merge(course2)
        -------------------------------------------------------
        Parameters:
            course2: given course to be merged with current course (Course)
        Returns:
            None
        -------------------------------------------------------
        """
        students = deepcopy(course2.students)
        
        for student in students:
            self.register(student)
            course2.drop(student)
            
        return
    
    def split(self):
        """
        -------------------------------------------------------
        Description:
            splits a class into two sections
            The first section is current course, with first half of students, 
                crn changed to old_crnA
            The second section is a new course, with students second half of students
                crn is old_crnB
            If current course has one or no students, second course will be empty
        Use: course2 = course_object.split()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            course2 - a new course containing second half of student list (Course)
        -------------------------------------------------------
        """
        # Changing current course CRN
        code = deepcopy(self.crn)
        self.crn = '{}A'.format(code)
            
        # Creating new course with new CRN and empty student list
        crn2 = '{}B'.format(code)
        second_list = []
        course2 = Course(crn2, second_list)
            
        # If current course has an even # of students
        if len(self.students) > 1:
            if len(self.students) % 2 == 0:
                midpoint_index = len(self.students) / 2
            elif len(self.students) % 2 == 1:
                midpoint_index = int(len(self.students) / 2) + 1
                
            st_list = deepcopy(self.students)
            
            for i in range(len(st_list)):
                if i >= midpoint_index:
                    student = self.students[i]
                    course2.register(student)
                    
            while len(self.students) != midpoint_index:
                self.students.pop()
                          
        return course2
    
    def __hash__(self):
        hash_crn = 0 
        for char in self.crn: 
            hash_crn += ord(char) 
        hash_value = hash_crn ** hash_crn
        return hash_value % 100000000
    
