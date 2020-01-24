from abc import ABCMeta, abstractmethod


class Context:
    def __init__(self):
        self._input = ""
        self._output = 0

        # using property decorator
        # a getter function
        @property
        def Input(self):
            return self._input

        # a setter function
        @Input.setter
        def Input(self, a):
            self._input = a

        @property
        def Output(self):
            return self._input

        # a setter function
        @Output.setter
        def Output(self, a):
            self._input = a


class Expression(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def One():
        ""
    @staticmethod
    @abstractmethod
    def Four():
        ""
    @staticmethod
    @abstractmethod
    def Five():
        ""
    @staticmethod
    @abstractmethod
    def Nine():
        ""
    @staticmethod
    @abstractmethod
    def Multiplier():
        ""

    @staticmethod
    @abstractmethod
    def Interpret(context:Context):
        ""
        
class HundredExpression(Expression):
    def One(self):
        return "C"
    def Four(self):
        return "CD"
    def Five(self):
        return "D"
    def Nine(self):
        return "CM"
    def Multiplier(self):
        return 100

    def Interpret(self, context:Context):
        if context.Input.Length == 0:
            return

        if context.Input.StartsWith(self.Nine()):
            context.Output += (9 * self.Multiplier())
            context.Input = context.Input.Substring(2)
        elif context.Input.StartsWith(self.Four()):
            context.Output += (4 * self.Multiplier())
            context.Input = context.Input.Substring(2)
        elif context.Input.StartsWith(self.Five()):
            context.Output += (5 * self.Multiplier())
            context.Input = context.Input.Substring(1)
        
        while context.Input.StartsWith(self.One()):
            context.Output += (1 * self.Multiplier())
            context.Input = context.Input.Substring(1)

# class OneExpression : Expression
# {
#     public override string One() { return "I"; }
#     public override string Four() { return "IV"; }
#     public override string Five() { return "V"; }
#     public override string Nine() { return "IX"; }
#     public override int Multiplier() { return 1; }
# }

# class TenExpression : Expression
# {
#     public override string One() { return "X"; }
#     public override string Four() { return "XL"; }
#     public override string Five() { return "L"; }
#     public override string Nine() { return "XC"; }
#     public override int Multiplier() { return 10; }
# }

# class ThousandExpression : Expression
# {
#     public override string One() { return "M"; }
#     public override string Four() { return " "; }
#     public override string Five() { return " "; }
#     public override string Nine() { return " "; }
#     public override int Multiplier() { return 1000; }
# }

# class Program
# {
#     static void Main()
#     {
#         string roman = null;

#         while (!string.IsNullOrEmpty(roman = Console.ReadLine()))
#         {
#             Context context = new Context(roman);

#             List<Expression> tree = new List<Expression>();
#             tree.Add(new ThousandExpression());
#             tree.Add(new HundredExpression());
#             tree.Add(new TenExpression());
#             tree.Add(new OneExpression());

#             foreach (Expression exp in tree)
#             {
#                 exp.Interpret(context);
#             }

#             Console.WriteLine("{0} = {1}",
#             roman, context.Output);
#         }

#         Console.ReadKey();
#     }
# }
