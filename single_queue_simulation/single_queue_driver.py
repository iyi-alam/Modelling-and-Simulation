import numpy as np
import matplotlib.pyplot as plt
import os
from single_queue_geo_d_1 import single_queue_geo_d_1


def compare_plot(injection_rate_arr, waiting_time_simulation, 
                 waiting_time_analytical, save_folder, save_name, save_title):
    plt.figure()

    # Simulation curve:
    plt.plot(injection_rate_arr, waiting_time_simulation,
            '^k--', markersize=10, linewidth=1, label="Simulation")

    # Analytical curve:
    plt.plot(injection_rate_arr, waiting_time_analytical,
            'bo-', markersize=10, linewidth=1, label="Analytical")
    
    plt.legend(loc="upper left", fontsize=10, frameon=True)
    plt.xlabel("Injection Rate (packets/cycle)", fontsize=10)
    plt.ylabel("Average Waiting Time (cycles)", fontsize=10)
    # Force scientific notation on y-axis
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.title(save_title, fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.box(True)

    save_path = os.path.join(save_folder, save_name)
    plt.savefig(save_path)


def main():
    # Parameter Initialization
    service_time = 6 #deterministic
    injection_rate_arr = np.arange(0.05, 0.45, 0.05)  # -> increase stop limit a little bit to include the last point
    waiting_time_simulation = np.zeros(len(injection_rate_arr), dtype=np.float32)
    average_utilization = np.zeros(len(injection_rate_arr), dtype=np.float32)
    average_occupancy = np.zeros(len(injection_rate_arr), dtype=np.float32)
    #average_residual_time = np.zeros(len(injection_rate_arr), dtype=np.float32)
    simulation_length = 1000000

    waiting_time_analytical = np.zeros(len(injection_rate_arr), dtype=np.float32)
    #residual_time_analytical = np.zeros(len(injection_rate_arr), dtype=np.float32)

    for injection_rate_idx in range(len(injection_rate_arr)):
        injection_rate = injection_rate_arr[injection_rate_idx]

        # Simulation
        average_occupancy[injection_rate_idx], average_utilization[injection_rate_idx] = single_queue_geo_d_1(
            injection_rate=injection_rate,
            service_time=service_time,
            simulation_length=simulation_length
        )
        waiting_time_simulation[injection_rate_idx] = average_occupancy[injection_rate_idx] / injection_rate

        # Analytical
        rho = injection_rate*service_time
        waiting_time_analytical[injection_rate_idx] = 0.5*rho*(service_time-1)/(1-rho)
    
    compare_plot(injection_rate_arr, waiting_time_simulation, waiting_time_analytical, 
                 save_folder="/data/home/samsadalam/mtech_project/modelling_simulation/single_queue_simulation/outputs",
                 save_name=f"compare_svct_{service_time}_simlen_{simulation_length}.png",
                 save_title=f"Simulatio of Geo/D/1 Queue \n Service time = {service_time}, simulation length = {simulation_length}")


if __name__ == "__main__":
    main()