<<<<<<< HEAD
DOLLAR_CURRENCY = 79.2
EURO_CURRENCY = 92.93


# Класс Person.
class Person:
    # Инкапсулированные свойства класса.
    __name: str
    __salary: int

    # Конструктор класа Person.
    # Аттрибуту salary присваивается значение по умолчанию в случае осутствия значения для него.
    def __init__(self, name, email, phone, salary=0):
        self.__name = name
        self.__salary = salary
        # Для каждого экземпляра класса Person создается экземпляра класса Contacts.
        # Это реализация композиции.
        self.contacts = Contacts(email, phone)

    # Геттеры и сеттеры для имени и зарплаты.
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            raise ValueError("Wrong salary.")

    # Перегрузка стандартных операторов сложения и вычитания.
    def __add__(self, other):
        return Person(f"{self.name}+{other.name}", self.contacts.email,
                      self.contacts.phone, self.__salary + other.salary)

    def __sub__(self, other):
        salary = self.salary - other.salary
        if salary < 0:
            salary = 0
        return Person(f"{self.name}-{other.name}", self.contacts.email,
                      self.contacts.phone, salary)

    # Методы, определяющие поведение.
    def hello(self):
        text = f"Hello!\nMy name is {self.name}.\nNice to meet you!\n"
        print(text)

    def __my_salary(self, cur):
        currency = {'dollar': DOLLAR_CURRENCY, 'euro': EURO_CURRENCY, 'rouble': 1}
        if str.lower(cur) in currency:
            salary = self.salary / currency[cur]
        else:
            salary = -1
        return salary

    def my_salary_interface(self):
        cur = input("What currency do you prefer: dollar, euro or rouble? ")
        salary = self.__my_salary(cur)
        if salary == -1:
            text = f"My salary in roubles is {self.salary}\n"
        else:
            text = f"Well, my salary in {cur}s is {salary:.2f}\n"
        print(text)


# Класс Contacts, реализующий отношение композиции.
class Contacts:
    # Инкапсулированные свойства.
    __email: str
    __phone: str

    def __init__(self, email, phone):
        self.__email = email
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if str.isdigit(value[1:]) and (value[0] == "+" or str.isdigit(value[0])):
            self.__phone = value
        else:
            raise ValueError("Wrong phone number.")


# Класс Student, производный от класса Person.
class Student(Person):
    # Инкапсулированные свойства.
    __year: int
    __degree: str
    __uni: str

    # Конструктор класса. Для salary, degree и uni установлены значения по умолчанию.
    def __init__(self, name, email, phone, year, salary=0, degree="bachelor", uni="ITMO"):
        super().__init__(name, email, phone, salary)
        self.__year = year
        self.__degree = degree
        self.__uni = uni

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value in range(1, 6):
            self.__year = value
        else:
            raise ValueError("Wrong year.")

    @property
    def degree(self):
        return self.__degree

    @degree.setter
    def degree(self, value):
        degrees = ["bachelor", "master", "doctor"]
        if value in degrees:
            self.__degree = value
        else:
            raise ValueError("Wrong degree.")

    @property
    def uni(self):
        return self.__uni

    @uni.setter
    def uni(self, value):
        self.__uni = value

    # Метод, характерный для данного класса и отсутствующий в базовом классе.
    def information(self):
        text = f"I am {self.year} year {self.degree} student at {self.uni} University.\n"
        print(text)


# Класс Tutor, производный от класса Person.
class Tutor(Person):
    # Инкапсулированные свойства.
    __exp: int
    __spec: str
    __uni: str

    # Конструктор класса. Для salary и uni установлены значения по умолчанию.
    def __init__(self, name, email, phone, exp, spec, salary=20000, uni="ITMO"):
        super().__init__(name, email, phone, salary)
        self.__exp = exp
        self.__spec = spec
        self.__uni = uni

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, value):
        if value >= 0:
            self.__exp = value
        else:
            raise ValueError("Wrong experience.")

    @property
    def spec(self):
        return self.__spec

    @spec.setter
    def spec(self, value):
        self.__spec = value

    @property
    def uni(self):
        return self.__uni

    @uni.setter
    def uni(self, value):
        self.__uni = value

    # Метод, характерный для данного класса и отсутствующий в базовом классе.
    def information(self):
        text = f"I am tutor  at {self.uni} University.\n" \
               f"My specialization is {self.spec}.\n" \
               f"I've been working here for {self.exp} years already.\n"
        print(text)
=======
DOLLAR_CURRENCY = 79.2
EURO_CURRENCY = 92.93


class Person:
    __name: str
    __salary: int

    def __init__(self, name, email, phone, salary=0):
        self.__name = name
        self.__salary = salary
        self.contacts = Contacts(email, phone)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            raise ValueError("Wrong salary.")

    def __add__(self, other):
        return Person(f"{self.name}+{other.name}", self.contacts.email,
                      self.contacts.phone, self.__salary + other.salary)

    def __sub__(self, other):
        salary = self.salary - other.salary
        if salary < 0:
            salary = 0
        return Person(f"{self.name}-{other.name}", self.contacts.email,
                      self.contacts.phone, salary)

    def hello(self):
        text = f"Hello!\nMy name is {self.name}.\nNice to meet you!\n"
        print(text)

    def __my_salary(self, cur):
        currency = {'dollar': DOLLAR_CURRENCY, 'euro': EURO_CURRENCY, 'rouble': 1}
        if str.lower(cur) in currency:
            salary = self.salary / currency[cur]
        else:
            salary = -1
        return salary

    def my_salary_interface(self):
        cur = input("What currency do you prefer: dollar, euro or rouble? ")
        salary = self.__my_salary(cur)
        if salary == -1:
            text = f"My salary in roubles is {self.salary}\n"
        else:
            text = f"Well, my salary in {cur}s is {salary:.2f}\n"
        print(text)


class Contacts:
    __email: str
    __phone: str

    def __init__(self, email, phone):
        self.__email = email
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if str.isdigit(value[1:]) and (value[0] == "+" or str.isdigit(value[0])):
            self.__phone = value
        else:
            raise ValueError("Wrong phone number.")


class Student(Person):
    __year: int
    __degree: str
    __uni: str

    def __init__(self, name, email, phone, year, salary=0, degree="bachelor", uni="ITMO"):
        super().__init__(name, email, phone, salary)
        self.__year = year
        self.__degree = degree
        self.__uni = uni

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value in range(1, 6):
            self.__year = value
        else:
            raise ValueError("Wrong year.")

    @property
    def degree(self):
        return self.__degree

    @degree.setter
    def degree(self, value):
        degrees = ["bachelor", "master", "doctor"]
        if value in degrees:
            self.__degree = value
        else:
            raise ValueError("Wrong degree.")

    @property
    def uni(self):
        return self.__uni

    @uni.setter
    def uni(self, value):
        self.__uni = value

    def information(self):
        text = f"I am {self.year} year {self.degree} student at {self.uni} University.\n"
        print(text)


class Tutor(Person):
    __exp: int
    __spec: str
    __uni: str

    def __init__(self, name, email, phone, exp, spec, salary=20000, uni="ITMO"):
        super().__init__(name, email, phone, salary)
        self.__exp = exp
        self.__spec = spec
        self.__uni = uni

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, value):
        if value >= 0:
            self.__exp = value
        else:
            raise ValueError("Wrong experience.")

    @property
    def spec(self):
        return self.__spec

    @spec.setter
    def spec(self, value):
        self.__spec = value

    @property
    def uni(self):
        return self.__uni

    @uni.setter
    def uni(self, value):
        self.__uni = value

    def information(self):
        text = f"I am tutor  at {self.uni} University.\n" \
               f"My specialization is {self.spec}.\n" \
               f"I've been working here for {self.exp} years already.\n"
        print(text)

>>>>>>> 363667d4eb33893966e0d4dc13bd255876e8125e
