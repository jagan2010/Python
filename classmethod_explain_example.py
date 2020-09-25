class Oracledb:
    def __init__(self,inst_type="RAC",inst_num=2):
        self.instance_type=inst_type
        self.num_instances=inst_num
    def description(self):
        print("This is",self.instance_type,"Database and has",self.num_instances,"instances")
    @classmethod
    def singleinstance(cls):
        instance_type="standalone"
        num_instances=1
