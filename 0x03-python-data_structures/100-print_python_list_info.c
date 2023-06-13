#include <Python.h>
/**
 * print_python_list_info - main func
 * @p: py object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int l_size;
	int i;
	PyListObject *l_obj;

	l_size = PyList_Size(p);
	l_obj = (PyListObject *)p;
	printf("[*] Size of the Python List = %li\n", l_size);
}
