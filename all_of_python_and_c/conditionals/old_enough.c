//Ryan Crop, old enough c
#include <stdio.h>
#include <string.h>
int age;
int main(void){
printf("What is your age?\n");
scanf("%d", &age);
if (age >= 18 ){
    printf("Wow because your %d you can vote!\n", age);
}else if (age <18 && age >16){
    printf("Sorry but because your only %d years old, you can't vote, but you can drive, get your learners permit and go to school.\n", age);
}else if (age <18 && age > 15){
    printf("Sense your %d that means you can drive get your leanres permit and go to school but you cant vote!\n", age);
}else if (age == 15){
    printf("Sorry but sense your only %d you can't drive yet or vote, but you can get your learners permit and go to school.\n", age);
}else if (age < 16 && age > 14){
    printf("Wow being %d means you can get a Learners permit and go to school but you cant drive or vote!\n", age);
}else if (age < 15 && age > 5){
    printf("Sorry but sense your only %d you can't get your learners permit drive or vote but you can go to school.\n", age);
}else if(age >4 && age <15){
    printf("Wow, %d is old enough that you can go to school, but you cant get your learners permit drive or vote!\n", age);
}else{
    printf("Sorry but %d is not old enough to go to school, get your learners permit, drive, or vote.\n", age);
} 
    return 0;
}