//Ryan Crop, Function Notes in c
#include <stdio.h>

//void add(int numOne,int numTwo){
    //printf("%d\n", numOne+numTwo);
//}
void input(char type[50], int length){
    char answer[50];
    printf("Please give me a %s\n", type);
    getStr(answer, sizeof(answer)-1);
    return answer;
}



int main(void){
//printf("Hello World\n");
//add(4,9);
//add(1000,2);
//add(47,9);
//add(82,-9);
char name = word("name");
printf("%s was %s until they somehow reached %s", word("name", 50), word("verb", 50), word("place", 50));
    return 0;
}