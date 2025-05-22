# modules/module_A.py

class ModuleA:
    def __init__(self, module_manager):
        self.name = "Module A"
        self.version = "1.0"
        self.manager = module_manager
        self.module_b_ref = None
        self.module_b_version = "1.0"
        print(f"{self.name}: Inicjalization.")

    def setup(self):
        print(f"{self.name}: Setup - connencting with B module.")
        self.module_b_ref = self.manager.get_module_instance("module_B")
        if self.module_b_ref:
            if self.module_b_ref.provide_info()["version"] == self.module_b_version:
                print(f"{self.name}: Connected to B module")
            else:
                raise Exception(f"{self.name}: {self.version}: "
                                f"{self.module_b_ref.provide_info()["name"]} {self.module_b_ref.provide_info()["version"]}"
                                f" not compatible, expected version {self.module_b_version}")
        else:
            print(f"{self.name}: Warning: Module B is not loaded or available.")

    def do_something_requiring_b(self):
        if self.module_b_ref:
            print(f"{self.name}: Performing an action that requires Module B.")
            data_from_b = self.module_b_ref.get_data_for_a()
            print(f"{self.name}: Recived form B: '{data_from_b}'")
            self.module_b_ref.process_data_from_a("Pierdol sie")
        else:
            print(f"{self.name}: Cannot perform the action, Module B is unavailable.")

    def run(self):
        self.do_something_requiring_b()

    def provide_info(self):
        return {"name": self.name, "version": self.version}


Module = ModuleA
