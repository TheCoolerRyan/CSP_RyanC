//Ryan Crop, Program.c
#include <stdio.h>

char name[] = "person";
int num = 42;
float pi = 3.14;
int mynum;
int main(void){
    printf("Hello %s, my age is %d and my favroite number is %f\n", name, num, pi);
    printf("type a number but don't tell me it: \n");
    scanf("%d", &mynum);
    printf("Your magic number is: %d", mynum);
    printf("\n Thats a cool one");
    return 0;
}