#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class UtfprocConan(ConanFile):
    name = "utf8proc"
    version = "2.1.0"
    url = "https://github.com/bincrafters/conan-utf8proc"
    description = "utf8proc is a small, clean C library that provides Unicode normalization, case-folding, and other operations for data in the UTF-8 encoding."
    license = "https://github.com/JuliaLang/utf8proc/blob/master/LICENSE.md"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [False]}
    default_options = {'shared': 'False'}
    export = ['utf8proc.h']

    def source(self):
        source_url = "https://github.com/JuliaLang/utf8proc/"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, "sources")
        #Rename to "sources" is a convention to simplify later steps

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="sources")
        cmake.build()

    def package(self):
        with tools.chdir("sources"):
            self.copy(pattern="LICENSE")
            self.copy(pattern="*utf8proc.h", dst="include/utf8proc", src="", keep_path=False)
            self.copy(pattern="*.dll", dst="bin", src="", keep_path=False)
            self.copy(pattern="*.lib", dst="lib", src="", keep_path=False)
            self.copy(pattern="*.a", dst="lib", src="", keep_path=False)
            self.copy(pattern="*.so*", dst="lib", src="", keep_path=False)
            self.copy(pattern="*.dylib", dst="lib", src="", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
