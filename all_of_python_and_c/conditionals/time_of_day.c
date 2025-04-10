//Ryan Crop, Time of day C
#include <stdio.h>
#include <time.h>
int main(void){
    time_t now = time(NULL);
    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
if (hour > 5 & hour< 11){
    printf("Hello and good mourning.");
}else if(hour >= 11 & hour <= 16){
    printf("Hello, you should really be outside because its a great afternoon");
}else if (hour > 16 & hour < 21){
    printf("Hello I hope your having a great  evening but you should be heading to bed soon.");
}else{
    printf("Man! It's to early for this, go to bed! And have a good night!");
}
    return 0;
}