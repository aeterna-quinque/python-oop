from Second.Classes import *


def main():
    bob = Person("Bob", "bob@gmail.com", "+1235463", 225)
    greg = Person("Greg", "greg@gmail.com", "", 125)
    '''
    greg.contacts.phone = "+125125"

    bob.hello()
    bob.my_salary_interface()

    greg.hello()
    greg.my_salary_interface()

    greg2 = greg + bob
    greg2.hello()
    greg2.my_salary_interface()

    greg3 = greg - bob
    greg3.hello()
    greg3.my_salary_interface()
    '''
    bob_student = Student("Bob", "s_bob@gmail.com", "123", 1, 100)
    bob_student.hello()
    bob_student.my_salary_interface()
    bob_student.information()

    jack_tutor = Tutor("Jack", "t_jack@gmail.com", "+9981", 10, "ICT")
    jack_tutor.hello()
    jack_tutor.my_salary_interface()
    jack_tutor.information()

    jack2 = jack_tutor + bob_student
    jack2.hello()
    jack2.my_salary_interface()

    bobs2 = bob_student - jack_tutor
    bobs2.hello()
    bobs2.my_salary_interface()


if __name__ == "__main__":
    main()
