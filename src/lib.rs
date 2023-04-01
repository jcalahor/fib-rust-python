use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use pyo3::types::PyDict;
use pyo3::types::PyInt;
mod fib_calcs;

use fib_calcs::fib_number::__pyo3_get_function_fibonacci_number;
use fib_calcs::fib_numbers::__pyo3_get_function_fibonacci_numbers;


#[pyfunction]
fn say_hello() {
    println!("saying hello from Rust!");
}

#[pyfunction]
fn print_dicts(a: &PyDict) -> PyResult<i32> {
    let mut r = 0;
    for k in a.keys().iter() {
        let num =  a.get_item(&k).unwrap().downcast::<PyInt>()?.extract::<i32>().unwrap();
        println!("key: {} value: {}", k, num);
        r += num;
    }
    Ok(r);
}




#[pymodule]
fn fib_rust_python(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(say_hello));
    m.add_wrapped(wrap_pyfunction!(fibonacci_number));
    m.add_wrapped(wrap_pyfunction!(fibonacci_numbers));
    m.add_wrapped(wrap_pyfunction!(print_dicts));
    Ok(())
}
