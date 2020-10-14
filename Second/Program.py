from Second.Classes import *


# Функция main, в которой создаются экземпляры созданных классов.
def main():
    # Создаем два экземпляра класса Person
    bob = Person("Bob", "bob@gmail.com", "+1235463", 225)
    greg = Person("Greg", "greg@gmail.com", "", 125)

    # Пример работы сеттера.
    # Если номер телефона содержит ненужные элементы, то появится ошибка.
    greg.contacts.phone = "+125125"

    # Поведение экземпляра Person bob
    bob.hello()
    bob.my_salary_interface()

    # Поведение экземпляра Person greg
    greg.hello()
    greg.my_salary_interface()

    # Использование перегруженного стандартного оператора сложения.
    greg2 = greg + bob
    greg2.hello()
    greg2.my_salary_interface()

    # Использование перегруженного стандартного оператора вычитания.
    greg3 = greg - bob
    greg3.hello()
    greg3.my_salary_interface()

    # Создание экземпляра класса Student, производного от Person.
    bob_student = Student("BobS", "s_bob@gmail.com", "123", 1, 100)
    # Поведение экземпляра Student bob_student
    bob_student.hello()
    bob_student.my_salary_interface()
    bob_student.information()

    # Создание экземпляра класса Tutor, производного от Person.
    jack_tutor = Tutor("Jack", "t_jack@gmail.com", "+9981", 10, "ICT")
    # Поведение объекта Tutor jack_tutor
    jack_tutor.hello()
    jack_tutor.my_salary_interface()
    jack_tutor.information()

    # Использование перегруженных операторов в производных классах.
    jack2 = jack_tutor + bob_student
    jack2.hello()
    jack2.my_salary_interface()

    bobs2 = bob_student - jack_tutor
    bobs2.hello()
    bobs2.my_salary_interface()


# Вызов main
if __name__ == "__main__":
    main()
