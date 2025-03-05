//Ryan Crop, Loop notes c
#include <stdio.h>

int main(void){
//What is a loop?  
    // a section of code that repates
//What are the two types of loops? 
     // For
//int x;
//for (x=0; x<10; x++){
    //printf("Hello");
//}
    //While
//int i= 1;
//while(i<10){
    //printf("%d\n", i);
    //i++;
//}
    //What is iteration 
        //The act of repeating
    //What are lists (Array)?
        // A bunch of values in one variable
    //How do you make lists (Arrays) in C?
int grades[] = {97, 95, 100, 94, 81, 96, 99};
    // In the brakets we say how long the list will be, if the list is set there brackets can be empty
    //data type is whatever is in the bracket

printf("%d\n", grades[3]); // To print one item we put the index number in the brackets when we print.
grades[2] = 73; // udapte grades one at a time using the index number
printf("%d\n", grades[2]);
//This tells me the number of bytes in it
printf("%lu", sizeof(grades));
//How to get the size of the array
int length = sizeof(grades)/sizeof(grades[0]);
printf("%d\n", length);

    //How do you make for loops in C?
    //Iterators should be x or i
int t;
for(t=0;t<=10;t+=2){
    printf("%d\n", t);
}
int l;
for(l=0; l< length; l++){
    printf("%d\n", grades[l]);
}
    //How do you make while loops in C?
int iterator= 100;
while(iterator>= 0){
    printf("%d\n", iterator);
    iterator -= 10;

}

char movies[][20] = {"Cinderella", "The Smerf Movie", "Transformers", "Cars", "Up", "1984"};
int mlength = sizeof(movies)/sizeof(movies[0]);
int m = 0;
while(m<mlength){
    printf("I like the movie %s\n", movies[m]);
    m++;
}

    return 0;
}