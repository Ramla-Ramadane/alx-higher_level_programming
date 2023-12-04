#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function prints information
 * about a Python list, including its size, allocated
 * space, and the type of each element
 * @p: points to list
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i;
	long int size = PyList_Size(p);
	PyListObject *list_obj = (PyListObject *)p;
	const char *Elm_type;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list_obj->allocated);
	for (i = 0; i < size; i++)
	{
		Elm_type = Py_TYPE(list_obj->ob_item[i])->tp_name;
		printf("Element %d: %s\n", i, Elm_type);
	}
}
