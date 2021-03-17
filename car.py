class Car():
    def __init__(self,make,model,year):
      """
      初始化描述汽车的属性
      """
      self.make=make
      self.model=model
      self.year=year
      #给属性指定默认值
      self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return  long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self,mileage):
        """
        将里程表读数设置成指定的值
        禁止将里程表读数往回调
        :param mileage:
        :return:
        """
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You cant roll back on odometer")
    def increment(self,mils):
        """
        将里程表读数增加指定的量
        :param mils:
        :return:
        """
        self.odometer_reading+=mils
        "hello".print










