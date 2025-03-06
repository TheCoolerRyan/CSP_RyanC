//Ryan Crop, My family Loop C
#include <stdio.h>

int main(void){
char famileys[][20] = {"Caden", "Julia", "Reese", "Justin", "Rachel"};
int mlength = sizeof(famileys)/sizeof(famileys[0]);
int m = 0;
while(m<mlength){
    printf("Hello %s Crop!\n", famileys[m]);
    m++;
}
    return 0;
}