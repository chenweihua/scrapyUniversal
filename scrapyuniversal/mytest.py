#1 类也是对象class ObjectCreator(object):       pass#类也是一种对象，当使用class关键字时，python解释器会创建一个对象，这个特殊的对象拥有创建对象的能力，所以它是一个类print(ObjectCreator)def echo(o):    print(o)#可以将类作为参数传给函数echo(ObjectCreator)#可以为类增加属性print(hasattr(ObjectCreator,'new_attribute'))ObjectCreator.new_attribute = 'foo'print(hasattr(ObjectCreator,'new_attribute'))#可以将类赋值给变量ObjectCreatorMirror = ObjectCreatorprint(ObjectCreatorMirror)# 2 动态的创建类#类也是对象，你可以在运行时使用关键字class动态的创建类def choose_class(name):    if name == 'Foo':        class Foo():            pass        return Foo #返回的是类,不是类的实例MyClass = choose_class('Foo')print(MyClass)print(MyClass())#可以通过这个类创建实例#查看类的类型print(type(MyClass))print(type(MyClass()))#此处返回的为何不是一个类的实例，输出的结果为何和print(MyClass)一样print(type(ObjectCreator))#可以发现类的类型都是'type',此处的type()可以接受一个类的描述作为参数，然后动态的创建并返回一个类print(ObjectCreator())#使用type动态创建类对象，注意这里的类对象和类实例不是一个意思#type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)可以替代传统的定义一个类方式MyShinyClass = type('MyShinyClass',(),{})print(MyShinyClass)print(MyShinyClass())print(type(MyShinyClass()))print('Test 2')# class Too(object):#     bar = True# 以上的代码可以这样写Too = type('Too',(),{'bar':True})FooChild = type('Foochild',(Too,),{})print(FooChild)print(FooChild.bar)# 3 所有这一切都是通过元类来实现的，那到底什么是元类# 元类就是用来创建类对象的类，也就是类的类(和二级指针概念差不多)# 可以用如下代码理解#MyClass = MetaClass()#MyObject = MyClass()# 函数type实际上是一个元类。type就是Python在背后用来创建所有类的元类.Python中所有的东西，# 注意，我是指所有的东西——都是对象。这包括整数、字符串、函数以及类。它们全部都是对象，而且它们都是从一个类创建而来。print('Test 3')age = 35print(age.__class__)name = 'bob'print(name.__class__)def foo():passprint(foo.__class__)class Bar(object):passb = Bar()print(b.__class__)# 现在，对于任何一个__class__的__class__属性又是什么呢？print('Test 4')print(age.__class__.__class__)print(name.__class__.__class__)print(foo.__class__.__class__)print(b.__class__.__class__)# 因此，元类就是创建类这种对象的东西。如果你喜欢的话，可以把元类称为“类工厂”（不要和工厂类搞混了:D） type就是Python的内建元类，当然了，你也可以创建自己的元类。# 4 自定义元类class Upper(type):    def __new__(cls, name, bases, dct):        #定义创建类对象时的行为，注意是类对象而不是类的实例        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))        uppercase_attr = dict((name.upper(), value) for name, value in attrs)        return type.__new__(cls, name, bases, uppercase_attr)#----------------------------------class Foo2(metaclass=Upper):    bar = 'mary'print('Test 5')print(hasattr(Foo2,'bar'))print(hasattr(Foo2,'BAR'))