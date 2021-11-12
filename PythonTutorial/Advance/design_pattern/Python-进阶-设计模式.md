# 软件设计 原则

那 SOLID 原则是什么呢？它实际上是五个设计原则首字母的缩写，它们分别是：

- 单一职责原则（Single responsibility principle，SRP）
- 开放封闭原则（Open–closed principle，OCP）Liskov
- 替换原则（Liskov substitution principle，LSP）
- 接口隔离原则（Interface segregation principle，ISP）
- 依赖倒置原则（Dependency inversion principle，DIP）

## 单一职责原则

在《敏捷软件开发：原则、实践与模式》中其定义是，“一个模块应该有且仅有一个变化的原因”；而到了《架构整洁之道》中，其定义就变成了“一个模块应该对一类且仅对一类行为者（actor）负责”

单一职责原则这个看起来最简单的原则，实际上也蕴含着很多值得挖掘的内容。要想理解好单一职责原则：

- 我们需要理解封装，知道要把什么样的内容放到一起；
- 我们需要理解分离关注点，知道要把不同的内容拆分开来；
- 我们需要理解变化的来源，知道把不同行为者负责的代码放到不同的地方。

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass
```

Animal违反了SRP，SRP指出，类应该有且只有一个引起变化的原因，在这里，我们看见两个责任，动物数据库管理和动物属性。
这样的设计可能带来什么问题呢？如果应用程序变化会影响到数据库管理功能，使用Animal属性的类不得不重新修改并编译。

为了让这段代码遵守SRP原则，我们创建了另外一个类来处理存储动物到数据库这个功能

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass


class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass

    def save(self, animal: Animal):
        pass
```

## 开放封闭原则

开放封闭原则是这样表述的：软件实体（类、模块、函数）应该对扩展开放，对修改封闭。这个说法是 Bertrand Meyer 在其著作《面向对象软件构造》（Object-Oriented Software
Construction）中提出来的，它给软件设计提出了一个极高的要求：不修改代码。或许你想问，不修改代码，那我怎么实现新的需求呢？答案就是靠扩展。用更通俗的话来解释，就是新需求应该用新代码实现。开放封闭原则向我们描述的是一个结果，就是我们可以不修改代码而仅凭扩展就完成新功能。但是，这个结果的前提是要在软件内部留好扩展点，而这正是需要我们去设计的地方。因为每一个扩展点都是一个需要设计的模型。

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass


animals = [
    Animal('lion'),
    Animal('mouse')
]


def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')

        elif animal.name == 'mouse':
            print('squeak')


animal_sound(animals)
```

animal_sound没有遵守开放封闭原则，因为当一个新的动物类需要添加的时候，会引起这个类的修改。如果我们添加一个新的动物，蛇， 我们必须修改animal_sound 这个方法。
你看见了，对于每个新的动物类而言，一个新的逻辑需要添加到animal_sound里面去。

```python
animals = [
    Animal('lion'),
    Animal('mouse'),
    Animal('snake')
]


def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
        elif animal.name == 'mouse':
            print('squeak')
        elif animal.name == 'snake':
            print('hiss')


animal_sound(animals)
```

我们怎么修改让他能够符合开放封闭原则呢？

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animal_sound(animals)
```

动物现在有一个虚拟方法 make_sound。我们让每一个动物类都实现make_sound方法。 每个动物类都有他自己的实现。现在我们有一个新的动物，animal_sound 不需要改变。

另外一个例子：

```python
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4
```

在这个例子中，如果我们需要添加一个新的折扣类型，新的逻辑需要添加到discount这个类里面 为了让这个例子遵守开放封闭原则，我们这可以用新的类来扩展基类。

```python
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2
```

如果需要给svip用户80%折扣，你可以添加一个新类。

```python
class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2
```

## Liskove替换原则

2008 年，图灵奖授予 Barbara Liskov，表彰她在程序设计语言和系统设计方法方面的卓越工作。她在设计领域影响最深远的就是以她名字命名的 Liskov 替换原则（Liskov substitution principle，简称
LSP）。1988 年，Barbara Liskov 在描述如何定义子类型时写下这样一段话：
> > 这里需要如下替换性质：若每个类型 S 的对象 o1，都存在一个类型 T 的对象 o2，使得在所有针对 T 编程的程序 P 中，用 o1 替换 o2 后，程序 P 行为保持不变，则 S 是 T 的子类型。用通俗的讲法来说，意思就是，子类型（subtype）必须能够替换其父类型（base type）。 在 OOP 世界里，继承算是一个非常特殊的存在，它有点像一把无坚不摧的双刃剑，强大且危险。合理使用继承，可以大大减少类与类之间的重复代码，让程序事半功倍，而不当的继承关系，则会让类与类之间建立起错误的强耦合，带来大片难以理解和维护的代码。

正是因为这样，对继承的态度也可以大致分为两类。大多数人认为，继承和多态、封装等特性一样，属于面向对象编程的几大核心特征之一。而同时有另一部分人觉得，继承带来的 坏处远比好处多。甚至在 Go
这门相对年轻的编程语言里，设计者直接去掉了继承，提倡完全使用组合来替代。

### 一个违反 L 原则的样例

假设我们在为一个 Web 站点设计用户模型。这个站点的用户分为两类：普通用户和站点管理员。所以在代码里，我们定义了两个用户类：普通用户类 User 和管理员类 Admin。

```python
class User(Model):
    """普通用户模型类
    """

    def __init__(self, username: str):
        self.username = username

    def deactivate(self):
        """停用当前用户
        """
        self.is_active = True
        self.save()


class Admin(User):
    """管理员用户类
    """

    def deactivate(self):
        # 管理员用户不允许被停用
        raise RuntimeError('admin can not be deactivated!')
```

因为普通用户的绝大多数操作在管理员上都适用，所以我们把 Admin 类设计成了继承自 User 类的子类。不过在“停用”操作方面，管理员和普通用户之间又有所区别： 普通用户可以被停用，但管理员不行。

于是在 Admin 类里，我们重写了 deactivate 方法，使其抛出一个 RuntimeError 异常，让管理员对象无法被停用。

子类继承父类，然后重写父类的少量行为，这看上去正是类继承的典型用法。但不幸的是，这段代码违反了“里氏替换原则”。具体是怎么回事呢？让我们来看看。

不当继承关系如何违反 L 原则 现在，假设我们需要写一个新函数，它可以同时接受多个用户对象作为参数，批量将它们停用。代码如下：

```python
def deactivate_users(users: Iterable[User]):
    """批量停用多个用户
    """
    for user in users:
        user.deactivate()
```

很明显，上面的代码是有问题的。因为 deactivate_users 函数在参数注解里写到，它接受一切 可被迭代的 User 对象，那么管理员 Admin 是不是 User 对象？当然是，因为它是继承自 User 类的子类。

但是，如果你真的把 [User("foo"), Admin("bar_admin")] 这样的用户列表传到 deactivate_users 函数里，程序立马就会抛出 RuntimeError 异常，因为管理员对象 Admin("
bar_admin") 压根不支持停用操作。

在 deactivate_users 函数看来，子类 Admin 无法随意替换父类 User 使用，所以现在的代码是不符合 L 原则的。

正确的修改办法 既然为函数增加类型判断无法让代码变得更好，那我们就应该从别的方面入手。

“里氏替换原则”提到，子类（Admin）应该可以随意替换它的父类（User），而不破坏程序（deactivate_users）本身的功能。我们试过直接修改类的使用者来遵守这条原则，但是失败了。所以这次，让我们试着从源头上解决问题：重新设计类之间的继承关系。

具体点来说，子类不能只是简单通过抛出异常的方式对某个类方法进行“退化”。如果 “对象不能支持某种操作” 本身就是这个类型的 核心特征 之一，那我们在进行父类设计时，就应该把这个 核心特征 设计进去。

拿用户类型举例，“用户可能无法被停用” 就是 User 类的核心特征之一，所以在设计父类时，我们就应该把它作为类方法（或属性）写进去。

让我们看看调整后的代码：

```python
class User(Model):
    """普通用户模型类
    """

    def __init__(self, username: str):
        self.username = username

    def allow_deactivate(self) -> bool:
        """是否允许被停用
        """
        return True

    def deactivate(self):
        """将当前用户停用
        """
        self.is_active = True
        self.save()


class Admin(User):
    """管理员用户类
    """

    def allow_deactivate(self) -> bool:
        # 管理员用户不允许被停用
        return False


def deactivate_users(users: Iterable[User]):
    """批量停用多个用户
    """
    for user in users:
        if not user.allow_deactivate():
            logger.info(f'user {user.username} does not allow deactivating, skip.')
            continue
        user.deactivate()
```

在新代码里，我们在父类中增加了 allow_deactivate 方法，由它来决定当前的用户类型是否允许被停用。而在 deactivate_users 函数中，也不再需要通过脆弱的类型判断，来判定某类用户是否可以被停用。我们只需要调用
user.allow_deactivate() 方法，程序便能自动跳过那些不支持停用操作的用户对象。

在这样的设计中，User 类的子类 Admin 做到了可以完全替代父类使用，而不会破坏程序 deactivate_users 的功能。

所以我们可以说，修改后的类继承结构是符合里氏替换原则的。

“里氏替换原则”是一个非常具体的原则，它专门为 OOP 里的继承场景服务。当你设计类继承关系，尤其是编写子类代码时，请经常性的问自己这个问题：“如果我把项目里所有使用父类的地方换成这个子类，程序是否还能正常运行？”

如果答案是否定的，那么你就应该考虑调整一下现在的类设计了。调整方式有很多种，有时候你得把大类拆分为更小的类，有时候你得调换类之间的继承关系，有时候你得为父类添加新的方法和属性，就像文章里的第一个场景一样。只要开动脑筋，总会找到合适的办法。

让我们最后再总结一下吧：

- “L：里氏替换原则”认为子类应该可以任意替换父类被使用
- 在类的使用方增加具体的类型判断（isinstance），通常不是最佳解决方案
- 违反里氏替换原则，通常也会导致违反“开放-关闭”原则
- 考虑什么是类的核心特征，然后为父类增加新的方法和属性可以帮到你
- 子类方法应该和父类同名方法返回同一类型，或者返回支持更多操作的子类型也行
- 子类的方法参数应该和父类同名方法完全一致，或者更为宽松

## 接口隔离原则

接口隔离原则（Interface Segregation Principle，ISP）
> 要求程序员尽量将臃肿庞大的接口拆分成更小的和更具体的接口，让接口中只包含客户感兴趣的方法。

2002 年罗伯特·C.马丁给“接口隔离原则”的定义是：客户端不应该被迫依赖于它不使用的方法（Clients should not be forced to depend on methods they do not
use）。该原则还有另外一个定义：一个类对另一个类的依赖应该建立在最小的接口上（The dependency of one class to another one should depend on the smallest
possible interface）。

以上两个定义的含义是:
要为各个类建立它们需要的专用接口，而不要试图去建立一个很庞大的接口供所有依赖它的类去调用。

接口隔离原则和单一职责都是为了提高类的内聚性、降低它们之间的耦合性，体现了封装的思想，但两者是不同的：

- 单一职责原则注重的是职责，而接口隔离原则注重的是对接口依赖的隔离。
- 单一职责原则主要是约束类，它针对的是程序中的实现和细节；接口隔离原则主要约束接口，主要针对抽象和程序整体框架的构建。

### 接口隔离原则的优点

- 接口隔离原则是为了约束接口、降低类对接口的依赖性，遵循接口隔离原则有以下 5 个优点。
- 将臃肿庞大的接口分解为多个粒度小的接口，可以预防外来变更的扩散，提高系统的灵活性和可维护性。
- 接口隔离提高了系统的内聚性，减少了对外交互，降低了系统的耦合性。
- 如果接口的粒度大小定义合理，能够保证系统的稳定性；但是，如果定义过小，则会造成接口数量过多，使设计复杂化；如果定义太大，灵活性降低，无法提供定制服务，给整体项目带来无法预料的风险。
- 使用多个专门的接口还能够体现对象的层次，因为可以通过接口的继承，实现对总接口的定义。
- 能减少项目工程中的代码冗余。过大的大接口里面通常放置许多不用的方法，当实现这个接口的时候，被迫设计冗余的代码。

### 接口隔离原则的实现方法

- 在具体应用接口隔离原则时，应该根据以下几个规则来衡量。
- 接口尽量小，但是要有限度。一个接口只服务于一个子模块或业务逻辑。
- 为依赖接口的类定制服务。只提供调用者需要的方法，屏蔽不需要的方法。
- 了解环境，拒绝盲从。每个项目或产品都有选定的环境因素，环境不同，接口拆分的标准就不同深入了解业务逻辑。
- 提高内聚，减少对外交互。使接口用最少的方法去完成最多的事情。

让我们看一个IShape类

```python
class IShape:
    def draw_square(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError
```

当我们去实现这个借口时候可以用以下方式

```python
class Circle(IShape):
    def draw_circle(self):
        pass


class Square(IShape):
    def draw_square(self):
        pass


class Rectangle(IShape):

    def draw_rectangle(self):
        pass
```

乍一看好像没有什么问题，可是基类IShape设计太胖了，当我们用具体几何图形类继承积累之后，返现有额外的两个借口没有使用。

IShape这个类并没有遵守ISP原则。客户端（这里是是矩形、圆形和方形）不应该被迫依赖他们不需要或不使用的方法。 此外，ISP还指出，接口应该只执行一项工作（就像就像SRP原则一样）任何额外的行为分组都应该被抽象出来到另一个接口上。
在这里，我们的IShape接口执行的动作应该由其他接口独立处理其他接口独立处理的动作。 为了使我们的IShape接口符合ISP原则，我们将这些动作分离到动作到不同的接口。
类（圆形、矩形、方形、三角形......）可以直接继承自IShape接口。 等）可以直接继承自IShape接口，并实现自己的绘制行为。

```python
class IShape:
    def draw(self):
        raise NotImplementedError


class Circle(IShape):
    def draw(self):
        pass


class Square(IShape):
    def draw(self):
        pass


class Rectangle(IShape):
    def draw(self):
        pass
```

## 依赖倒置原则

依赖倒置原则（Dependence Inversion Principle，DIP）是 Object Mentor 公司总裁罗伯特·马丁（Robert C.Martin）于 1996 年在 C++ Report 上发表的文章。

依赖倒置原则的原始定义为：高层模块不应该依赖低层模块，两者都应该依赖其抽象；抽象不应该依赖细节，细节应该依赖抽象（High level modules shouldnot depend upon low level modules.Both
should depend upon abstractions.Abstractions should not depend upon details. Details should depend upon
abstractions）。其核心思想是：要面向接口编程，不要面向实现编程。

依赖倒置原则是实现开闭原则的重要途径之一，它降低了客户与实现模块之间的耦合。

由于在软件设计中，细节具有多变性，而抽象层则相对稳定，因此以抽象为基础搭建起来的架构要比以细节为基础搭建起来的架构要稳定得多。这里的抽象指的是接口或者抽象类，而细节是指具体的实现类。

使用接口或者抽象类的目的是制定好规范和契约，而不去涉及任何具体的操作，把展现细节的任务交给它们的实现类去完成。

### 依赖、倒置原则的作用

依赖倒置原则的主要作用如下。

- 依赖倒置原则可以降低类间的耦合性。
- 依赖倒置原则可以提高系统的稳定性。
- 依赖倒置原则可以减少并行开发引起的风险。
- 依赖倒置原则可以提高代码的可读性和可维护性。

### 依赖倒置原则的实现方法

- 依赖倒置原则的目的是通过要面向接口的编程来降低类间的耦合性，所以我们在实际编程中只要遵循以下4点，就能在项目中满足这个规则。
- 每个类尽量提供接口或抽象类，或者两者都具备。
- 变量的声明类型尽量是接口或者是抽象类。
- 使用继承时尽量遵循里氏替换原则。

## 参考资料：

- https://zhuanlan.zhihu.com/p/89969529
- https://github.com/heykarimoff/solid.python