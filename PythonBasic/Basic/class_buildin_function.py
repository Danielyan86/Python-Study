from PythonBasic.Basic import class_inheritence as cl

# 判断一个类是否是另一个类的子类
print(issubclass(cl.ElectricCar, cl.Car))
car_obj = cl.Car()
# 判断实例类型
print(isinstance(car_obj, cl.Car))
# 判断类属性
print(hasattr(car_obj, "color"))
# 获取类属性
print(getattr(car_obj, "color"))
print(dir(car_obj))
# 删除类属性
print(car_obj.condition)
print(delattr(car_obj, "color"))
print(dir(car_obj))
