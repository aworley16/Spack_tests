# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install mpipcl
#
# You can edit this file again by typing:
#
#     spack edit mpipcl
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Mpipcl(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.github.com/mpi-advance/MPIPCL/"
    git = "https://github.com/mpi-advance/MPIPCL.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("BSD-3-Clause", checked_by="aworley16")

    version("1.3.0", commit="7c205e3")

    depends_on("c", type="build")

    # FIXME: Add dependencies if required.
    depends_on("mpi")
    depends_on("cmake @3.17:")

    variant("static_libs", default=False, description="Build MPIPCL static library")
    variant("dynamic_libs", default=True, description="Build MPIPCL shared library")        
    variant("debug", default=False, description="Turn on debug statments")
    variant("examples", default=False, description="Build Example programs")
    variant("Unique_names", default=False, description="Changes the types and names of functions to MPIP in)stead of MPIX")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        print("HELLO WORLD")
        if self.spec.satisfies("+static_libs"):
            print("HELLO--STATIC")
            args.append("-DSTATIC_LIBS=ON")

        if self.spec.satisfies("~dynamic_libs"):
            args.append("-DDYNAMIC_LIBS=OFF")
            print("HELLO--DYNAMIC")
        if self.spec.satisfies("+debug"):
            args.append("-DCMAKE_BUILD_TYPE=DEBUG")
            print("HELLO-- DEBUG")
        if self.spec.satisfies("+examples"):
            args.append("-DBUILD_EXAMPLES=ON")
            print("HELLO-- EXAMPLES")


        return args
