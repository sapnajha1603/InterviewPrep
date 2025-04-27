1. GoogleTest (C++ Example)

#include <gtest/gtest.h>

// Function to test
int add(int a, int b) {
    return a + b;
}

// Test case
TEST(AdditionTest, PositiveNumbers) {
    EXPECT_EQ(add(2, 3), 5);
    EXPECT_EQ(add(0, 0), 0);
}

// Main function for GoogleTest
int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

2. Pytest (Python Example)

# test_example.py

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0

Run using:

pytest test_example.py

3. Openpyxl (Reading and Writing Excel Files)

from openpyxl import Workbook, load_workbook

# Create a new Excel file
wb = Workbook()
ws = wb.active
ws.title = "Example Sheet"
ws.append(["ID", "Name", "Age"])
ws.append([1, "Alice", 30])
ws.append([2, "Bob", 25])
wb.save("example.xlsx")

# Read the Excel file
wb = load_workbook("example.xlsx")
ws = wb.active
for row in ws.iter_rows(values_only=True):
    print(row)

4. Pandas (Data Processing)

import pandas as pd

# Create a DataFrame
data = {"Name": ["Alice", "Bob"], "Age": [30, 25], "City": ["New York", "Los Angeles"]}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Save to CSV
df.to_csv("example.csv", index=False)

# Read from CSV
df = pd.read_csv("example.csv")
print("\nLoaded DataFrame:")
print(df)

5. dohq-artifactory (Downloading a File)

from artifactory import ArtifactoryPath

# Artifactory details
url = "https://artifactory.example.com/artifactory/repo/path/to/file.zip"
api_key = "your-api-key"

# Connect to Artifactory
path = ArtifactoryPath(url, apikey=api_key)

# Download the file
with path.open() as fd, open("file.zip", "wb") as out_file:
    out_file.write(fd.read())
print("File downloaded successfully.")

6. ctypes/pywin32 for Trace32

import ctypes

# Load the Trace32 DLL
trace32_dll = ctypes.WinDLL("path/to/trace32.dll")

# Example: Call a function from the DLL (replace with actual function)
result = trace32_dll.SomeFunction()  # Replace `SomeFunction` with the actual function name
print(f"Result: {result}")

Using pywin32:

import win32com.client

# Connect to Trace32
trace32 = win32com.client.Dispatch("Trace32.Application")
trace32.LoadProgram("path/to/program")
print("Program loaded.")

7. Threading with threading.Lock()

import threading

lock = threading.Lock()
shared_resource = []

def thread_function(name):
    with lock:
        shared_resource.append(name)
        print(f"{name} added to shared resource.")

threads = []
for i in range(5):
    thread = threading.Thread(target=thread_function, args=(f"Thread-{i}",))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Final shared resource:", shared_resource)

8. Multiprocessing

from multiprocessing import Process, Queue

def worker(queue, value):
    queue.put(value * 2)

if __name__ == "__main__":
    queue = Queue()
    processes = []

    for i in range(5):
        p = Process(target=worker, args=(queue, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    while not queue.empty():
        print(queue.get())

9. CProfile
import cProfile
import time

# Example function to profile
def slow_function():
    time.sleep(2)  # Simulating a slow operation
    print("Finished slow operation")

def fast_function():
    print("Finished fast operation")

# Main function
def main():
    slow_function()
    fast_function()

# Run the profiler
if __name__ == "__main__":
    cProfile.run("main()")

What Happens:

    The cProfile module runs the main() function and measures the execution time of each function.
    After execution, you’ll get a detailed report showing:
        The number of calls to each function.
        The total time spent in each function.
        The time spent per call.

Example Output:

         3 function calls in 2.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.002    2.002 <string>:1(<module>)
        1    0.000    0.000    2.002    2.002 script_name.py:5(main)
        1    2.002    2.002    2.002    2.002 script_name.py:2(slow_function)
        0    0.000             0.000          profile:0(profiler)
        1    0.000    0.000    0.000    0.000 script_name.py:8(fast_function)

How to Interpret:

    ncalls: Number of times the function was called.
    tottime: Total time spent in the function (excluding calls to other functions).
    cumtime: Cumulative time, including calls to other functions.

In this example, slow_function() took 2 seconds, which is the bottleneck.