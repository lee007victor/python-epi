class TestClassVariable:
    cls_var = 2
    cls_list = []
    def print_cls_var(self):
        print TestClassVariable.cls_var

t1 = TestClassVariable()
t2 = TestClassVariable()

print("Test class variable.")
print t1.cls_var, t2.cls_var
t2.cls_var = 4
print t1.cls_var, t2.cls_var  # only t2.cls_var was changed: 2, 4
TestClassVariable.cls_var = 5
print t1.cls_var, t2.cls_var  # only t1.cls_var was changed: 5, 4

print("Test class list.")
print t1.cls_list, t2.cls_list
t1.cls_list.append(1)
print t1.cls_list, t2.cls_list
