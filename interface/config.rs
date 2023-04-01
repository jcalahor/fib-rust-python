use pyo3::prelude::{pyfunction, PyResult};
use pyo3::types::{PyDict, PyList};
use pyo3::exceptions::PyTypeError;
use crate::fib_calcs::fib_number::fibonacci_number;
use crate::fib_calcs::fib_numbers::fibonacci_numbers;
