//Ryan Crop, jHow to get time in c
#include <stdio.h>
#include <time.h>


int main(void){
    //time_t seconds;
    //seconds = time(NULL);
    //printf("Seconds since jaunuary 1, 1970 = %d\n", seconds);

//Current time
    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);
    printf("Our current time and date is %s", asctime(timeinfo));

    //Gives us the current hour
    time_t now = time(NULL);
    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
    printf("%d", hour);
    return 0;
}