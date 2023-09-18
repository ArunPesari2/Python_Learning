import time

# Function to calculate the sum of numbers in a given range
def calculate_sum(start, end):
    result = 0
    for number in range(start, end + 1):
        result += number
    return result

if __name__ == "__main__":
    # Define the range of numbers to calculate the sum
    start_number = 1
    end_number = 100000000  # A large range
    
    # Without multiprocessing
    start_time = time.time()
    result_without_multiprocessing = calculate_sum(start_number, end_number)
    end_time = time.time()
    
    # Calculate and print the time taken without multiprocessing
    time_without_multiprocessing = end_time - start_time
    print(f"Without multiprocessing:")
    print(f"Sum of numbers from {start_number} to {end_number}: {result_without_multiprocessing}")
    print(f"Time taken: {time_without_multiprocessing} seconds")
    
    # With multiprocessing
    import multiprocessing
    
    # Specify the number of processes to use
    num_processes = 4

    # Split the range into segments for each process
    segment_size = (end_number - start_number + 1) // num_processes
    
    # Create a multiprocessing Pool
    with multiprocessing.Pool(processes=num_processes) as pool:
        start_time = time.time()
        
        # Map the calculate_sum function to segments concurrently
        segments = [(start_number + i * segment_size, start_number + (i + 1) * segment_size - 1) for i in range(num_processes)]
        results = pool.starmap(calculate_sum, segments)
        
        end_time = time.time()
    
    # Calculate the total result from all processes
    total_result = sum(results)
    
    # Print the results and the time taken with multiprocessing
    print(f"\nWith multiprocessing:")
    print(segments)
    print(f"Sum of numbers from {start_number} to {end_number}: {total_result}")
    print(f"Time taken: {end_time - start_time} seconds")
