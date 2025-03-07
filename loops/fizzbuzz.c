//Ryan Crop, Template
#include <stdio.h>
int(numbers) = 1;
int main(void){
while (numbers >= 0 && numbers <51){
if(numbers % 15 == 0){
    printf("FizzBuzz!\n");
}else if(numbers % 5 == 0){
    printf("Buzz.\n");
}else if(numbers % 3 == 0){
    printf("Fizz.\n");
}else{
    printf("%d\n", numbers);
}
numbers += 1;
}
    return 0;
}