#include "bytesobject.h"
#include <stdio.h>
void print_python_bytes(PyObject *p)
{
	char *s[1024];
	Py_ssize_t len;

	PyBytes_AsStringAndSize(
			*p,      /* bytes object */
			char **s,           /* pointer to buffer variable */
			*len     /* pointer to length variable or NULL */
			);
	printf("%s\n", s);
}
