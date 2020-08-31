"""
-------------------------
# Student Name: Quynh Dao
#-------------------------
"""
from data import Student, Course


def file_to_students(filename):
    """
    -------------------------------------------------------
    Description:
        Reads contents of given file into a list of Student Objects
        Each line in file is formatted as:
        sid:last,first
    Use: students = file_to_students(filename)
    -------------------------------------------------------
    Parameters:
        filename - name of file (str)
    Returns:
        students - list of student objects (list)            
    -------------------------------------------------------
    """
    students = []
    
    f = open(filename, 'r')
    
    for line in f:
        int1 = line.find(':')
        int2 = line.find(',')
        
        sid = line[:int1]
        last = line[int1 + 1:int2]
        first = line[int2 + 1:].strip('\n')
        student = Student(sid, last, first)
        students.append(student)
        
    return students

    
def file_to_course(filename):
    """
    -------------------------------------------------------
    Description:
        Reads contents of given file into a Course object
        First line in the file contains course CRN
        The following lines are formatted as:
        sid:last,first
    Use: course = file_to_course(filename)
    -------------------------------------------------------
    Parameters:
        filename - name of file (str)
    Returns:
        course - a course object (Course)            
    -------------------------------------------------------
    """
    f = open(filename, 'r')
    crn = f.readline().strip('\n')
    students = []
    
    for line in f:
        int1 = line.find(':')
        int2 = line.find(',')
        
        sid = line[:int1]
        last = line[int1 + 1:int2]
        first = line[int2 + 1:].strip('\n')
        student = Student(sid, last, first)
        students.append(student)

    course = Course(crn, students)
    return course


def get_batches(course):
    """
    -------------------------------------------------------
    Description:
        Breaks students registered in the course into batches
        A list containing sets, each representing a batch
        A student batch is a set containing students enroled in the same year
    Use: batches = get_batches(course)
    -------------------------------------------------------
    Parameters:
        course - a course object (Course)
    Returns:
        batches - list of sets (list)            
    -------------------------------------------------------
    """
    years = []
    batches = []
    
    for i in range(len(course.students)):
        student_id = course.students[i].key()
        year = str(student_id[:4])
        if year not in years:
            years.append((year))
            
    for i in range(len(years)):
        batches.append(set())
    
    for i in range(len(years)):
        for j in range((len(course.students))):
            if years[i] in course.students[j].key():
                batches[i].add(course.students[j])
    
    return batches


class Department:

    def __init__(self, name, programs, instructors, students):
        self.name = name
        self.programs = programs
        self.instructors = instructors
        self.students = students
        
    def program_count(self):
        return len(self.programs)
    
    def instructor_count(self):
        return len(self.instructors)
    
    def student_count(self):
        return len(self.students)
    
    def key(self):
        return self.name
    
    def __str__(self):
        string = self.name + ':'
        attributes = ['programs', 'instructors', 'students']
        for i in range(len(attributes)):
            string += '(' + attributes[i] + ':'
            if i == 0:
                string += str(self.program_count())
            if i == 1:
                string += str(self.instructor_count())
            if i == 2:
                string += str(self.student_count())
            string += ')'
        return string
    
    def get_students(self):
        keys = []
        for i in range(len(self.students)):
            keys.append(self.students[i].sid)
        return keys
    
    def is_closed(self):
        result = False
        if self.program_count() == 0:
            result = True
        return result
    
    def __contains__(self, substring):
        result = False
        if type(substring) == str:
            if substring in self.programs:
                result = True
            elif substring in self.instructors:
                result = True
        else:
            for i in range(len(self.students)):
                if substring.key() == self.students[i].key():
                    result = True
        return result
        
    def list(self):
        return [self.name, self.programs, self.instructors, self.students]
    
    def get_batch(self, year):
        years = []
        values = []
        
        for i in range(len(self.get_students())):
            string = str(self.students[i])
            if int(string[:4]) not in years:
                years.append(int(string[:4]))
                
        for i in range(len(years)):
            values.append([])
            
        for i in range(len(years)):
            for j in range(len(self.students)):
                if str(years[i]) in str(self.students[j].sid):
                    values[i].append(self.students[j].sid)
                    
        d = dict(zip(years, values))
    
        if years == []:
            keys = []
        else:
            keys = d.get(year)
        
        return keys
                       
        
