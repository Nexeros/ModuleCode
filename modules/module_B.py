# modules/module_B.py

class ModuleB:
    def __init__(self, module_manager):
        self.name = "Module B"
        self.version = "1.2"
        self.manager = module_manager
        self.module_a_ref = None
        self.module_a_version = "1.0"
        print(f"{self.name}: Inicjalization.")

    def setup(self):
        print(f"{self.name}: Setup - connencting with A module.")
        self.module_a_ref = self.manager.get_module_instance("module_A")
        if self.module_a_ref:
            if self.module_a_ref.provide_info()["version"] == self.module_a_version:
                print(f"{self.name}: Connected to A module")
            else:
                raise Exception(f"{self.name}: {self.version}: "
                                f"{self.module_a_ref.provide_info()["name"]} {self.module_a_ref.provide_info()["version"]}"
                                f" not compatible, expected version {self.module_a_version}")
        else:
            print(f"{self.name}: Warning: Module A is not loaded or available.")

    def get_data_for_a(self):
        print(f"{self.name}: Providing data for Module A.")
        return "Chuj ci w dupę"

    def process_data_from_a(self, data):
        print(f"{self.name}: Processing data from A: '{data}'")
        if self.module_a_ref:
            info_from_a = self.module_a_ref.provide_info()
            print(f"{self.name}: Received from A: '{info_from_a}'")

    def provide_info(self):
        return {"name": self.name, "version": self.version}


Module = ModuleB
