from conans import ConanFile
from conans.model import Generator

class cmake_find_paths(Generator):
    @property
    def filename(self):
        return "conan_cmake_find_paths"

    @property
    def content(self):
        cmake_find_paths = ";".join(dep_cpp_info.rootpath.replace("\\", "/")
                                    for _, dep_cpp_info in self.deps_build_info.dependencies)
        return cmake_find_paths


class CMakeFindPaths(ConanFile):
    name = "cmake_find_paths"
    version = "0.1"
    url = "https://github.com/memsharded/cmake_find_generator"
    license = "MIT"

    def build(self):
      pass

    def package_info(self):
      self.cpp_info.includedirs = []
      self.cpp_info.libdirs = []
      self.cpp_info.bindirs = []