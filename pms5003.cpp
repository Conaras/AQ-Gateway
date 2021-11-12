#include "mbed.h"

#include "PMS3005.h"

PMS5003 pm25(D8, D2, NC); // UART TX, UART RX, POWER

static EventQueue queue; // The callback from the driver is triggered from IRQ, use EventQueue to debounce to normal context

void pm25_data_callback(pms5003_data_t data) {
    
    printf("---------------------------------------\n");
    printf("Concentration Units (standard)\n");
    printf("PM 1.0: %u", data.pm10_standard);
    printf("\t\tPM 2.5: %u", data.pm25_standard);
    printf("\t\tPM 10: %u\n", data.pm100_standard);
    printf("---------------------------------------\n");
    printf("Concentration Units (environmental)\n");
    printf("PM 1.0: %u", data.pm10_env);
    printf("\t\tPM 2.5: %u", data.pm25_env);
    printf("\t\tPM 10: %u\n", data.pm100_env);
    printf("---------------------------------------\n");
    printf("Particles > 0.3um / 0.1L air: %u\n", data.particles_03um);
    printf("Particles > 0.5um / 0.1L air: %u\n", data.particles_05um);
    printf("Particles > 1.0um / 0.1L air: %u\n", data.particles_10um);
    printf("Particles > 2.5um / 0.1L air: %u\n", data.particles_25um);
    printf("Particles > 5.0um / 0.1L air: %u\n", data.particles_50um);
    printf("Particles > 10.0 um / 0.1L air: %u\n", data.particles_100um);
    printf("---------------------------------------\n");
    //wait(7);
    
}

int main() {
    printf("Hello nibbber\n");

    // This callback runs in an interrupt context, thus we debounce to the event queue here
    pm25.enable(queue.event(&pm25_data_callback));
    printf("First Line\n");
    //pms5003_data_t data;
    printf("2nd Line\n");
    //pm25_data_callback(data);
    //printf("3rd Line\n");
    queue.dispatch_forever();
    printf("Last Line\n");
}


