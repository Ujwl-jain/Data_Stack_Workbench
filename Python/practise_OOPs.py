'''
PYTHON OOP DRILL — BATCH 4
============================================================
13 Topics · 3 Easy + 3 Medium + 3 Hard each = 117 Questions
============================================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 1. OOP BASICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q1.  Create a class `Dog` with attributes name, breed, and age.
     Add a method `bark()` that returns "Woof! My name is {name}."
     Add a method `info()` that returns all attributes as a formatted
     string. Create 3 Dog objects and call both methods on each.

Q2.  Create a class `Rectangle` with attributes width and height.
     Add methods area(), perimeter(), and is_square() (returns bool).
     Create instances with different dimensions and test all methods.

Q3.  Create a class `Student` with attributes name, roll_no, and
     a list of marks. Add methods:
     - average() → returns average of marks
     - highest() → returns highest mark
     - lowest()  → returns lowest mark
     - result()  → returns "Pass" if average >= 40 else "Fail"

[Medium]
Q4.  Create a class `BankAccount` with attributes owner, account_no,
     and balance. Add methods deposit(amount), withdraw(amount),
     and get_statement() that prints all transactions with timestamps.
     Use a list to store transaction history internally.

Q5.  Create a class `Library` that manages a collection of books.
     Each book is a dict with title, author, and available (bool).
     Add methods: add_book(), remove_book(), borrow_book(title),
     return_book(title), and list_available(). Handle cases where
     books don't exist or are already borrowed.

Q6.  Create a class `Inventory` for a shop. Each item has name,
     price, and quantity. Add methods:
     - add_item(name, price, qty)
     - sell_item(name, qty) → reduce stock, raise error if insufficient
     - restock_item(name, qty) → increase stock
     - total_value() → sum of price * qty for all items
     - low_stock_alert(threshold) → return items below threshold qty

[Hard]
Q7.  Design a `Hospital` system with two classes: Doctor and Patient.
     Doctor has name, specialization, and a list of patients.
     Patient has name, age, diagnosis, and assigned doctor.
     Add methods to assign a doctor to a patient, list all patients
     of a doctor, and transfer a patient from one doctor to another.

Q8.  Create a `School` class that manages Students and Teachers.
     - A Student belongs to a class (grade) and has subjects + marks.
     - A Teacher teaches one or more subjects.
     Add methods: enroll_student(), assign_teacher(), get_topper(),
     get_subject_average(subject), and generate_report_card(student).

Q9.  Build a `Casino` card game simulator. Create a `Deck` class with
     52 cards (suits × ranks). Add methods: shuffle() (import random),
     draw_card(), cards_remaining(). Create a `Player` class with name
     and hand (list of cards). Create a `Game` class that deals cards
     to players and determines winner by highest card value.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 2. CONSTRUCTORS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q10. Create a class `Person` with a constructor that accepts name,
     age, and city. Give city a default value of "Unknown".
     Print a message inside __init__ when an object is created.
     Create objects with and without the city argument.

Q11. Create a class `Circle` with a constructor that takes radius.
     Inside __init__, compute and store area and perimeter as
     instance attributes (not as methods). Import math for pi.
     Print all three attributes when creating an object.

Q12. Create a class `Counter` with a constructor that sets count = 0.
     Add methods increment(), decrement(), reset(), and get_count().
     Demonstrate that each object has its own independent counter.

[Medium]
Q13. Create a class `Config` where the constructor accepts **kwargs
     and stores all keyword arguments as instance attributes
     dynamically using setattr(). Add a method show() that prints
     all stored config key-value pairs. Also add a get(key, default)
     method that returns the value or a default if key doesn't exist.

Q14. Create a class `Matrix` with a constructor that accepts a 2D
     list. Validate inside __init__ that all rows have equal length,
     raise ValueError if not. Store rows, cols, and the data.
     Add methods get(row, col), set(row, col, value), and display().

Q15. Create two classes: `Address` (street, city, pincode) and
     `Employee` (name, emp_id, address). The Employee constructor
     should accept an Address object. Demonstrate object composition.
     Add a full_info() method that prints all details including
     the nested address info.

[Hard]
Q16. Create a class `Connection` that simulates a database connection.
     The constructor should accept host, port, and db_name.
     Add a class-level list to track all open connections.
     Add methods connect(), disconnect(), and a class method
     get_all_connections() that returns all currently open ones.
     Ensure disconnect() removes it from the tracking list.

Q17. Create a class `Version` that accepts a version string like
     "3.9.1". Parse it inside __init__ into major, minor, patch
     integers. Add methods is_compatible(other_version) (same major),
     is_newer(other_version) (compare all three parts),
     and bump(part) where part is 'major', 'minor', or 'patch'.

Q18. Create a class `Pipeline` whose constructor accepts a list of
     functions. Add a method run(data) that passes the data through
     each function in sequence (output of one is input to next).
     Add methods add_step(func), remove_step(index), and
     preview(data, steps=None) that shows intermediate results.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 3. DECORATORS (OOP context)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q19. Create a class `Temperature` with a property temp_celsius.
     Use @property to create a getter.
     Use @temp_celsius.setter to validate: raise ValueError if
     temp is below -273.15 (absolute zero).
     Also add a read-only property temp_fahrenheit computed from celsius.

Q20. Create a class `Circle` using @property for radius. In the setter,
     validate that radius > 0. Add read-only properties area and
     diameter that compute from radius. Demonstrate that changing
     radius automatically updates area and diameter.

Q21. Create a class `Employee` with a @property for salary.
     In the setter, ensure salary >= 0 and is a number.
     Add a @property annual_salary that returns salary * 12.
     Add a @property tax() that returns 30% of annual_salary if
     annual_salary > 500000, else 10%.

[Medium]
Q22. Write a class-level decorator `@log_calls` (as a function outside
     the class) that wraps any method to print the method name,
     arguments passed, and the return value every time it is called.
     Apply it to at least 3 methods in a class.

Q23. Write a decorator `@validate_types(**type_map)` that checks the
     types of arguments passed to a method using the type_map dict.
     Apply it to methods in a class to enforce that name is str,
     age is int, salary is float, etc.

Q24. Create a class `Cache` and write a `@cached_property` decorator
     (implement it yourself, don't use functools). It should compute
     the property value once, store it in the instance dict, and
     return the cached value on subsequent accesses without recomputing.

[Hard]
Q25. Write a `@singleton` class decorator that ensures only one
     instance of a class can ever be created. Any subsequent
     instantiation should return the same existing instance.
     Test it with a DatabaseConnection class.

Q26. Write a `@classproperty` descriptor class that allows a property
     to be accessed on the class itself (not just instances).
     Example: MyClass.count should work like a property but at class
     level. Use it to track how many instances have been created.

Q27. Build a full `@retry` decorator for class methods that retries
     the method on failure up to n times, with a configurable delay
     between attempts. Log each retry attempt with the attempt number.
     Apply it to a method that randomly raises an exception.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 4. GETTERS AND SETTERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q28. Create a class `Person` with private attributes _name and _age.
     Write manual getter and setter methods (get_name, set_name,
     get_age, set_age). In set_age, validate age is between 0-150.
     In set_name, validate it is a non-empty string.

Q29. Create a class `Product` with private _price and _discount.
     Use @property and setter for both. Validate price > 0 and
     0 <= discount <= 100. Add a read-only property final_price
     that computes price after discount.

Q30. Create a class `UserProfile` with private _username, _email,
     and _password. Username must be 3-20 chars, alphanumeric.
     Email must contain '@' and '.'. Password must be >= 8 chars.
     Use @property setters to enforce all validations with clear
     error messages.

[Medium]
Q31. Create a class `Rectangle` where width and height are private.
     Use @property setters that enforce both values are positive
     numbers. Add a property aspect_ratio. Add a method resize(factor)
     that multiplies both dimensions by factor using the setters
     (so validation still runs).

Q32. Create a class `Student` where marks is a private list.
     Write a getter that returns a copy (not the original list,
     to prevent external modification). Write a setter that validates
     every mark is between 0 and 100 before assigning.
     Add a property grade that computes the letter grade from average.

Q33. Create a class `Config` with private settings stored in a dict.
     Use __getattr__ and __setattr__ overrides (dunder methods) to
     intercept all attribute access and modification. Log every get
     and set operation. Prevent setting keys that start with '_'.

[Hard]
Q34. Create a `DataTable` class where columns are defined at
     construction time. Use property-like descriptors (define a
     separate `TypedColumn` descriptor class with __get__ and __set__)
     to enforce column data types. Raise TypeError if wrong type is
     assigned to a column.

Q35. Create a class `ObservableProperty` as a descriptor that, when
     a value is set, calls all registered callback functions with
     (old_value, new_value). Use it in a `FormField` class to trigger
     validation callbacks whenever a field value changes.

Q36. Build a class `FrozenConfig` that allows setting attributes only
     once (at construction). Any attempt to modify an attribute after
     construction raises an AttributeError. Use __setattr__ override.
     Add an unfreeze() context manager that temporarily allows changes.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 5. INHERITANCE (ALL TYPES)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q37. Create a base class `Animal` with attributes name, sound, and
     method speak() that returns "{name} says {sound}".
     Create subclasses Dog, Cat, and Cow that call the parent
     constructor with appropriate sounds. Override speak() in Dog
     to add "and wags tail" at the end.

Q38. Create a class `Shape` with a method area() that returns 0.
     Create subclasses Circle, Rectangle, and Triangle that each
     override area() with correct formulas. Create a list of mixed
     shapes and compute total area using a loop.

Q39. Create a base class `Vehicle` with attributes make, model, year,
     and method info(). Create subclasses Car (add doors attribute)
     and Motorcycle (add has_sidecar attribute). Both should call
     super().__init__() and extend info() with their extra details.

[Medium]
Q40. Demonstrate multilevel inheritance:
     Animal → Mammal → Dog → GuideDog.
     Each level adds one new attribute and one new method.
     Show that GuideDog has access to all methods from all levels.
     Use super() correctly at each level.

Q41. Demonstrate multiple inheritance with the MRO (Method Resolution
     Order). Create classes A, B, C, D where D inherits from B and C,
     both of which inherit from A (Diamond problem).
     Override a method at each level and show which one gets called.
     Print D.__mro__ to show the resolution order.

Q42. Create a real-world multiple inheritance example:
     Class Flyable with method fly().
     Class Swimmable with method swim().
     Class Duck that inherits both and also adds quack().
     Create a list of objects (some Flyable, some Swimmable, some both)
     and use isinstance() and hasattr() to call the right methods.

[Hard]
Q43. Build a class hierarchy for a company payroll system:
     Base class `Employee` (name, emp_id, base_salary).
     Subclasses: FullTimeEmployee (adds bonus), PartTimeEmployee
     (adds hourly_rate and hours_worked), Contractor (adds contract_fee).
     Each has an overridden calculate_pay() method.
     Create a `Payroll` class that takes a list of any Employee type
     and generates a total payroll report.

Q44. Build a plugin system using inheritance. Create a base class
     `Plugin` with abstract-style methods: name(), version(),
     execute(data). Create 3 concrete plugin subclasses:
     UpperCasePlugin, ReversePlugin, WordCountPlugin.
     Create a `PluginManager` class that registers plugins by name
     and runs them in sequence on input data.

Q45. Create a full inheritance chain for a game:
     Entity → Character → Hero → Warrior.
     Entity: x, y position, move(dx, dy).
     Character: health, attack_power, take_damage(dmg), is_alive().
     Hero: name, level, gain_xp(xp), level_up().
     Warrior: weapon, shield_block(), special_attack().
     Each level must call super().__init__() and add meaningful methods.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 6. ACCESS MODIFIERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q46. Create a class `Person` that demonstrates all three access levels:
     - public attribute: name
     - protected attribute: _age
     - private attribute: __ssn
     Show what happens when you try to access each from outside
     the class. Show how to access __ssn using name mangling.

Q47. Create a class `BankAccount` with a private __balance and private
     __pin. Add public methods deposit(), withdraw() (requires correct
     pin), and get_balance() (requires correct pin). Show that direct
     access to __balance fails but the methods work.

Q48. Create a class `Car` with public attributes (make, model),
     a protected attribute _mileage, and a private attribute __vin.
     Create a subclass `ElectricCar` and show which attributes
     it can and cannot access directly. Access _mileage from the
     subclass and show the name mangling for __vin.

[Medium]
Q49. Create a class `Database` with a private __connection_string and
     private __query_history list. Public methods: connect(), execute(sql),
     get_history(). Protected method _validate_sql(sql). Show that
     __query_history can only be accessed through get_history() and
     not directly. Demonstrate name mangling to show it still exists.

Q50. Create a class `Employee` with private __salary and __performance.
     Add a protected method _calculate_bonus() that is meant to be
     used by subclasses. Create a subclass `Manager` that calls
     _calculate_bonus() but also has its own private __team_size.
     Show which attributes are accessible from where.

Q51. Write a class `SecureForm` that stores private field values in
     a __data dict. Use __getattr__ to allow attribute-style access
     but log a warning for any access to protected or private fields
     attempted from outside. Add a method to list all field names
     without exposing their values.

[Hard]
Q52. Simulate a real access control pattern: create a class `AdminPanel`
     with private __admin_commands list and protected _logs list.
     Public users can only call view_dashboard(). A protected method
     _run_report() is available to subclasses. Private __delete_all()
     is only callable from inside the class. Create a subclass
     `SuperAdmin` that accesses _run_report() and attempts name mangling
     to call __delete_all(). Show and explain the behavior.

Q53. Create a class `APIClient` where the API key is stored as a
     private attribute. Write a method that uses the key internally
     without ever exposing it. Override __repr__ and __str__ to ensure
     the key never appears in string representations.
     Add a method rotate_key(new_key) with password confirmation.

Q54. Build a class `ImmutableRecord` that uses __slots__ and private
     attributes to create a record whose fields can only be set once
     (at construction). Use __setattr__ to enforce this. Show how
     __slots__ prevents adding arbitrary new attributes.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 7. STATIC METHODS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q55. Create a class `MathUtils` with only @staticmethod methods:
     - is_prime(n) → bool
     - factorial(n) → int
     - gcd(a, b) → int
     - lcm(a, b) → int
     Call each method on the class directly (without instantiation).

Q56. Create a class `StringUtils` with @staticmethod methods:
     - is_palindrome(s) → bool
     - word_count(s) → int
     - reverse_words(s) → str
     - capitalize_words(s) → str
     Show that these don't need self or cls to work.

Q57. Create a class `DateUtils` with @staticmethod methods:
     - is_leap_year(year) → bool
     - days_in_month(month, year) → int
     - is_valid_date(day, month, year) → bool
     Import calendar module. Call directly on class and on an instance.

[Medium]
Q58. Create a class `TemperatureConverter` with @staticmethod methods
     for all conversions: celsius_to_fahrenheit, fahrenheit_to_celsius,
     celsius_to_kelvin, kelvin_to_celsius, fahrenheit_to_kelvin,
     kelvin_to_fahrenheit. Add a static method convert(value, from_unit,
     to_unit) that routes to the correct conversion.

Q59. Create a class `Validator` with @staticmethod methods:
     - is_valid_email(email) → bool
     - is_valid_phone(phone) → bool (10 digits, starts with 6-9)
     - is_valid_pan(pan) → bool (format: ABCDE1234F)
     - is_valid_pincode(pin) → bool (6 digits)
     Use string methods (no regex). Call them inside an instance method
     validate_user(data_dict) to validate a user's full profile.

Q60. Create a `UnitConverter` class with static methods for:
     length (km↔miles, m↔feet), weight (kg↔lbs), volume (L↔gallons).
     Add a static method batch_convert(values, from_unit, to_unit) that
     applies conversion to a list using map() and a lambda.

[Hard]
Q61. Create a class `DataProcessor` where static methods handle
     pure transformations: normalize(data) (scale to 0-1),
     standardize(data) (z-score), flatten(nested_list),
     chunk(lst, size). Instance methods use these static methods
     internally in a process(data, steps) pipeline. Show the
     separation of stateless utility logic from stateful instance logic.

Q62. Design a `Factory` class with a static method create(type, **kwargs)
     that returns instances of different subclasses based on the type
     string. Example: Factory.create('circle', radius=5) returns a
     Circle object. This is the Factory Design Pattern using static methods.

Q63. Create a `Registry` class with a private class-level dict and
     a @staticmethod register(name, cls) that adds a class to the
     registry. A @staticmethod get(name) retrieves the class.
     Use this to build a plugin registry where plugins register
     themselves at import time using the registry.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 8. INSTANCE AND CLASS VARIABLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q64. Create a class `Employee` with a class variable company_name and
     instance variables name and salary. Show that all instances share
     company_name but have their own name and salary. Then change
     company_name on one instance and show the difference between
     changing it on the class vs on the instance.

Q65. Create a class `Counter` with a class variable count = 0.
     Increment count in __init__ every time a new object is created.
     Decrement it in __del__ when an object is destroyed.
     Add a class method get_count() to retrieve it.
     Create and delete objects, verifying the count updates correctly.

Q66. Create a class `Student` with a class variable school = "ABC School"
     and instance variables name and grade. Show:
     - all students share the same school
     - changing Student.school affects all instances
     - assigning school on one instance only shadows it for that instance
     Print clearly to demonstrate each case.

[Medium]
Q67. Create a class `Product` with class variables: total_products = 0,
     all_prices = []. Each new instance adds to both. Add class methods
     average_price() and most_expensive() that operate on the class-level
     data. Show how class variables serve as shared state across instances.

Q68. Create a class `Config` where class variables hold default settings.
     Instance variables hold per-instance overrides. Write a method
     get_setting(key) that checks instance overrides first, falls back
     to class defaults. Write a class method update_default(key, value)
     to change the class-level default for all instances.

Q69. Create a class hierarchy where a class variable is defined in the
     base class `Animal`. Subclasses `Dog` and `Cat` each override it.
     Show how each subclass has its own version while Animal's original
     remains. Also show that an instance variable with the same name
     shadows the class variable for that instance only.

[Hard]
Q70. Build a `ConnectionPool` class that uses class variables to
     maintain a pool of reusable connection objects. Class variable
     max_connections limits the pool size. When all connections are
     in use, requesting a new one should wait (simulate with a counter).
     Use class methods to acquire() and release() connections.

Q71. Create a class `Borg` (Borg pattern — alternative to Singleton)
     where all instances share the same state using a shared class-level
     __dict__. Any attribute change on one instance is immediately
     visible on all others. Demonstrate with 3 instances modifying
     different attributes and showing all three see every change.

Q72. Design a class `AuditLog` using class variables to maintain a
     shared audit trail across all instances. Every time any instance
     calls any method, it's logged to the class-level log with:
     timestamp, instance id, method name, arguments.
     Write a class method get_audit_trail() and clear_log().


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 9. CLASS METHODS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q73. Create a class `Date` with attributes day, month, year.
     Add a @classmethod from_string(cls, date_str) that parses a
     "DD-MM-YYYY" string and returns a Date object.
     Add another @classmethod today(cls) that uses datetime.date.today()
     to return today's date as a Date object.

Q74. Create a class `Temperature` with a value in Celsius.
     Add classmethods: from_fahrenheit(cls, f), from_kelvin(cls, k)
     that each return a Temperature object converted to Celsius.
     Show all three ways to create a Temperature object.

Q75. Create a class `Person` with name and age. Add a classmethod
     from_dict(cls, data) that accepts a dict {'name':..., 'age':...}
     and returns a Person object. Add from_csv_line(cls, line) that
     parses "Alice,30" and returns a Person. Test both constructors.

[Medium]
Q76. Create a class `FileProcessor` with a class variable supported_formats.
     Add a @classmethod register_format(cls, fmt) that adds a new format.
     Add a @classmethod can_process(cls, filename) that checks if the
     file extension is supported.
     Add a @classmethod from_file(cls, filepath) that reads file content
     and returns a FileProcessor instance.

Q77. Create a base class `Animal` with a classmethod create(cls, name)
     that returns an instance of cls (not Animal). Inherit Dog and Cat
     from Animal. Show that Animal.create('buddy') returns an Animal,
     but Dog.create('rex') returns a Dog. This demonstrates how
     classmethods work with inheritance.

Q78. Build a class `QueryBuilder` where class methods are used to
     create pre-configured instances: QueryBuilder.select_all(table),
     QueryBuilder.insert(table), QueryBuilder.update(table).
     Each classmethod sets up the instance appropriately and returns it.
     Instance methods add_condition(col, val) and build() complete
     the SQL string.

[Hard]
Q79. Create a class `DataPipeline` with a class-level registry of
     named pipelines stored as a class variable. Add a classmethod
     register(cls, name, steps) that saves a pipeline config.
     Add a classmethod run(cls, name, data) that retrieves and
     executes a named pipeline. Add list_pipelines() classmethod.

Q80. Create a `Multiton` pattern: like Singleton but allows one instance
     per key. Use a class variable dict to store instances by key.
     Implement via @classmethod get_instance(cls, key). Demonstrate
     with a LocaleFormatter class where each locale ('en', 'hi', 'fr')
     gets exactly one shared instance.

Q81. Build a full `ORM-like` class `Model` where classmethod find(cls,
     **filters) searches a class-level "database" (list of dicts),
     classmethod create(cls, **data) adds a record, classmethod
     delete(cls, id) removes one, and classmethod all(cls) returns all.
     Subclass it with UserModel and ProductModel, each with their own
     class-level storage.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 10. SUPER KEYWORD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q82. Create a class `Animal` with __init__(name, sound) and speak().
     Create `Dog` that calls super().__init__ and adds a breed param.
     Override speak() and use super().speak() inside it, then append
     extra dog behavior. Show clearly what super() provides at each step.

Q83. Create a class `Shape` with __init__(color) and describe().
     Create `Rectangle(Shape)` with __init__(color, width, height) using
     super(). Create `ColoredRectangle(Rectangle)` adding a border_color.
     Each describe() calls super().describe() and adds its own details.
     Trace the output to show the chain.

Q84. Create classes `A`, `B(A)`, `C(A)`, `D(B, C)` where each __init__
     prints which class is initializing. Use super().__init__() in each.
     Create a D object and observe the MRO-based initialization order.
     Then print D.__mro__ to confirm it.

[Medium]
Q85. Create a `Vehicle` → `Car` → `ElectricCar` hierarchy.
     Each __init__ adds new parameters. Each class also has a method
     describe() that calls super().describe() and adds its own line.
     Add a method start() at Vehicle level. Override start() in
     ElectricCar to call super().start() and add "silently" at the end.

Q86. Create a `LoggedList` class that inherits from Python's built-in
     list. Use super() to call the original list methods but add logging
     before/after each operation. Override append(), remove(), and pop().
     Each override logs: "Operation: append, Value: x, Size before: n".

Q87. Create a mixin pattern: WriteLogMixin and ReadLogMixin each add
     logging behavior. Create a class DataStore(WriteLogMixin,
     ReadLogMixin, dict) that uses super() correctly in a cooperative
     multiple inheritance chain. Show that all mixins in the MRO are
     called in the right order.

[Hard]
Q88. Build a deep inheritance chain with super():
     Logger → TimestampLogger → FileLogger → RotatingFileLogger.
     Each level overrides log(message) and calls super().log() to chain
     behavior. RotatingFileLogger should also track log count and
     "rotate" (clear) after every 5 logs. Trace the call through all
     4 levels for a single log() call.

Q89. Create a `Validator` base class with validate(data) → bool.
     Create mixins: RangeValidator, TypeValidator, RequiredValidator.
     Create a `FormField` class that inherits from all three and uses
     super().validate(data) in each mixin so all validations run in
     MRO order. A value must pass ALL validators to return True.

Q90. Build a `Component` system (like React) with super():
     BaseComponent → StyledComponent → AnimatedComponent → ModalComponent.
     Each layer adds render() behavior using super().render().
     The final ModalComponent.render() should output a combined string
     that shows contributions from all layers:
     "base_content + styles + animation + modal_wrapper".


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 11. DUNDER METHODS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q91. Create a class `Book` and implement:
     __init__(title, author, pages)
     __str__ → "Title by Author (N pages)"
     __repr__ → "Book('Title', 'Author', N)"
     __len__ → returns number of pages
     Test each by printing the object, using repr(), and len().

Q92. Create a class `Point` with x and y coordinates. Implement:
     __str__ → "(x, y)"
     __repr__ → "Point(x, y)"
     __eq__ → True if both x and y are equal
     __hash__ → so Points can be used in sets and as dict keys
     Test by putting Point objects in a set and dict.

Q93. Create a class `ShoppingCart` and implement:
     __init__ → empty list of items
     __len__ → number of items in cart
     __contains__ → supports "item in cart"
     __iter__ → allows for-loop over cart items
     __getitem__ → allows cart[index] access
     Add method add_item(item) and test all dunder behaviors.

[Medium]
Q94. Create a class `Matrix` and implement:
     __add__ → matrix addition (element-wise)
     __sub__ → matrix subtraction (element-wise)
     __mul__ → scalar multiplication (Matrix * number)
     __eq__  → True if all elements match
     __str__ → nicely formatted grid
     Test all operations with 2x2 and 3x3 matrices.

Q95. Create a class `WordCollection` and implement:
     __init__(words: list)
     __add__ → combines two collections (union, no duplicates)
     __sub__ → removes words of second collection from first
     __and__ → intersection of two collections
     __or__  → union of two collections
     __len__, __iter__, __contains__, __str__
     Test all operators with meaningful word sets.

Q96. Create a class `ChainableQuery` that implements:
     __init__(data: list of dicts)
     __getitem__ → filter by index or slice
     __call__ → filter by a condition function
     __iter__ → iterate over current data
     __len__ → current record count
     __str__ → table-like string of records
     Chain operations: query(lambda x: x['age']>18)[0:5]

[Hard]
Q97. Create a class `LazyList` that implements the iterator protocol
     (__iter__ and __next__) from scratch. It should compute elements
     on demand (lazily) using a generator function passed at creation.
     Implement __getitem__ using islice for slicing support.
     Implement __len__ by materializing the iterator (with a warning).

Q98. Create a `Descriptor` class that implements __get__, __set__, and
     __delete__. Use it to create typed attributes on any class:
     e.g. TypedAttr(int) ensures only ints can be set. Apply multiple
     descriptors to a single class and show how they each manage their
     own storage in the instance's __dict__.

Q99. Create a class `FrozenDict` that behaves exactly like a dict but
     is immutable after creation. Implement:
     __init__ → populate from a regular dict
     __getitem__, __iter__, __len__, __contains__, __str__, __repr__
     __setitem__, __delitem__ → raise TypeError
     __hash__ → make it hashable so it can be a dict key or in a set
     Test all behaviors thoroughly.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 12. METHOD OVERRIDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q100. Create a class `Animal` with methods: speak(), eat(), sleep().
      Each returns a generic string. Create subclasses Dog, Cat, Bird
      that each override all three methods with animal-specific behavior.
      Create a list of mixed animals and call all methods on each.

Q101. Create a class `Employee` with method calculate_pay() that
      returns base_salary. Override it in:
      - Manager: base_salary + bonus
      - Intern: base_salary * 0.5
      - Contractor: hourly_rate * hours
      Create a list of all types and print the payslip for each.

Q102. Create a class `Notification` with method send(message) that
      just prints to console. Override it in:
      - EmailNotification: prints "Email sent: {message}"
      - SMSNotification: prints "SMS sent (160 char limit): {message[:160]}"
      - PushNotification: prints "Push: {message}"
      Create a list of all types and call send() on each.

[Medium]
Q103. Create a base class `Sorter` with a method sort(lst) that returns
      the list sorted using Python's built-in sorted(). Override it in:
      - BubbleSorter: implement bubble sort manually
      - MergeSorter: implement merge sort manually
      - QuickSorter: implement quick sort manually
      Create each, sort the same list, and verify all produce same output.

Q104. Create a class `DataExporter` with method export(data) that
      returns a string. Override in:
      - CSVExporter: format data as CSV rows
      - JSONExporter: format data as JSON string (import json)
      - MarkdownExporter: format as a Markdown table
      Use the same list-of-dicts data and export it in all three formats.

Q105. Create a class `Game` with methods: start(), play_turn(), end().
      Override all three in subclasses NumberGuessingGame and WordGame.
      Each game has different logic but follows the same interface.
      Create a `GameEngine` class that accepts any Game object and calls
      start(), multiple play_turn(), then end() — without knowing the type.

[Hard]
Q106. Create a `Parser` base class with method parse(text) → list.
      Override in:
      - CSVParser: splits by comma, handles quoted fields
      - JSONParser: uses json.loads() with error handling
      - FixedWidthParser: accepts column widths, slices each row
      Create a `DataIngestion` class that accepts any Parser type.
      This is the Strategy Design Pattern via method overriding.

Q107. Build a `Renderer` hierarchy:
      Base: render(content) → returns raw content unchanged.
      HTMLRenderer: wraps in <html><body> tags.
      MarkdownRenderer: converts **bold** to <b> and # to <h1>.
      Each overrides render() and optionally calls super().render()
      to process the content through the chain.
      Chain HTMLRenderer(MarkdownRenderer()) and test.

Q108. Create a class `Collection` with methods:
      add(item), remove(item), contains(item), size(), to_list().
      Override all in:
      - SortedCollection: always maintains sorted order on add
      - UniqueCollection: rejects duplicate items on add
      - BoundedCollection(max_size): rejects items when full
      - PriorityCollection: items are (priority, value) tuples, always
        pops highest priority first
      Test each with the same sequence of operations.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 13. OPERATOR OVERLOADING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q109. Create a class `Vector2D` with x and y. Overload:
      + (__add__) → adds two vectors
      - (__sub__) → subtracts two vectors
      * (__mul__) → scalar multiplication (Vector * number)
      == (__eq__) → True if x and y both equal
      str (__str__) → "(x, y)"
      Test all operations.

Q110. Create a class `Fraction` with numerator and denominator.
      Simplify in __init__ using GCD. Overload:
      + → fraction addition
      - → fraction subtraction
      * → fraction multiplication
      / → fraction division (__truediv__)
      == → equality after simplification
      str → "numerator/denominator"

Q111. Create a class `Money` with amount and currency.
      Overload + and - (raise error if currencies differ).
      Overload * for scalar multiplication (Money * 1.5).
      Overload > and < for comparison (__gt__, __lt__).
      Overload == for equality. str → "₹1200.00" style formatting.

[Medium]
Q112. Create a class `Matrix` and overload:
      + → matrix addition
      - → matrix subtraction
      * → supports both Matrix*Matrix (dot product for 2x2)
           and Matrix*scalar
      ** → element-wise power (__pow__)
      == → element-wise equality
      [] → __getitem__ for row access: matrix[0] returns first row
      Implement and test all with 2x2 matrices.

Q113. Create a class `Interval` representing a range [start, end].
      Overload:
      + → merge two overlapping intervals into one (raise error if no overlap)
      & → (__and__) intersection of two intervals
      in → (__contains__) check if a number is in the interval
      < > == → comparison by start point
      str → "[start, end]"
      len → (__len__) end - start (length of interval)

Q114. Create a class `Polynomial` storing coefficients as a list
      (index = power). Example: [1, 2, 3] = 1 + 2x + 3x².
      Overload:
      + → polynomial addition
      * → polynomial multiplication
      __call__ → evaluate at x: poly(2) computes the value at x=2
      str → "1 + 2x + 3x^2" formatted nicely
      == → same coefficients
      len → degree of polynomial

[Hard]
Q115. Create a class `BigInt` that stores a very large integer as a
      list of digits (to simulate arbitrary precision). Overload:
      + → addition with carry
      * → multiplication
      == and < and > → comparison
      str → the full number as a string
      int → (__int__) convert back to Python int
      Test with numbers larger than 10^20.

Q116. Create a class `Set` from scratch (without using Python's set).
      Store elements in a list internally. Overload all set operators:
      | (__or__) → union
      & (__and__) → intersection
      - (__sub__) → difference
      ^ (__xor__) → symmetric difference
      <= (__le__) → issubset
      >= (__ge__) → issuperset
      == → equality
      in (__contains__), len, iter, str

Q117. Build a class `DataFrame` (mini pandas-like) with columns and
      rows stored as a dict of lists. Overload:
      [] (__getitem__) → column access by name, or row by int index
      + → concatenate two DataFrames (append rows)
      == → element-wise equality returning a bool DataFrame
      len → number of rows
      iter → iterate over rows as dicts
      str → nicely formatted table
      Add a filter(col, func) method using the overloaded [] internally.


============================================================
 SUMMARY — BATCH 4 (OOP)
============================================================
Total Questions   : 117
Easy per topic    : 3    (39 total)
Medium per topic  : 3    (39 total)
Hard per topic    : 3    (39 total)

Topics Covered:
  1.  OOP Basics
  2.  Constructors
  3.  Decorators (OOP context)
  4.  Getters and Setters
  5.  Inheritance (all types)
  6.  Access Modifiers
  7.  Static Methods
  8.  Instance and Class Variables
  9.  Class Methods
  10. Super Keyword
  11. Dunder Methods
  12. Method Overriding
  13. Operator Overloading
============================================================
'''
