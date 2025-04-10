//Ryan Crop, Name Decorator 
#include <stdio.h>
#include <string.h>
char name [20];
char bedazled1[20] = "<-=-";
char bedazled2[20] = "-=->";
int main(void){
printf("Hello, what is your name?");
scanf("%s", name);
strcat(bedazled1, name);
strcat(bedazled1, bedazled2);
printf("Behold your knew and imporved name is...%s", bedazled1);
printf("!!!");
    return 0;
}