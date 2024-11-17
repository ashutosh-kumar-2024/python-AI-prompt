from .a import A
from .b import B

class C:
    def function_c(self):
        a_instance = A()
        b_instance = B()
        result_a = a_instance.function_a()
        result_b = b_instance.function_b()
        return f"Function C combines: {result_a} + {result_b}"
