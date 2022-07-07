PyQt5 - Python Bindings for the Qt v5 Toolkit


COMMERCIAL VERSION

If you have the Commercial version of PyQt5 then you should also have a
license file that you downloaded separately.  The license file must be copied
to the "sip" directory before starting to build PyQt5.


INSTALLATION

Check for any other README files in this directory that relate to your
particular platform.  Feel free to contribute a README for your platform or to
provide updates to any existing documentation.

The first step is to configure PyQt5 by running the following command.

	python configure.py

This assumes that the correct Python interpreter is on your path.  Something
like the following may be appropriate on Windows.

	c:\python36\python configure.py

If you have multiple versions of Python installed then make sure you use the
interpreter for which you wish to generate bindings for.

The configure.py script takes many options.  Use the "--help" command line
option to display a full list of the available options.

The next step is to build PyQt5 using your platform's make command.

	make

The final step is to install PyQt5 by running the following command.
(Depending on your system you may require root or administrator privileges.)

	make install


THE REST OF THE DISTRIBUTION

The "examples" directory contain some examples of Python scripts, including
versions of the standard Qt tutorials and examples.

The "doc" directory contains HTML documentation for the bindings.
