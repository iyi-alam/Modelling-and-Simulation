import random
random.seed(753)

def single_queue_geo_d_1(injection_rate, service_time, simulation_length):
    """
    Simulated a single queue for geo/d/1 system (clock driven simulation)
    Args:
        injection_rate: \lambda-rate of arrival of customers
        service_time: avg service time of the server, assumed deterministic
        simulation_length: total time period for which the simulation will be run
    """

    # Initialize state variables
    occupancy_counter = 0
    is_server_busy = False
    current_occupancy = 0
    utilization_counter = 0
    remaining_service_time = 0
    num_arrivals = 0
    arrival_this_cycle = False

    # Run Simulation
    for cycle in range(simulation_length):

        # Arrival Routine
        if random.uniform(0,1) <= injection_rate:
            current_occupancy += 1
            arrival_this_cycle = True
            num_arrivals += 1
        else:
            arrival_this_cycle = False
        
        # Service Routine
        if is_server_busy:
            remaining_service_time -= 1
            if remaining_service_time == 0:
                is_server_busy = False
            else:
                pass
        else:
            pass

        # Putting a packet into the server
        if not is_server_busy and current_occupancy > 0:
            is_server_busy = True
            current_occupancy -= 1
            remaining_service_time = service_time
        else:
            pass

        # Update Counters
        occupancy_counter += current_occupancy 
        if is_server_busy:
            utilization_counter += 1
        else:
            pass

        assert (occupancy_counter >= 0), "Occupancy counter fell below 0!"
        assert (current_occupancy >= 0), "Current occupancy fell below 0!"


    # Result Collection:
    average_occupancy = occupancy_counter/simulation_length
    average_utilization = utilization_counter/simulation_length

    return average_occupancy, average_utilization

