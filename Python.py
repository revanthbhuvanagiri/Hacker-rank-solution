class computers:
    def laptop_config(self):
        print("My laptop configuration is 16GB of RAM and 512GB of Storage")
    def desktop_config(self):
        print("My laptop configuration is 32GB of RAM and 1TB of Storage")
    def equal_config(self):
        print("Same config for both laptop and desktop")

laptop_specs = computers()
desktop_specs = computers()
same_specs = computers()

laptop_specs.laptop_config()
desktop_specs.desktop_config()
same_specs.equal_config()
