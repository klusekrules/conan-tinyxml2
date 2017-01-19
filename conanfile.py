from conans import ConanFile, CMake, tools
import os


class TinyxmlConan(ConanFile):
    name = "tinyxml2"
    description="TinyXML-2 is a simple, small, efficient, C++ XML parser"
    version = "4.0.1"
    license = "MIT"
    url = "https://github.com/cinderblocks/conan-tinyxml2"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
       self.run("git clone https://github.com/leethomason/tinyxml2")
       self.run("cd tinyxml2 && git checkout %s" % self.version)

    def build(self):
        cmake = CMake(self.settings)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        self.run('cmake tinyxml2 %s %s' % (cmake.command_line, shared))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include/tinyxml2", src="tinyxml2")
        self.copy("*.dll", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a*", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["tinyxml2"]
