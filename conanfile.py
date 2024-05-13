import os
from conan import ConanFile


class Recipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("audiofile/1.1.1")
        self.requires("glog/0.7.0")
        self.requires("soundtouch/2.3.2")

    def layout(self):
        multi = True if self.settings.get_safe("compiler") == "msvc" else False
        if multi:
            self.folders.generators = os.path.join("build", "generators")
        else:
            self.folders.generators = os.path.join("build", str(self.settings.build_type), "generators")
