from School import *
from Person import *

def main():
    school = School('sajib','CTG')
    
    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)
    
    abul = Student('abir khan',eight)
    school.student_admission(abul)
    babul = Student('abirann khan',eight)
    school.student_admission(babul)
    cabul = Student('abirniiiii khan',eight)
    school.student_admission(cabul)
    
    physics_teacher =Teacher('sajib uddin')
    physics = Subject('physics',physics_teacher)
    eight.add_subject(physics)
    
    chemistry_teacher =Teacher('hossain uddin')
    chemistry = Subject('chemistry',chemistry_teacher)
    eight.add_subject(chemistry)
    
    biology_teacher =Teacher('Aazmal uddin')
    biology = Subject('biology',biology_teacher)
    eight.add_subject(biology)
    
    eight.take_semester_final()

    print(school)
    

if __name__ == '__main__':
    main()
    