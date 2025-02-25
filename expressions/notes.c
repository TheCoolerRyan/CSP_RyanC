//Ryan Crop, Expressions Notes C
#include <stdio.h>
#include <math.h> 
//this lets us do exponents
// Integers int when we set the variable and %d when we print
// Floats float when we set the variable and %f when we print
// strings (Words) char when we set the variable and %s when we print
int mynum;
float percent;
int add = 4+6;
int sub = 4-6;
int mul = 4*6;
float div = 6/4;
int mod = 6%4;
float ex = pow( 5, 2);

int main(void){
    printf("Type a number: \n");
    scanf("%d", &mynum);
    printf("You input %d\n", mynum);
    printf("Give me a percent as a decimal: \n");
    scanf("%f\n", &percent);
    printf("Your percent is %f\n" , percent);
    
    printf("%d\n", add);
    printf("%d\n", sub);
    mul = 7*4;
    printf("%d\n", mul);
    printf("%.23f\n", div);
    printf("%d\n", mod);
    printf("%f\n", ex);
    return 0;
}