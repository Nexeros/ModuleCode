import os
import importlib

MODULES_DIR = "./modules"


class ModuleManager:
    def __init__(self):
        self.loaded_modules = {}

    def load_modules(self):
        print("--- Loading modules ---")
        #Piszę żeby zobaczyć czy dizała w PyCharm pushowanie zmian na gita
        if not os.path.exists(os.path.join(MODULES_DIR, "__init__.py")):
            print(f"Warning: __init__.py file missing in folder '{MODULES_DIR}'. Creating file...")
            with open(os.path.join(MODULES_DIR, "__init__.py"), "w") as f:
                pass

        for filename in os.listdir(MODULES_DIR):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name_py = filename[:-3]
                try:
                    module_import_path = f"modules.{module_name_py}"
                    py_module = importlib.import_module(module_import_path)

                    if hasattr(py_module, "Module"):
                        ModuleClass = getattr(py_module, "Module")
                        module_instance = ModuleClass(self)
                        self.loaded_modules[module_name_py] = module_instance
                        print(f"Loaded and initialized: {module_instance.name}")
                    else:
                        print(f"Warning: Module {module_name_py} does not define a 'Module' class.")

                except ImportError as e:
                    print(f"Module import error: {module_name_py}: {e}")
                except Exception as e:
                    print(f"Error initializing module {module_name_py}: {e}")
        print("--- Modules loading finished ---\n")

    def setup_modules(self):
        print("--- Modules Setup ---")
        for module_name, module_instance in self.loaded_modules.items():
            if hasattr(module_instance, "setup"):
                try:
                    module_instance.setup()
                except Exception as e:
                    print(f"Error during module setup: {module_name}: {e}")
            else:
                print(f"Module {module_name} has no setup() method.")
        print("--- Modules Setup finished ---\n")

    def get_module_instance(self, module_name):
        return self.loaded_modules.get(module_name)

    def run_application_logic(self):
        print("--- Logic Startup ---")
        for module_instance in self.loaded_modules.values():
            if hasattr(module_instance, "run"):
                module_instance.run()

        print("--- Logic finished ---")


if __name__ == "__main__":
    manager = ModuleManager()
    manager.load_modules()
    manager.setup_modules()
    manager.run_application_logic()
