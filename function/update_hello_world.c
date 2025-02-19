//Ryan Crop, update hello world program C
#include <stdio.h>
void input(char type[50], int length){
    char name[50];
    printf("please give me a %s\n", type);
    getStr(name, sizeof(name)-1);
     return name;
}
int main(void){
printf("Hello World");
char name = word(name);
    return 0;
}