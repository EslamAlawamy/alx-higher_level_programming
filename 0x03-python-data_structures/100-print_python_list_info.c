#include <Python.h>
/**
 * print_python_list_info - main func
 * @p: py object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i = 0, list_len = 0;
	PyObject *item;
	PyListObject *clone = (PyListObject *) p;

	list_len = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", list_len);
}
