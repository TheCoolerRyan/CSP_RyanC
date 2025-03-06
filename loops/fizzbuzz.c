//Ryan Crop, Template
#include <stdio.h>
numbers = 0;
int main(void){
while (numbers >= 0 && numbers <51){
    if(numbers % 15 == 0){
    printf("FizzBuzz!");
}else if(numbers % 5 == 0){
    printf("Buzz.");
}else if(numbers % 3 == 0){
    printf("Fizz.");
}else{
    printf(numbers);
}}
    numbers += 1;
    return 0;
}