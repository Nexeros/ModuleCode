# modules/module_C.py

class ModuleC:
    def __init__(self, module_manager):
        self.name = "Module C"
        self.version = "1.0"
        self.manager = module_manager
        print(f"{self.name}: Initialization.")

    def setup(self):
        print(f"{self.name}: Setup.")

    def run(self):
        self.say_hello()

    def say_hello(self):
        print(f"{self.name}: Hello world!")

    def provide_info(self):
        return {"name": self.name, "version": self.version}


Module = ModuleC
